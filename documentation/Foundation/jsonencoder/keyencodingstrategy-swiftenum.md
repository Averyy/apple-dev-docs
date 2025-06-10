# JSONEncoder.KeyEncodingStrategy

**Framework**: Foundation  
**Kind**: enum

The values that determine how to encode a type’s coding keys as JSON keys.

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
enum KeyEncodingStrategy
```

#### Overview

> **Note**:  Key encoding strategies other than [`JSONEncoder.KeyEncodingStrategy.useDefaultKeys`](jsonencoder/keyencodingstrategy-swift.enum/usedefaultkeys.md) may have a noticeable performance cost because those strategies may inspect and transform each key.

## Topics

### Built-in Encoding
- [JSONEncoder.KeyEncodingStrategy.convertToSnakeCase](jsonencoder/keyencodingstrategy-swift.enum/converttosnakecase.md)
  A key encoding strategy that converts camel-case keys to snake-case keys.
- [JSONEncoder.KeyEncodingStrategy.useDefaultKeys](jsonencoder/keyencodingstrategy-swift.enum/usedefaultkeys.md)
  A key encoding strategy that doesn’t change key names during encoding.
### Custom Encoding
- [case custom(([any CodingKey]) -> any CodingKey)](jsonencoder/keyencodingstrategy-swift.enum/custom(_:).md)
  A key encoding strategy defined by the closure you supply.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var outputFormatting: JSONEncoder.OutputFormatting](jsonencoder/outputformatting-swift.property.md)
  A value that determines the readability, size, and element order of the encoded JSON object.
- [JSONEncoder.OutputFormatting](jsonencoder/outputformatting-swift.struct.md)
  The output formatting options that determine the readability, size, and element order of an encoded JSON object.
- [var keyEncodingStrategy: JSONEncoder.KeyEncodingStrategy](jsonencoder/keyencodingstrategy-swift.property.md)
  A value that determines how to encode a  type’s coding keys as JSON keys.
- [var userInfo: [CodingUserInfoKey : any Sendable]](jsonencoder/userinfo.md)
  A dictionary you use to customize the encoding process by providing contextual information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum)*