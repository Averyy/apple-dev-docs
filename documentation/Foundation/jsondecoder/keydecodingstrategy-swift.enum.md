# JSONDecoder.KeyDecodingStrategy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The values that determine how to decode a type’s coding keys from JSON keys.

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
enum KeyDecodingStrategy
```

#### Overview

> **Note**:  Key decoding strategies other than [`JSONDecoder.KeyDecodingStrategy.useDefaultKeys`](./keydecodingstrategy-swift.enum/usedefaultkeys.md) may have a noticeable performance cost because those strategies may inspect and transform each key.

## Topics

### Built-in Decoding
- [JSONDecoder.KeyDecodingStrategy.convertFromSnakeCase](./keydecodingstrategy-swift.enum/convertfromsnakecase.md)
  A key decoding strategy that converts snake-case keys to camel-case keys.
- [JSONDecoder.KeyDecodingStrategy.useDefaultKeys](./keydecodingstrategy-swift.enum/usedefaultkeys.md)
  A key decoding strategy that doesn’t change key names during decoding.
### Custom Decoding
- [case custom(([any CodingKey]) -> any CodingKey)](./keydecodingstrategy-swift.enum/custom%28_%29.md)
  A key decoding strategy defined by the closure you supply.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing Decoding
- [var keyDecodingStrategy: JSONDecoder.KeyDecodingStrategy](./keydecodingstrategy-swift.property.md)
  A value that determines how to decode a type’s coding keys from JSON keys.
- [var userInfo: [CodingUserInfoKey : any Sendable]](./userinfo.md)
  A dictionary you use to customize the decoding process by providing contextual information.
- [var allowsJSON5: Bool](./allowsjson5.md)
  Specifies that decoding supports the JSON5 syntax.
- [var assumesTopLevelDictionary: Bool](./assumestopleveldictionary.md)
  Specifies that decoding assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with braces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/keydecodingstrategy-swift.enum)*