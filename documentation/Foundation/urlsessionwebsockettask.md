# URLSessionWebSocketTask

**Framework**: Foundation  
**Kind**: class

A URL session task that communicates over the WebSockets protocol standard.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class URLSessionWebSocketTask
```

#### Overview

[`URLSessionWebSocketTask`](urlsessionwebsockettask.md) is a concrete subclass of [`URLSessionTask`](urlsessiontask.md) that provides a message-oriented transport protocol over TCP and TLS in the form of WebSocket framing. It follows the WebSocket Protocol defined in [`RFC 6455`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6455).

You create a [`URLSessionWebSocketTask`](urlsessionwebsockettask.md) with either a `ws:` or `wss:` URL. When creating the task, you can also provide a list of protocols to advertise during the handshake phase. Once the handshake completes, your app receives notifications through the session’s [`delegate`](urlsession/delegate.md).

You send data with [`send(_:completionHandler:)`](urlsessionwebsockettask/send(_:completionhandler:).md) and receive data with [`receive(completionHandler:)`](urlsessionwebsockettask/receive(completionhandler:).md). The task performs reads and writes asynchronously, and allows you to send and receive messages that contain both binary frames and UTF-8 encoded text frames. The task enqueues any reads or writes you perform prior to the handshake’s completion, and executes them after the handshake completes.

[`URLSessionWebSocketTask`](urlsessionwebsockettask.md) supports redirection and authentication like other types of tasks do, using the methods in [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md). The WebSocket task calls the redirection and authentication delegate methods prior to completing the handshake. The WebSocket task also supports cookies, by storing cookies to the session configuration’s [`httpCookieStorage`](urlsessionconfiguration/httpcookiestorage.md), and attaches cookies to outgoing HTTP handshake requests.

> **Note**:  watchOS supports [`URLSessionWebSocketTask`](urlsessionwebsockettask.md) for specific use cases. For more details, see [`TN3135: Low-level networking on watchOS`](https://developer.apple.com/documentation/Technotes/tn3135-low-level-networking-on-watchOS).

## Topics

### Sending and receiving data
- [func send(URLSessionWebSocketTask.Message, completionHandler: ((any Error)?) -> Void)](urlsessionwebsockettask/send(_:completionhandler:).md)
  Sends a WebSocket message, receiving the result in a completion handler.
- [URLSessionWebSocketTask.Message](urlsessionwebsockettask/message.md)
  An enumeration of the types of messages sent and received.
- [func receive(completionHandler: (Result<URLSessionWebSocketTask.Message, any Error>) -> Void)](urlsessionwebsockettask/receive(completionhandler:).md)
  Reads a WebSocket message once all the frames of the message are available.
- [var maximumMessageSize: Int](urlsessionwebsockettask/maximummessagesize.md)
  The maximum number of bytes to buffer before the receive call fails with an error.
### Sending ping frames
- [func sendPing(pongReceiveHandler: ((any Error)?) -> Void)](urlsessionwebsockettask/sendping(pongreceivehandler:).md)
  Sends a ping frame from the client side, with a closure to receive the pong from the server endpoint.
### Closing the connection
- [func cancel(with: URLSessionWebSocketTask.CloseCode, reason: Data?)](urlsessionwebsockettask/cancel(with:reason:).md)
  Sends a close frame with the given close code and optional close reason.
- [var closeCode: URLSessionWebSocketTask.CloseCode](urlsessionwebsockettask/closecode-swift.property.md)
  A code that indicates the reason a connection closed.
- [URLSessionWebSocketTask.CloseCode](urlsessionwebsockettask/closecode-swift.enum.md)
  A code that indicates why a WebSocket connection closed.
- [var closeReason: Data?](urlsessionwebsockettask/closereason.md)
  A block of data that provides further information about why a connection closed.
### Instance Methods
- [func receive() async throws -> URLSessionWebSocketTask.Message](urlsessionwebsockettask/receive.md)
- [func send(URLSessionWebSocketTask.Message) async throws](urlsessionwebsockettask/send(_:).md)

## Relationships

### Inherits From
- [URLSessionTask](urlsessiontask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](progressreporting.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func webSocketTask(with: URL) -> URLSessionWebSocketTask](urlsession/websockettask(with:)-87ipz.md)
  Creates a WebSocket task for the provided URL.
- [func webSocketTask(with: URLRequest) -> URLSessionWebSocketTask](urlsession/websockettask(with:)-mtks.md)
  Creates a WebSocket task for the provided URL request.
- [func webSocketTask(with: URL, protocols: [String]) -> URLSessionWebSocketTask](urlsession/websockettask(with:protocols:).md)
  Creates a WebSocket task given a URL and an array of protocols.
- [protocol URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to WebSocket tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/urlsessionwebsockettask)*