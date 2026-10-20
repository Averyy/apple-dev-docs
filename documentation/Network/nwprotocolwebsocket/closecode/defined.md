# NWProtocolWebSocket.CloseCode.Defined

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

Well-known close code values.

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
enum Defined
```

## Topics

### Defined Close Codes
- [NWProtocolWebSocket.CloseCode.Defined.normalClosure](./defined/normalclosure.md)
  A normal closure occurred with no errors.
- [NWProtocolWebSocket.CloseCode.Defined.goingAway](./defined/goingaway.md)
  An endpoint is no longer available, such as when a server is down.
- [NWProtocolWebSocket.CloseCode.Defined.protocolError](./defined/protocolerror.md)
  An endpoint is terminating the connection due to a protocol error.
- [NWProtocolWebSocket.CloseCode.Defined.unsupportedData](./defined/unsupporteddata.md)
  An endpoint is terminating the connection because it received a type of data it cannot accept.
- [NWProtocolWebSocket.CloseCode.Defined.noStatusReceived](./defined/nostatusreceived.md)
  This value is reserved for local errors and indicates that no Close code was received.
- [NWProtocolWebSocket.CloseCode.Defined.abnormalClosure](./defined/abnormalclosure.md)
  This value is reserved for local errors and indicates that no Close message was received.
- [NWProtocolWebSocket.CloseCode.Defined.invalidFramePayloadData](./defined/invalidframepayloaddata.md)
  An endpoint is terminating the connection because it received data within a message that was inconsistent with the message type.
- [NWProtocolWebSocket.CloseCode.Defined.policyViolation](./defined/policyviolation.md)
  An endpoint is terminating the connection because it received a message that violates its policy.
- [NWProtocolWebSocket.CloseCode.Defined.messageTooBig](./defined/messagetoobig.md)
  An endpoint is terminating the connection because it received a message that is too big for it to process.
- [NWProtocolWebSocket.CloseCode.Defined.mandatoryExtension](./defined/mandatoryextension.md)
  The WebSocket client expected the server to negotiate one or more extensions that were not negotiated.
- [NWProtocolWebSocket.CloseCode.Defined.internalServerError](./defined/internalservererror.md)
  The server is terminating the connection because it encountered an unexpected condition that prevented it from fulfilling the request.
- [NWProtocolWebSocket.CloseCode.Defined.tlsHandshake](./defined/tlshandshake.md)
  This value is reserved for local errors and indicates that the TLS handshake failed.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Close Code Types
- [init(rawValue: UInt16) throws](./init%28rawvalue%29.md)
  Initializes a close code with a raw value.
- [case protocolCode(NWProtocolWebSocket.CloseCode.Defined)](./protocolcode%28_%29.md)
  A well-known close code reserved by the protocol (values 1000-2999).
- [NWProtocolWebSocket.CloseCode.applicationCode(_:)](./applicationcode%28_%29.md)
  A close code in the range reserved for applications and frameworks (3000-3999).
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](./privatecode%28_%29.md)
  A close code in the private-use range (4000-4999).


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode/defined)*