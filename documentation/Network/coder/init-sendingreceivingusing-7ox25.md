# init(sending:receiving:using:_:)

**Framework**: Network  
**Kind**: init

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
init<BelowProtocol>(sending: Sending.Type, receiving: Coder<Sending, _Receiving, CoderType>.Receiving.Type, using: CoderType, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where BelowProtocol : DatagramProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/coder/init(sending:receiving:using:_:)-7ox25)*