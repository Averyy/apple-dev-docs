# decode(_:from:)

**Framework**: Combine  
**Kind**: method  
**Required**: Yes

Decodes an instance of the indicated type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func decode<T>(_ type: T.Type, from: Self.Input) throws -> T where T : Decodable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/topleveldecoder/decode(_:from:))*