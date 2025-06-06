# Schema.Relationship

**Framework**: SwiftData  
**Kind**: class

An object that describes the configuration and behavior of a relationship between two model classes.

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
final class Relationship
```

## Topics

### Creating a relationship
- [init(Schema.Relationship.Option..., deleteRule: Schema.Relationship.DeleteRule, minimumModelCount: Int?, maximumModelCount: Int?, originalName: String?, inverse: AnyKeyPath?, hashModifier: String?)](schema/relationship/init(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:).md)
### Managing the configuration
- [var keypath: AnyKeyPath?](schema/relationship/keypath.md)
- [var destination: String](schema/relationship/destination.md)
- [var inverseName: String?](schema/relationship/inversename.md)
- [var inverseKeyPath: AnyKeyPath?](schema/relationship/inversekeypath.md)
- [var deleteRule: Schema.Relationship.DeleteRule](schema/relationship/deleterule-swift.property.md)
- [Schema.Relationship.DeleteRule](schema/relationship/deleterule-swift.enum.md)
  Describes the rule to apply when deleting a model containing references to other models.
- [var isToOneRelationship: Bool](schema/relationship/istoonerelationship.md)
### Specifying value information
- [var valueType: any Any.Type](schema/relationship/valuetype.md)
### Managing identity
- [var name: String](schema/relationship/name.md)
- [var originalName: String](schema/relationship/originalname.md)
### Determining behavior
- [var options: [Schema.Relationship.Option]](schema/relationship/options.md)
### Versioning
- [var hashModifier: String?](schema/relationship/hashmodifier.md)
### Encoding and decoding
- [func encode(to: any Encoder) throws](schema/relationship/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](schema/relationship/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Hashing
- [func hash(into: inout Hasher)](schema/relationship/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing attributes
- [static func == (Schema.Relationship, Schema.Relationship) -> Bool](schema/relationship/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Debugging
- [var debugDescription: String](schema/relationship/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
### Structures
- [Schema.Relationship.Option](schema/relationship/option.md)
### Instance Properties
- [var hashValue: Int](schema/relationship/hashvalue.md)
  The hash value.
- [var isAttribute: Bool](schema/relationship/isattribute.md)
- [var isTransient: Bool](schema/relationship/istransient.md)
- [var isUnique: Bool](schema/relationship/isunique.md)
- [var maximumModelCount: Int?](schema/relationship/maximummodelcount.md)
- [var minimumModelCount: Int?](schema/relationship/minimummodelcount.md)
### Default Implementations
- [Equatable Implementations](schema/relationship/equatable-implementations.md)
- [SchemaProperty Implementations](schema/relationship/schemaproperty-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [SchemaProperty](schemaproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship)*