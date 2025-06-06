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
- [var valueType: any Any.Type](schema/attribute/valuetype.md)
### Managing identity
- [var name: String](schema/attribute/name.md)
- [var originalName: String](schema/attribute/originalname.md)
### Determining behavior
- [var options: [Schema.Attribute.Option]](schema/attribute/options.md)
- [var isAttribute: Bool](schema/attribute/isattribute.md)
- [var isTransformable: Bool](schema/attribute/istransformable.md)
### Versioning
- [var hashModifier: String?](schema/attribute/hashmodifier.md)
### Encoding and decoding
- [func encode(to: any Encoder) throws](schema/attribute/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](schema/attribute/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Hashing
- [func hash(into: inout Hasher)](schema/attribute/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing attributes
- [static func == (Schema.Attribute, Schema.Attribute) -> Bool](schema/attribute/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Debugging
- [var debugDescription: String](schema/attribute/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
### Structures
- [Schema.Attribute.Option](schema/attribute/option.md)
### Instance Properties
- [var hashValue: Int](schema/attribute/hashvalue.md)
  The hash value.
- [var isOptional: Bool](schema/attribute/isoptional.md)
- [var isRelationship: Bool](schema/attribute/isrelationship.md)
- [var isTransient: Bool](schema/attribute/istransient.md)
- [var isUnique: Bool](schema/attribute/isunique.md)
### Default Implementations
- [Equatable Implementations](schema/attribute/equatable-implementations.md)

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

## See Also

- [Schema.CompositeAttribute](schema/compositeattribute.md)
  An object that describes an attribute that derives its value by composing other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/attribute)*