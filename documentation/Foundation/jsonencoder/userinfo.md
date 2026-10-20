# userInfo

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A dictionary you use to customize the encoding process by providing contextual information.

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

### Customizing Encoding
- [var outputFormatting: JSONEncoder.OutputFormatting](./outputformatting-swift.property.md)
  A value that determines the readability, size, and element order of the encoded JSON object.
- [JSONEncoder.OutputFormatting](./outputformatting-swift.struct.md)
  The output formatting options that determine the readability, size, and element order of an encoded JSON object.
- [var keyEncodingStrategy: JSONEncoder.KeyEncodingStrategy](./keyencodingstrategy-swift.property.md)
  A value that determines how to encode a  type’s coding keys as JSON keys.
- [JSONEncoder.KeyEncodingStrategy](./keyencodingstrategy-swift.enum.md)
  The values that determine how to encode a type’s coding keys as JSON keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/userinfo)*