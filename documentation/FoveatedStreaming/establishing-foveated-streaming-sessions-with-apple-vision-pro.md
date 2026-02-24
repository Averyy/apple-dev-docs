# Establishing foveated streaming sessions with Apple Vision Pro

**Framework**: Foveated Streaming

Discover, pair, and manage streaming sessions between Apple Vision Pro and local streaming endpoints by implementing the session management connection protocol.

#### Overview

Before foveated streaming can begin, Apple Vision Pro and your local streaming endpoint must discover each other on the same network, securely pair through certificate-based authentication, and establish a communication channel to coordinate the streaming session life cycle. The session management connection protocol handles this foundational layer — operating independently of the stream — to ensure reliable connection establishment and session state synchronization.

Implement this TCP-based protocol in your streaming application by doing the following:

- Broadcast an mDNS service from the streaming endpoint to permit discovery by Apple Vision Pro.
- Receive and acknowledge connection requests.
- Receive and acknowledge barcode presentation requests.
- Alert Apple Vision Pro when the streaming endpoint is ready to stream content.
- Continuously observe the state of the streaming session.
- Send Apple Vision Pro disconnection requests.

> **Note**: Implementing the session management connection protocol is one of several steps involved in streaming your desktop application to Apple Vision Pro. For more information on the other steps, see [`Streaming a CloudXR application to Apple Vision Pro with foveation`](streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md).

#### Make Your Streaming Endpoint Discoverable

Set the mDNS service name to `_apple-foveated-streaming._tcp`. This tells Apple Vision Pro that it can connect to your streaming endpoint by broadcasting an mDNS service from your desktop .

Add an entry to the mDNS service’s TXT record that specifies the bundle ID of the Apple Vision Pro app that initiates connections:

| Key | Value |
| --- | --- |
| `Application-Identifier` | The bundle ID of the visionOS app. |

If you don’t specify the bundle ID of your visionOS app it won’t be able to connect to the streaming endpoint.

For more information on building a visionOS app to display your streamed content, see [`Creating a foveated streaming client on visionOS`](creating-a-foveated-streaming-client-on-visionos.md).

#### Interpret the Messaging Format

Apple Vision Pro uses a TCP connection with the IP address and port number the mDNS service advertises to send and receive messages.

Each message between the Apple Vision Pro and the streaming application begins with a 4 byte, unsigned, little-endian number that indicates the length of the incoming message. The message itself is in JSON, so each message looks like the following:

```swift
// The size in bytes of the JSON packet, in little endian (0x25 == 37 bytes).
25000000
// Followed by the JSON payload. This example encodes the following in UTF-8:
// { "ClientID": "123456789ABCDEF0" }
7B202243 6C69656E 74494422 3A202231 3233342D 35363738 2D394142 432D4445 46302220 7D
```

Because TCP doesn’t provide a mechanism to define the size of an atomic “packet”, it’s necessary to prefix each message between the Apple Vision Pro and the streaming application with the message length.

#### Acknowledge a Connection Request

Apple Vision Pro sends a connection request to your streaming endpoint when it initiates the connection. The connection request defines the streaming parameters and provides the necessary information for establishing and managing the foveated streaming session.

The following is an example of a `RequestConnection` message:

```json
{
    "Event": "RequestConnection",
    "ProtocolVersion": "1",
    "StreamingProvider": "com.nvidia.CloudXR",
    "StreamingProviderVersion": "6",
    "UserInterfaceIdiom": "Vision",
    "SessionID": "68753A444D6F12269C600050E4C00067",
    "ClientID": "a81bc81bdead4e5dabff90865d1e13b1"
}
```

The following table describes each parameter in the `RequestConnection` message:

