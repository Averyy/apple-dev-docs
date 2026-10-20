# SchemaProperty

**Framework**: SwiftData  
**Kind**: protocol  
**Role**: Protocol

An interface for describing a property.

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
protocol SchemaProperty : Decodable, Encodable, Hashable
```

## Topics

### Instance Properties
- [var isAttribute: Bool](./schemaproperty/isattribute.md)
- [var isOptional: Bool](./schemaproperty/isoptional.md)
- [var isRelationship: Bool](./schemaproperty/isrelationship.md)
- [var isTransient: Bool](./schemaproperty/istransient.md)
- [var isUnique: Bool](./schemaproperty/isunique.md)
- [var name: String](./schemaproperty/name.md)
- [var originalName: String](./schemaproperty/originalname.md)
- [var valueType: any Any.Type](./schemaproperty/valuetype.md)

## Relationships

### Inherits From
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
### Conforming Types
- [Schema.Attribute](./schema/attribute.md)
- [Schema.CompositeAttribute](./schema/compositeattribute.md)
- [Schema.Index](./schema/index.md)
- [Schema.Relationship](./schema/relationship.md)
- [Schema.Unique](./schema/unique.md)

## See Also

### Properties
- [protocol RelationshipCollection](./relationshipcollection.md)
  An interface for describing a collection of related models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schemaproperty)*