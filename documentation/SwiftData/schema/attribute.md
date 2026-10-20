# Schema.Attribute

**Framework**: SwiftData  
**Kind**: class  
**Role**: Class

An object that describes the configuration and behavior of a specific property of a model class.

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
class Attribute
```

## Topics

### Creating an attribute
- [init(Schema.Attribute.Option..., originalName: String?, hashModifier: String?)](./attribute/init%28_,originalname,hashmodifier%29.md)
- [init(name: String, originalName: String?, options: [Schema.Attribute.Option], valueType: any Any.Type, defaultValue: Any?, hashModifier: String?)](./attribute/init%28name,originalname,options,valuetype,defaultvalue,hashmodifier%29.md)
### Specifying value information
- [var defaultValue: Any?](./attribute/defaultvalue.md)
### Determining behavior
- [var options: [Schema.Attribute.Option]](./attribute/options.md)
- [var isTransformable: Bool](./attribute/istransformable.md)
### Versioning
- [var hashModifier: String?](./attribute/hashmodifier.md)
### Structures
- [Schema.Attribute.Option](./attribute/option.md)
### Instance Properties
- [var isCodable: Bool](./attribute/iscodable.md)

## Relationships

### Inherited By
- [Schema.CompositeAttribute](./compositeattribute.md)
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
- [Schema.CompositeAttribute](./compositeattribute.md)
  An object that describes an attribute that derives its value by composing other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/attribute)*