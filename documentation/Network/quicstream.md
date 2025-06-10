# QUICStream

**Framework**: Network  
**Kind**: struct

The default QUIC Stream type for Subconnection objects returned from a NetworkConnection over QUIC. Connection’s parameterized over QUICStream will expose a nearly identical stream interface as TCP. This type is not intended to be inserted into the protocol stack manually.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct QUICStream
```

## Topics

### Instance Properties
- [let belowProtocol: Void](quicstream/belowprotocol.md)
### Enumerations
- [QUICStream.Directionality](quicstream/directionality.md)
- [QUICStream.Initiator](quicstream/initiator.md)

## Relationships

### Conforms To
- [NetworkProtocolOptions](networkprotocoloptions.md)
- [OneToOneProtocol](onetooneprotocol.md)
- [StreamProtocol](streamprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/quicstream)*