# decode(_:from:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

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
func decode<T>(_ type: T.Type, from data: Data) throws -> T where T : Decodable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkdecoder/decode(_:from:))*