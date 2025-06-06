# NWProtocolQUIC.ApplicationError

**Framework**: Network  
**Kind**: struct

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
- [init(code: UInt64, reason: String?)](nwprotocolquic/applicationerror/init(code:reason:).md)
  Initializes a QUIC application error with an error code and an optional reason.
### Inspecting Application Errors
- [let code: UInt64](nwprotocolquic/applicationerror/code.md)
  The QUIC application error code.
- [let reason: String?](nwprotocolquic/applicationerror/reason.md)
  The QUIC application error reason.

## Relationships

### Conforms To
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var applicationError: NWProtocolQUIC.ApplicationError](nwprotocolquic/metadata/applicationerror.md)
  The QUIC application error code to send for the connection, or received from the peer.
- [var streamApplicationErrorCode: UInt64](nwprotocolquic/metadata/streamapplicationerrorcode.md)
  The QUIC application error code to send for the stream, or received from the peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/applicationerror)*