# send(_:type:lastMessage:metadata:)

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
final func send<Content>(_ content: Content, type: Int, lastMessage: Bool = false, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}) async throws where Content : DataProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/send(_:type:lastmessage:metadata:))*