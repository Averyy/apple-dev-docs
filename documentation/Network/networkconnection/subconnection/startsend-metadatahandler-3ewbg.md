# startSend(_:metadata:handler:)

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
final func startSend(_ content: String, @ProtocolMetadataBuilder metadata builder: () -> [NWProtocolMetadata] = {[]}, handler: ((String, Bool) async throws -> Void) async throws -> Void) async throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/subconnection/startsend(_:metadata:handler:)-3ewbg)*