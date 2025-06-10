# PropertyListDecoder

**Framework**: Foundation  
**Kind**: class

An object that decodes instances of data types from a property list.

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
class PropertyListDecoder
```

## Topics

### Decoding
- [init()](propertylistdecoder/init.md)
  Creates a new, reusable property list decoder.
- [func decode<T>(T.Type, from: Data) throws -> T](propertylistdecoder/decode(_:from:).md)
  Returns a value of the specified type by decoding a property list using the default property list format.
### Customizing Decoding
- [func decode<T>(T.Type, from: Data, format: inout PropertyListDecoder.PropertyListFormat) throws -> T](propertylistdecoder/decode(_:from:format:).md)
  Returns a value of the specified type by decoding a property list using the supplied format.
- [var userInfo: [CodingUserInfoKey : any Sendable]](propertylistdecoder/userinfo.md)
  A dictionary you use to customize decoding by providing contextual information.
### Instance Methods
- [func decode<T, C>(T.Type, from: Data, configuration: C.Type) throws -> T](propertylistdecoder/decode(_:from:configuration:)-1m1ya.md)
- [func decode<T>(T.Type, from: Data, configuration: T.DecodingConfiguration) throws -> T](propertylistdecoder/decode(_:from:configuration:)-62fzt.md)
- [func decode<T>(T.Type, from: Data, format: inout PropertyListDecoder.PropertyListFormat, configuration: T.DecodingConfiguration) throws -> T](propertylistdecoder/decode(_:from:format:configuration:)-1frbk.md)
- [func decode<T, C>(T.Type, from: Data, format: inout PropertyListDecoder.PropertyListFormat, configuration: C.Type) throws -> T](propertylistdecoder/decode(_:from:format:configuration:)-2epy4.md)
### Type Aliases
- [PropertyListDecoder.PropertyListFormat](propertylistdecoder/propertylistformat.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [NetworkDecoder](../Network/NetworkDecoder.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TopLevelDecoder](../Combine/TopLevelDecoder.md)

## See Also

- [class PropertyListEncoder](propertylistencoder.md)
  An object that encodes instances of data types to a property list.
- [class PropertyListSerialization](propertylistserialization.md)
  An object that converts between a property list and one of several serialized representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistdecoder)*