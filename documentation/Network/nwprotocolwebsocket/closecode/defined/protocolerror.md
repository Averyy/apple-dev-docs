# NWProtocolWebSocket.CloseCode.Defined.protocolError

**Framework**: Network  
**Kind**: case

An endpoint is terminating the connection due to a protocol error.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case protocolError
```

## See Also

- [NWProtocolWebSocket.CloseCode.Defined.normalClosure](nwprotocolwebsocket/closecode/defined/normalclosure.md)
  A normal closure occurred with no errors.
- [NWProtocolWebSocket.CloseCode.Defined.goingAway](nwprotocolwebsocket/closecode/defined/goingaway.md)
  An endpoint is no longer available, such as when a server is down.
- [NWProtocolWebSocket.CloseCode.Defined.unsupportedData](nwprotocolwebsocket/closecode/defined/unsupporteddata.md)
  An endpoint is terminating the connection because it received a type of data it cannot accept.
- [NWProtocolWebSocket.CloseCode.Defined.noStatusReceived](nwprotocolwebsocket/closecode/defined/nostatusreceived.md)
  This value is reserved for local errors and indicates that no Close code was received.
- [NWProtocolWebSocket.CloseCode.Defined.abnormalClosure](nwprotocolwebsocket/closecode/defined/abnormalclosure.md)
  This value is reserved for local errors and indicates that no Close message was received.
- [NWProtocolWebSocket.CloseCode.Defined.invalidFramePayloadData](nwprotocolwebsocket/closecode/defined/invalidframepayloaddata.md)
  An endpoint is terminating the connection because it received data within a message that was inconsistent with the message type.
- [NWProtocolWebSocket.CloseCode.Defined.policyViolation](nwprotocolwebsocket/closecode/defined/policyviolation.md)
  An endpoint is terminating the connection because it received a message that violates its policy.
- [NWProtocolWebSocket.CloseCode.Defined.messageTooBig](nwprotocolwebsocket/closecode/defined/messagetoobig.md)
  An endpoint is terminating the connection because it received a message that is too big for it to process.
- [NWProtocolWebSocket.CloseCode.Defined.mandatoryExtension](nwprotocolwebsocket/closecode/defined/mandatoryextension.md)
  The WebSocket client expected the server to negotiate one or more extensions that were not negotiated.
- [NWProtocolWebSocket.CloseCode.Defined.internalServerError](nwprotocolwebsocket/closecode/defined/internalservererror.md)
  The server is terminating the connection because it encountered an unexpected condition that prevented it from fulfilling the request.
- [NWProtocolWebSocket.CloseCode.Defined.tlsHandshake](nwprotocolwebsocket/closecode/defined/tlshandshake.md)
  This value is reserved for local errors and indicates that the TLS handshake failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode/defined/protocolerror)*