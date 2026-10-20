# PropertyListEncoder

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that encodes instances of data types to a property list.

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
class PropertyListEncoder
```

## Mentions

- [Encoding and Decoding Custom Types](./encoding-and-decoding-custom-types.md)

## Topics

### Encoding
- [init()](./propertylistencoder/init%28%29.md)
  Creates a new, reusable property list encoder with the default formatting settings.
- [func encode<Value>(Value) throws -> Data](./propertylistencoder/encode%28_%29.md)
  Returns a property list that represents an encoded version of the value you supply.
- [func encode<T, C>(T, configuration: C.Type) throws -> Data](./propertylistencoder/encode%28_,configuration%29-4biuh.md)
- [func encode<T>(T, configuration: T.EncodingConfiguration) throws -> Data](./propertylistencoder/encode%28_,configuration%29-5ee8q.md)
### Customizing Encoding
- [var outputFormat: PropertyListDecoder.PropertyListFormat](./propertylistencoder/outputformat.md)
  A value that determines which property list format is used during encoding.
- [var userInfo: [CodingUserInfoKey : any Sendable]](./propertylistencoder/userinfo.md)
  A dictionary you use to customize the encoding process by providing contextual information.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [NetworkEncoder](../Network/networkencoder.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TopLevelEncoder](../Combine/toplevelencoder.md)

## See Also

### Property Lists
- [class PropertyListDecoder](./propertylistdecoder.md)
  An object that decodes instances of data types from a property list.
- [class PropertyListSerialization](./propertylistserialization.md)
  An object that converts between a property list and one of several serialized representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistencoder)*