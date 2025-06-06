# userInfo

**Framework**: Foundation  
**Kind**: property

A dictionary you use to customize the decoding process by providing contextual information.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@preconcurrency
var userInfo: [CodingUserInfoKey : any Sendable] { get set }
```

## See Also

- [var keyDecodingStrategy: JSONDecoder.KeyDecodingStrategy](jsondecoder/keydecodingstrategy-swift.property.md)
  A value that determines how to decode a type’s coding keys from JSON keys.
- [JSONDecoder.KeyDecodingStrategy](jsondecoder/keydecodingstrategy-swift.enum.md)
  The values that determine how to decode a type’s coding keys from JSON keys.
- [var allowsJSON5: Bool](jsondecoder/allowsjson5.md)
  Specifies that decoding supports the JSON5 syntax.
- [var assumesTopLevelDictionary: Bool](jsondecoder/assumestopleveldictionary.md)
  Specifies that decoding assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with braces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/userinfo)*