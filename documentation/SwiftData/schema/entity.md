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
### Instance Properties
- [var indices: [[String]]](schema/entity/indices.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let entities: [Schema.Entity]](schema/entities.md)
- [let entitiesByName: [String : Schema.Entity]](schema/entitiesbyname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/entity)*