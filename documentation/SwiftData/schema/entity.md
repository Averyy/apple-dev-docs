# Schema.Entity

**Framework**: SwiftData  
**Kind**: class

An object that provides a blueprint for the associated model class.

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
final class Entity
```

## Topics

### Creating an entity
- [init(String)](schema/entity/init(_:).md)
- [init(String, properties: any SchemaProperty...)](schema/entity/init(_:properties:).md)
- [init(String, subentities: Schema.Entity..., properties: any SchemaProperty...)](schema/entity/init(_:subentities:properties:).md)
### Assigning identity
- [var name: String](schema/entity/name.md)
### Managing attributes
- [var attributes: Set<Schema.Attribute>](schema/entity/attributes.md)
- [var attributesByName: [String : Schema.Attribute]](schema/entity/attributesbyname.md)
### Defining relationships
- [var relationships: Set<Schema.Relationship>](schema/entity/relationships.md)
- [var relationshipsByName: [String : Schema.Relationship]](schema/entity/relationshipsbyname.md)
### Managing properties
- [var properties: [any SchemaProperty]](schema/entity/properties.md)
- [var inheritedProperties: [any SchemaProperty]](schema/entity/inheritedproperties.md)
- [var inheritedPropertiesByName: [String : any SchemaProperty]](schema/entity/inheritedpropertiesbyname.md)
- [var storedProperties: [any SchemaProperty]](schema/entity/storedproperties.md)
- [var storedPropertiesByName: [String : any SchemaProperty]](schema/entity/storedpropertiesbyname.md)
### Applying constraints
- [var uniquenessConstraints: [[String]]](schema/entity/uniquenessconstraints.md)
### Configuring the inheritance chain
- [var superentity: Schema.Entity?](schema/entity/superentity.md)
- [var superentityName: String?](schema/entity/superentityname.md)
- [var subentities: Set<Schema.Entity>](schema/entity/subentities.md)
### Encoding and decoding
- [func encode(to: any Encoder) throws](schema/entity/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](schema/entity/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Hashing
- [func hash(into: inout Hasher)](schema/entity/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing entities
- [static func == (Schema.Entity, Schema.Entity) -> Bool](schema/entity/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var debugDescription: String](schema/entity/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
- [var hashValue: Int](schema/entity/hashvalue.md)
  The hash value.
- [var indices: [[String]]](schema/entity/indices.md)
### Default Implementations
- [Equatable Implementations](schema/entity/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [let entities: [Schema.Entity]](schema/entities.md)
- [let entitiesByName: [String : Schema.Entity]](schema/entitiesbyname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/entity)*