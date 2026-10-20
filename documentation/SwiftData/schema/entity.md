# Schema.Entity

**Framework**: SwiftData  
**Kind**: class  
**Role**: Class

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
- [init(String)](./entity/init%28_%29.md)
- [init(String, properties: any SchemaProperty...)](./entity/init%28_,properties%29.md)
- [init(String, subentities: Schema.Entity..., properties: any SchemaProperty...)](./entity/init%28_,subentities,properties%29.md)
### Assigning identity
- [var name: String](./entity/name.md)
### Managing attributes
- [var attributes: Set<Schema.Attribute>](./entity/attributes.md)
- [var attributesByName: [String : Schema.Attribute]](./entity/attributesbyname.md)
### Defining relationships
- [var relationships: Set<Schema.Relationship>](./entity/relationships.md)
- [var relationshipsByName: [String : Schema.Relationship]](./entity/relationshipsbyname.md)
### Managing properties
- [var properties: [any SchemaProperty]](./entity/properties.md)
- [var inheritedProperties: [any SchemaProperty]](./entity/inheritedproperties.md)
- [var inheritedPropertiesByName: [String : any SchemaProperty]](./entity/inheritedpropertiesbyname.md)
- [var storedProperties: [any SchemaProperty]](./entity/storedproperties.md)
- [var storedPropertiesByName: [String : any SchemaProperty]](./entity/storedpropertiesbyname.md)
### Applying constraints
- [var uniquenessConstraints: [[String]]](./entity/uniquenessconstraints.md)
### Configuring the inheritance chain
- [var superentity: Schema.Entity?](./entity/superentity.md)
- [var superentityName: String?](./entity/superentityname.md)
- [var subentities: Set<Schema.Entity>](./entity/subentities.md)
### Instance Properties
- [var indices: [[String]]](./entity/indices.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing entities
- [let entities: [Schema.Entity]](./entities.md)
- [let entitiesByName: [String : Schema.Entity]](./entitiesbyname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/entity)*