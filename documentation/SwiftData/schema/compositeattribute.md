# Schema.CompositeAttribute

**Framework**: SwiftData  
**Kind**: class  
**Role**: Class

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
- [init(name: String, originalName: String?, options: [Schema.Attribute.Option], valueType: any Any.Type, defaultValue: Any?, hashModifier: String?)](./compositeattribute/init%28name,originalname,options,valuetype,defaultvalue,hashmodifier%29.md)
### Composing attributes
- [var properties: [Schema.Attribute]](./compositeattribute/properties.md)
### Encoding and decoding
- [func encode(to: any Encoder) throws](./compositeattribute/encode%28to%29.md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](./compositeattribute/init%28from%29.md)
### Debugging
- [var debugDescription: String](./compositeattribute/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
### Operators
- [static func == (Schema.CompositeAttribute, Schema.CompositeAttribute) -> Bool](./compositeattribute/eqeq%28_,_%29.md)

## Relationships

### Inherits From
- [Schema.Attribute](./attribute.md)
### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [SchemaProperty](../schemaproperty.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Attributes
- [Schema.Attribute](./attribute.md)
  An object that describes the configuration and behavior of a specific property of a model class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/compositeattribute)*