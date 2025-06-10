# URLSessionWebSocketTask.CloseCode

**Framework**: Foundation  
**Kind**: enum

A code that indicates why a WebSocket connection closed.

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
enum CloseCode
```

#### Overview

The WebSocket close codes follow the close codes defined in [`RFC 6455`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6455#section-7.4.1).

## Topics

### Close codes
- [URLSessionWebSocketTask.CloseCode.abnormalClosure](urlsessionwebsockettask/closecode-swift.enum/abnormalclosure.md)
  A reserved code that indicates the connection closed without a close control frame.
- [URLSessionWebSocketTask.CloseCode.goingAway](urlsessionwebsockettask/closecode-swift.enum/goingaway.md)
  A code that indicates an endpoint is going away.
- [URLSessionWebSocketTask.CloseCode.internalServerError](urlsessionwebsockettask/closecode-swift.enum/internalservererror.md)
  A code that indicates the server terminated the connection because it encountered an unexpected condition.
- [URLSessionWebSocketTask.CloseCode.invalid](urlsessionwebsockettask/closecode-swift.enum/invalid.md)
  A code that indicates the connection is still open.
- [URLSessionWebSocketTask.CloseCode.invalidFramePayloadData](urlsessionwebsockettask/closecode-swift.enum/invalidframepayloaddata.md)
  A code that indicates the server terminated the connection because it received data inconsistent with the message’s type.
- [URLSessionWebSocketTask.CloseCode.mandatoryExtensionMissing](urlsessionwebsockettask/closecode-swift.enum/mandatoryextensionmissing.md)
  A code that indicates the client terminated the connection because the server didn’t negotiate a required extension.
- [URLSessionWebSocketTask.CloseCode.messageTooBig](urlsessionwebsockettask/closecode-swift.enum/messagetoobig.md)
  A code that indicates an endpoint is terminating the connection because it received a message too big for it to process.
- [URLSessionWebSocketTask.CloseCode.noStatusReceived](urlsessionwebsockettask/closecode-swift.enum/nostatusreceived.md)
  A reserved code that indicates an endpoint expected a status code and didn’t receive one.
- [URLSessionWebSocketTask.CloseCode.normalClosure](urlsessionwebsockettask/closecode-swift.enum/normalclosure.md)
  A code that indicates normal connection closure.
- [URLSessionWebSocketTask.CloseCode.policyViolation](urlsessionwebsockettask/closecode-swift.enum/policyviolation.md)
  A code that indicates an endpoint terminated the connection because it received a message that violates its policy.
- [URLSessionWebSocketTask.CloseCode.protocolError](urlsessionwebsockettask/closecode-swift.enum/protocolerror.md)
  A code that indicates an endpoint terminated the connection due to a protocol error.
- [URLSessionWebSocketTask.CloseCode.tlsHandshakeFailure](urlsessionwebsockettask/closecode-swift.enum/tlshandshakefailure.md)
  A reserved code that indicates the connection closed due to the failure to perform a TLS handshake.
- [URLSessionWebSocketTask.CloseCode.unsupportedData](urlsessionwebsockettask/closecode-swift.enum/unsupporteddata.md)
  A code that indicates an endpoint terminated the connection after receiving a type of data it can’t accept.
### Initializers
- [init?(rawValue: Int)](urlsessionwebsockettask/closecode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func cancel(with: URLSessionWebSocketTask.CloseCode, reason: Data?)](urlsessionwebsockettask/cancel(with:reason:).md)
  Sends a close frame with the given close code and optional close reason.
- [var closeCode: URLSessionWebSocketTask.CloseCode](urlsessionwebsockettask/closecode-swift.property.md)
  A code that indicates the reason a connection closed.
- [var closeReason: Data?](urlsessionwebsockettask/closereason.md)
  A block of data that provides further information about why a connection closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/closecode-swift.enum)*