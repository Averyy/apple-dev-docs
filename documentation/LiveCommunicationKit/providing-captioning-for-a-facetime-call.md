# Providing captioning for a FaceTime call

**Framework**: LiveCommunicationKit  
**Role**: Article

Connect to FaceTime Web to provide real-time caption services.

## Overview

Using the [`LiveAssistanceExtension`](./liveassistanceextension.md) and [`LiveAssistance`](./liveassistance.md) APIs, your app can invite a provider to a FaceTime call to deliver assistance, such as interpreting or captioning services. To support captioning in a call, FaceTime also supports a WebSocket API to deliver captions in real time. Your captioning app uses this API by making a connection to `localhost` on a reserved port. As you send captions over the WebSocket, FaceTime Web delivers them to the other participants in the call.

### Perform call and captioning setup

The process begins when a particpant in a call requests assistance services. If your app has the `com.apple.developer.conversation-accessibility` entitlement and provides a [`LiveAssistanceExtension`](./liveassistanceextension.md), the system offers it as a service provider. If the call participant chooses your app, your extension receives a call to the [`prepareAssistanceRequest(_:)`](./liveassistanceextension/prepareassistancerequest%28_%29.md) method.

As part of handling the assistance request, your extension receives a URL to allow an assistance provider join the call. Prior to forwarding this URL to your backend and from there to an individual to provide the service, FaceTime requires that you modify the URL to indicate the provider’s role. There are two roles:

- **captioner**: A provider who provides textual captions during the call. Opening this URL on the captioner’s device opens FaceTime Web and connects to the WebSocket running in the captioning app, as described later.
- **interpreter**: A provider who performs sign language interpretation during the call. This type currently has no specific behavior, but is reserved for future use.

Rewrite the URL by adding a `type` parameter to express the assistance provider’s role. For example, if your extension receives the following URL:

```
https://facetime.apple.com/join#v=1&p=<p>&k=<k>
```

Rewrite it to add `type=captioner`, like this:

```
https://facetime.apple.com/join?type=captioner#v=1&p=<p>&k=<k>
```

> 💡 **Tip**: Accurately parse the URL to rewrite it, since FaceTime links contain a fragment (`#`) that naïve string concatenation can break.

Forward the modified URL to an assistance provider. Opening the URL on their machine launches FaceTime Web to join the call. If the key-value pair `type=captioner` is present, FaceTime Web also connects to your captioning app’s WebSocket at `ws://localhost:12703`. The port `12703` is hardcoded into FaceTime Web and isn’t configurable; your captioning app must listen on this port. Make sure your app verifies that the connection’s origin is `https://facetime.apple.com`.

If the captioning app isn’t running when the URL opens the FaceTime call, FaceTime Web retries every few seconds to establish the WebSocket connection. This delay allows FaceTime Web to adopt an existing caption connection created by another participant, rather than creating a duplicate connection. After FaceTime Web establishes the WebSocket connection to the captioning app, it begins a captioning session that broadcasts captions to all call participants.

### Send captioning messages and receive responses

Your captioning app provides captions by sending JSON strings over the WebSocket connection. A caption message contains the text to send, a timestamp, and a sequence number, as described in [Send Caption Message](./captioning-caption-message.md).

The following example sends “Hello world” as the first caption in a session:

```json
{
  "type": "caption",
  "text": "Hello world\n",
  "timestamp": "2026-02-02T20:41:49.116Z",
  "seq": 1
}
```

In the `text` string, include a linefeed (`\n`) character at the end of each line. The on-screen captions render this character as the end of a line; omitting the character leaves the line open to receiving further text. For more information about the specific requirements of this message’s payload, see [Send Caption Message](./captioning-caption-message.md).

When FaceTime Web receives your caption message, it responds with a success or failure message. A success message looks like the following:

```json
{
  "type": "success",
  "timestamp": "2026-02-02T20:41:49.116Z",
  "seq": 1
}
```

The sequence number (`seq`) corresponds  to the sequence number you sent in the original caption message. [Receive Success Message](./captioning-success-message.md) describes the success message in further detail.

When an error occurs, FaceTime Web responds with an error message, which looks like the following:

```json
{
  "type": "error",
  "error": "invalid_request",
  "description": "The request format is invalid",
  "seq": 1
}
```

