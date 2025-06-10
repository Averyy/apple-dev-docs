# prependProtocols(_:)

**Framework**: Network  
**Kind**: method

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
final func prependProtocols<NewApplicationProtocol>(@ProtocolStackBuilder<NewApplicationProtocol> _ builder: () -> NewApplicationProtocol) -> NetworkConnection<NewApplicationProtocol> where NewApplicationProtocol : OneToOneProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/prependprotocols(_:))*