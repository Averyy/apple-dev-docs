# URLSessionWebSocketTask.CloseCode.mandatoryExtensionMissing

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A code that indicates the client terminated the connection because the server didn’t negotiate a required extension.

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
case mandatoryExtensionMissing
```

```c
NSURLSessionWebSocketCloseCodeMandatoryExtensionMissing
```

## Discussion

RFC 6455 indicates the client should provide a [`closeReason`](../closereason.md) with a list of the needed extensions.

## See Also

### Close codes
- [URLSessionWebSocketTask.CloseCode.abnormalClosure](./abnormalclosure.md)
  A reserved code that indicates the connection closed without a close control frame.
- [URLSessionWebSocketTask.CloseCode.goingAway](./goingaway.md)
  A code that indicates an endpoint is going away.
- [URLSessionWebSocketTask.CloseCode.internalServerError](./internalservererror.md)
  A code that indicates the server terminated the connection because it encountered an unexpected condition.
- [URLSessionWebSocketTask.CloseCode.invalid](./invalid.md)
  A code that indicates the connection is still open.
- [URLSessionWebSocketTask.CloseCode.invalidFramePayloadData](./invalidframepayloaddata.md)
  A code that indicates the server terminated the connection because it received data inconsistent with the message’s type.
- [URLSessionWebSocketTask.CloseCode.messageTooBig](./messagetoobig.md)
  A code that indicates an endpoint is terminating the connection because it received a message too big for it to process.
- [URLSessionWebSocketTask.CloseCode.noStatusReceived](./nostatusreceived.md)
  A reserved code that indicates an endpoint expected a status code and didn’t receive one.
- [URLSessionWebSocketTask.CloseCode.normalClosure](./normalclosure.md)
  A code that indicates normal connection closure.
- [URLSessionWebSocketTask.CloseCode.policyViolation](./policyviolation.md)
  A code that indicates an endpoint terminated the connection because it received a message that violates its policy.
- [URLSessionWebSocketTask.CloseCode.protocolError](./protocolerror.md)
  A code that indicates an endpoint terminated the connection due to a protocol error.
- [URLSessionWebSocketTask.CloseCode.tlsHandshakeFailure](./tlshandshakefailure.md)
  A reserved code that indicates the connection closed due to the failure to perform a TLS handshake.
- [URLSessionWebSocketTask.CloseCode.unsupportedData](./unsupporteddata.md)
  A code that indicates an endpoint terminated the connection after receiving a type of data it can’t accept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/closecode-swift.enum/mandatoryextensionmissing)*