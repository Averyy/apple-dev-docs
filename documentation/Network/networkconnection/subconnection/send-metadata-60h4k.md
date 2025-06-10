# send(_:metadata:)

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
final func send<Sending, Receiving, CoderType>(_ content: Sending, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where SubApplicationProtocol == Coder<Sending, Receiving, CoderType>, Sending : Encodable, Receiving : Decodable, CoderType : NetworkCoder
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/subconnection/send(_:metadata:)-60h4k)*