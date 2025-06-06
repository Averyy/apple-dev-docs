# userInfo

**Framework**: Foundation  
**Kind**: property

A dictionary you use to customize decoding by providing contextual information.

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

- [func decode<T>(T.Type, from: Data, format: inout PropertyListDecoder.PropertyListFormat) throws -> T](propertylistdecoder/decode(_:from:format:).md)
  Returns a value of the specified type by decoding a property list using the supplied format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistdecoder/userinfo)*