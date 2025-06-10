# sendIdempotent(_:endOfStream:metadata:)

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
final func sendIdempotent<Content>(_ content: Content, endOfStream: Bool = false, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) where Content : DataProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/sendidempotent(_:endofstream:metadata:)-85rup)*