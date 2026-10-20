# streamApplicationErrorCode

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The QUIC application error code to send for the stream, or received from the peer.

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
var streamApplicationErrorCode: UInt64 { get set }
```

## See Also

### Handling Errors
- [var applicationError: NWProtocolQUIC.ApplicationError](./applicationerror.md)
  The QUIC application error code to send for the connection, or received from the peer.
- [NWProtocolQUIC.ApplicationError](../applicationerror.md)
  A QUIC application error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolquic/metadata/streamapplicationerrorcode)*