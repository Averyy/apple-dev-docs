# init(type:length:_:)

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
init<T, L, BelowProtocol>(type: T.Type, length: L.Type, @ProtocolStackBuilder<BelowProtocol> _ builder: () -> BelowProtocol) where T : Sendable, T : UnsignedInteger, L : Sendable, L : UnsignedInteger, BelowProtocol : StreamProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tlv/init(type:length:_:)-h8s)*