As with the success message, the sequence number (`seq`) corresponds to the caption message that caused the error. See [Receive Error Message](./captioning-error-message.md) for information about the possible error messages and their meanings.

In either the success or error case, your captioning app increments the sequence number prior to sending its next caption message. This process uniquely identifies caption messages, and makes it possible to correlate caption messages to their success or error responses.

> ❗ **Important**: FaceTime Web imposes a rate limit of 4,096 bytes of caption text per 1,000-millisecond window, and refuses any text over that limit. Only the contents of the `text` value counts against this limit, not the rest of the JSON message. The count returns to zero after 1,000 ms have elapsed, rather than refilling gradually. The timing window is anchored to your first caption after the previous window elapses; track your send times to know when the budget resets. A refused caption spends nothing, so a single caption larger than the whole budget doesn’t consume the window.

### Handle disconnection and reconnection

FaceTime Web may disconnect the WebSocket in mid-call, for example as a result of the web page reloading. If this happens, FaceTime Web establishes a new WebSocket connection. Upon receiving the new connection, have your captioning app send a sequence message, which looks like the following:

```json
{
  "type": "seq"
}
```

FaceTime web responds with a sequence number, which looks like this:

```json
{
  "type": "seq",
  "seq": 42
}
```

The sequence number your captioning app receives represents the last caption that FaceTime Web successfully sent. Resume captioning from the next sequence number above this one; don’t attempt to backfill any sequence numbers below it.

See [Send Sequence Message](./captioning-send-sequence-message.md) and [Receive Sequence Message](./captioning-receive-sequence-message.md) for more details about resuming captioning after a WebSocket disconnect.

> 💡 **Tip**: It’s legal (and recommended) to send a sequence message when your captioning app initially accepts the WebSocket connection, prior to sending the first caption.

FaceTime Web’s connection to the call is separate from its WebSocket connection to the captioning app, and can fail due to conditions like network disruptions. If FaceTime Web needs to replace its connection to the call, caption messages sent during the outage fail with the error `no_call`. This failure isn’t an indication that the call is over; rather, it means that the call is temporarily unavailable. Continue re-sending the caption message until it succeeds. The wait is usually only a few seconds, but it doesn’t have a limit; you can keep trying.

When the call actually ends, FaceTime Web closes the WebSocket connection. The ending of the connection is your captioning app’s cue to handle the close event, clean up any associated state, and release any resources allocated for the captioning session.

### Use a bridge server, if necessary

Some caption apps can’t implement WebSocket handling directly, such as apps that only support HTTP-based caption protocols. In this case, you can run a local bridge server that translates HTTP requests into the WebSocket protocol and forwards responses as HTTP status codes. The following diagram shows this arrangement. ![A flow diagram showing three apps and how they interact to handle caption messaging. On the left, the CAT client uses HTTP to communicate with a bridge server in the middle of the diagram. The bridge server then uses a WebSocket connection to communicate with FaceTime Web on the right side of the diagram.](https://developer.apple.com/tutorials/images/com.apple.livecommunicationkit/ft-bridge-server@2x.png) If necessary, implement the bridge server as follows:

1. Listen on the WebSocket port (`ws://localhost:12703`) for FaceTime Web to connect, as described above.
2. Expose an HTTP endpoint, such as `POST / closedcaption`, compatible with the captioning client’s protocol.
3. Translate incoming HTTP requests from the captioning app into `CaptionMessage` objects and forward them over the WebSocket. The bridge server might need to supply the line terminator, depending on the HTTP protocol it implements. If the protocol includes line breaks as data, forward the body verbatim. Otherwise, append `\n` if the protocol defines each request as one finished line.
4. When the bridge server receives a response from FaceTime Web, return HTTP status codes to the captioning client, as described in the following table.

| Trigger | Returned HTTP status code |
| --- | --- |
| `SuccessMessage` | `200` |
| `ErrorMessage`: `no_call` | `400` |
| `ErrorMessage`: `rate_limited` | `429` |
| `ErrorMessage`: `unknown` | `500` |
| Client called `GET /closedcaption/seq` but no WebSocket connection is present. | `503` |
| The WebSocket relay to FaceTime Web failed or timed out. | `504` |

The case of an `ErrorMessage` with error string `no_call` represents a call not yet joined, or being reestablished. After returning HTTP status `400`, retry until the WebSocket closes or the WebSocket sends an `invalid_request` error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/providing-captioning-for-a-facetime-call)*