# NWProtocolQUIC.ApplicationError

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

A QUIC application error code.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct ApplicationError
```

## Topics

### Configuring Application Errors
- [init(code: UInt64, reason: String?)](./applicationerror/init%28code,reason%29.md)
  Initializes a QUIC application error with an error code and an optional reason.
### Inspecting Application Errors
- [let code: UInt64](./applicationerror/code.md)
  The QUIC application error code.
- [let reason: String?](./applicationerror/reason.md)
  The QUIC application error reason.

## Relationships

### Conforms To
- [ExpressibleByIntegerLiteral](../../Swift/expressiblebyintegerliteral.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling Errors
- [var applicationError: NWProtocolQUIC.ApplicationError](./metadata/applicationerror.md)
  The QUIC application error code to send for the connection, or received from the peer.
- [var streamApplicationErrorCode: UInt64](./metadata/streamapplicationerrorcode.md)
  The QUIC application error code to send for the stream, or received from the peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/applicationerror)*