| Parameter | Type | Description |
| --- | --- | --- |
| `Event` | `String` | Always set to `RequestConnection`. |
| `ProtocolVersion` | `String` | The protocol version to use. This is always set to `1`. |
| `StreamingProvider` | `String` | The specific streaming provider the Apple Vision Pro is requesting. By convention, this is a reverse DNS style string, like `com.example.technology`. |
| `StreamingProviderVersion` | `String` | The version information for the streaming provider. |
| `UserInterfaceIdiom` | `String` | The [`UIUserInterfaceIdiom`](https://developer.apple.com/documentation/UIKit/UIUserInterfaceIdiom) of the source device. Always set to `Vision` when streaming to Apple Vision Pro. |
| `SessionID` | `String` | A UUID which uniquely identifies this specific foveated streaming session. |
| `ClientID` | `String` | A UUID which uniquely identifies the Apple Vision Pro device. Persists between sessions; used for pairing. |

Acknowledge the connection request message by sending the Apple Vision Pro an `AcknowledgeConnection` message, for example:

```json
{
    "Event": "AcknowledgeConnection",
    "SessionID": "68753A444D6F12269C600050E4C00067",
    "ServerID": "5d542eab102b46caa5801cf3f9f33c3a",
    "CertificateFingerprint": "<fingerprint>"
}
```

The following table describes each parameter in the `AcknowledgeConnection` message:

| Parameter | Type | Description |
| --- | --- | --- |
| `Event` | `String` | Always set to `AcknowledgeConnection`. |
| `SessionID` | `String` | The UUID which uniquely identifies this specific foveated streaming session. Must match the session ID sent in `RequestConnection`, else the connection fails. |
| `ServerID` | `String` | A UUID which uniquely identifies the streaming endpoint. Persists between sessions; used for pairing. |
| `CertificateFingerprint` (Optional) | `String` | Contains the contents of the certificate fingerprint which the streaming application presents in the pairing barcode. Omit this value to force a re-pair. |

The Apple Vision Pro expects this response from the streaming endpoint after sending its initial connection request message.

The streaming endpoint can deny the connection by sending a `RequestSessionDisconnect` message. For more information, see [`Request a session disconnect`](establishing-foveated-streaming-sessions-with-apple-vision-pro#Request-a-session-disconnect.md).

#### Acknowledge a Barcode Presentation Request

After the streaming application acknowledges the connection request, Apple Vision Pro may request that you present a QR code to authenticate the connection.

The following is an example `RequestBarcodePresentation` message:

```json
{
    "Event": "RequestBarcodePresentation",
    "SessionID": "68753A444D6F12269C600050E4C00067"
}
```

The following table describes each parameter in the `RequestBarcodePresentation` message:

| Parameter | Type | Description |
| --- | --- | --- |
| `Event` | `String` | Always set to `RequestBarcodePresentation`. |
| `SessionID` | `String` | The UUID which uniquely identifies this specific foveated streaming session. Matches the session ID sent in `RequestConnection`. |

Apple Vision Pro expects the streaming application to present a QR code after receiving this message. For an example that demonstrates how to present a QR code with the necessary authentication information, see the [`StreamingSession-WindowsApp`](https://developer.apple.comhttps://github.com/apple/StreamingSession/tree/main/StreamingSession-WindowsApp/).

After the streaming application presents the QR code, send Apple Vision Pro an `AcknowledgeBarcodePresentation` message:

```json
{
    "Event": "AcknowledgeBarcodePresentation",
    "SessionID": "68753A444D6F12269C600050E4C00067"
}
```

The following table describes each parameter in the `AcknowledgeBarcodePresentation` message:

| Parameter | Type | Description |
| --- | --- | --- |
| `Event` | `String` | Always set to `AcknowledgeBarcodePresentation`. |
| `SessionID` | `String` | The UUID which uniquely identifies this specific foveated streaming session. Must match the session ID sent in `RequestConnection`. |

After receiving this message, Apple Vision Pro presents the barcode scanning UI.

#### Notify Apple Vision Pro That Youre Ready to Stream

Send a message to Apple Vision Pro when your streaming endpoint is ready to receive CloudXR™ connections and stream content.

The following is an example `MediaStreamIsReady` message:

```json
{
    "Event": "MediaStreamIsReady",
    "SessionID": "68753A444D6F12269C600050E4C00067"
}
```

The following table describes each parameter in the `MediaStreamIsReady` message:

| Parameter | Type | Description |
| --- | --- | --- |
| `Event` | `String` | Always set to `MediaStreamIsReady`. |
| `SessionID` | `String` | The UUID which uniquely identifies this specific foveated streaming session. Must match the session ID sent in `RequestConnection`. |

Apple Vision Pro doesn’t attempt to connect to your streaming application’s CloudXR port until it receives this message, giving your application time to launch the CloudXR server.

#### Track the Streaming Session Status

Apple Vision Pro sends messages when the foveated streaming session status changes.

The following is an example `SessionStatusDidChange` message:

```json
{
    "Event": "SessionStatusDidChange",
    "SessionID": "68753A444D6F12269C600050E4C00067",
    "Status": "CONNECTING"
}
```

The following table describes each parameter in the `SessionStatusDidChange` message:

| Parameter | Type | Description |
| --- | --- | --- |
| `Event` | `String` | Always set to `SessionStatusDidChange`. |
| `SessionID` | `String` | The UUID which uniquely identifies this specific foveated streaming session. Matches the session ID sent in `RequestConnection`. |
| `Status` | `String` | The current status of the streaming session. See the list of Status values, below. |

Status values for the `SessionStatusDidChange` message include:

- **`WAITING`**: The streaming provider is ready to connect to the endpoint, but the `MediaStreamIsReady` message hasn’t been sent.
- **`CONNECTING`**: The streaming provider is connecting to the remote endpoint. This can be reached from the `PAUSED` state.
- **`CONNECTED`**: The streaming provider is connected and streaming. This state always follows the `CONNECTING` state.
- **`PAUSED`**: The streaming session is active, but the streaming provider’s connection has been disconnected, such as when the person takes off their Apple Vision Pro. This state is recoverable and considered normal.
- **`DISCONNECTED`**: The streaming session is fully disconnected. This status may also be sent during pairing if the person cancels pairing.

> **Note**: Dismiss the QR code as soon as you receive the `SessionStatusDidChange` message. If pairing failed, the state will be `DISCONNECTED`.

#### Request a Session Disconnect

Sometimes your streaming application may need to request that the session disconnects, such as when the person quits the streaming application on the computer while the streaming session is still running.

To request disconnection, send a `RequestSessionDisconnect` message, for example:

```json
{
    "Event": "RequestSessionDisconnect",
    "SessionID": "68753A444D6F12269C600050E4C00067"
}
```

The following table describes each parameter in the `RequestSessionDisconnect` message:

| Parameter | Type | Description |
| --- | --- | --- |
| `Event` | `String` | Always set to `RequestSessionDisconnect`. |
| `SessionID` | `String` | The UUID which uniquely identifies this specific foveated streaming session. Must match the session ID sent in `RequestConnection`. |

This message may also be sent during pairing, which cancels the pairing process on Apple Vision Pro.

#### Understand Reconnection Behavior

When a person takes off their Apple Vision Pro, Apple Vision Pro sends a `SessionStatusDidChange` message with the `PAUSED` status. After sending the `PAUSED` status, Apple Vision Pro cancels the streaming connection and gracefully disconnects the TCP connection. When the person puts their Apple Vision Pro back on, Apple Vision Pro attempts to reconnect to the streaming endpoint, sending a `SessionStatusDidChange` message with the current state to alert the endpoint that the session is still active.

Keep your streaming application running after it receives a `SessionStatusDidChange` message with a `PAUSED` status to ensure the person can reconnect.

## See Also

- [Streaming a CloudXR application to Apple Vision Pro with foveation](streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md)
  Integrate NVIDIA CloudXR™ and the session management connection protocol into your desktop or cloud application to stream high-fidelity spatial content to Apple Vision Pro.
- [Creating a foveated streaming client on visionOS](creating-a-foveated-streaming-client-on-visionos.md)
  Build a visionOS app that streams high-fidelity immersive content from a computer or the cloud using the Foveated Streaming framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/establishing-foveated-streaming-sessions-with-apple-vision-pro)*