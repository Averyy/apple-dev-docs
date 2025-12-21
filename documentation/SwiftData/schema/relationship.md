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
### Determining behavior
- [var options: [Schema.Relationship.Option]](schema/relationship/options.md)
### Versioning
- [var hashModifier: String?](schema/relationship/hashmodifier.md)
### Structures
- [Schema.Relationship.Option](schema/relationship/option.md)
### Instance Properties
- [var maximumModelCount: Int?](schema/relationship/maximummodelcount.md)
- [var minimumModelCount: Int?](schema/relationship/minimummodelcount.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [SchemaProperty](schemaproperty.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship)*