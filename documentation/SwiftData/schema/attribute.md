# Schema.Attribute

**Framework**: SwiftData  
**Kind**: class

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
- [init(Schema.Attribute.Option..., originalName: String?, hashModifier: String?)](schema/attribute/init(_:originalname:hashmodifier:).md)
- [init(name: String, originalName: String?, options: [Schema.Attribute.Option], valueType: any Any.Type, defaultValue: Any?, hashModifier: String?)](schema/attribute/init(name:originalname:options:valuetype:defaultvalue:hashmodifier:).md)
### Specifying value information
- [var defaultValue: Any?](schema/attribute/defaultvalue.md)
### Determining behavior
- [var options: [Schema.Attribute.Option]](schema/attribute/options.md)
- [var isTransformable: Bool](schema/attribute/istransformable.md)
### Versioning
- [var hashModifier: String?](schema/attribute/hashmodifier.md)
### Structures
- [Schema.Attribute.Option](schema/attribute/option.md)

## Relationships

### Inherited By
- [Schema.CompositeAttribute](schema/compositeattribute.md)
### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [SchemaProperty](schemaproperty.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Schema.CompositeAttribute](schema/compositeattribute.md)
  An object that describes an attribute that derives its value by composing other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/attribute)*