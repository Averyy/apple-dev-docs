# MultiplexProtocol

**Framework**: Network  
**Kind**: protocol

Types that conform to MultiplexProtocol are allowed to be the top protocol in a network protocol stack for multiplexing network connection objects. Generally network protocols conforming to this will not directly expose send or receive methods. Instead, they usually expose methods to open and listen for multiplexed Subconnections which can be sent and received on

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
protocol MultiplexProtocol : NetworkProtocolOptions
```

## Relationships

### Inherits From
- [NetworkProtocolOptions](networkprotocoloptions.md)
### Conforming Types
- [QUIC](quic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/multiplexprotocol)*