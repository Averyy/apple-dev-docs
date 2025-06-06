# Schema.CompositeAttribute

**Framework**: SwiftData  
**Kind**: class

An object that describes an attribute that derives its value by composing other attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
final class CompositeAttribute
```

## Topics

### Creating a composite attribute
- [init(name: String, originalName: String?, options: [Schema.Attribute.Option], valueType: any Any.Type, defaultValue: Any?, hashModifier: String?)](schema/compositeattribute/init(name:originalname:options:valuetype:defaultvalue:hashmodifier:).md)
### Composing attributes
- [var properties: [Schema.Attribute]](schema/compositeattribute/properties.md)
### Encoding and decoding
- [func encode(to: any Encoder) throws](schema/compositeattribute/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](schema/compositeattribute/init(from:).md)
### Debugging
- [var debugDescription: String](schema/compositeattribute/debugdescription.md)
  A textual representation of this instance, suitable for debugging.

## Relationships

### Inherits From
- [Schema.Attribute](schema/attribute.md)
### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [SchemaProperty](schemaproperty.md)

## See Also

- [Schema.Attribute](schema/attribute.md)
  An object that describes the configuration and behavior of a specific property of a model class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/compositeattribute)*