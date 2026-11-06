# Send Caption Message

**Framework**: LiveCommunicationKit  
**Role**: Article

Send content and timing information for an individual caption.

## JSON

```json
    interface CaptionMessage {
      type: "caption";
      text: string;
      timestamp: string;
      seq: number;
    }
```

## Parameters

| Member | Type | Description |
| --- | --- | --- |
| `type` | String | The string `caption`. |
| `text` | String | The caption text, including line terminators. |
| `timestamp` | String | An ISO-8601 timestamp. In JavaScript, call `Date.toISOString()`. |
| `seq` | Number | A unique sequence number to identify the caption message to response messages. Any success or error message sent back from FaceTime Web contains this same number. |

## Discussion

Your captioning app or bridge server sends this message over the WebSocket to deliver an individual caption to the FaceTime call. Upon receipt, FaceTime Web attempts to forward the message to the other clients in the call. If successsful, FaceTime Web responds with a `SuccessMessage`; otherwise, it sends an `ErrorMessage`. Both of these response messages use the same sequence number as the original `CaptionMessage`

Send the message as a JSON string, similar to the following:

```json
{
  "type": "caption",
  "text": "Hello world.\n",
  "timestamp": "2026-02-02T20:41:49.116Z",
  "seq": 1
}
```

### Sending valid caption text

Use line breaks (`\n`) in the `text` member to indicate the actual ends of lines. The captioning service interprets line breaks as valid data, not a consequence of message framing. Make sure your captioning app ends each finished line of text with the `\n` character. A message with no terminating `\n` character leaves the line open and available for continuation by the next message. The system reserves this kind of open line for streaming as the captioner types it. However, no current system sends such a stream, so a message with no terminator is effectively a bug in the captioning application, and results in consecutive sentences running together on screen.

Don’t send an empty value for `text`; FaceTime Web responds to this with an `"invalid_request"` error. You can send a single line terminator (`\n`) as the `text` value.

## See Also

### WebSocket messages
- [Receive Success Message](./captioning-success-message.md)
  Receive confirmation that FaceTime Web delivered a caption message to the call.
- [Receive Error Message](./captioning-error-message.md)
  Receive notification that FaceTime Web couldn’t deliver a caption to the call.
- [Send Sequence Message](./captioning-send-sequence-message.md)
  Request the most recent sequence number from the FaceTime Web service.
- [Receive Sequence Message](./captioning-receive-sequence-message.md)
  Receive the most recent sequence number from the FaceTime Web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/captioning-caption-message)*