# Schema.Relationship

**Framework**: SwiftData  
**Kind**: class  
**Role**: Class

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
- [init(Schema.Relationship.Option..., deleteRule: Schema.Relationship.DeleteRule, minimumModelCount: Int?, maximumModelCount: Int?, originalName: String?, inverse: AnyKeyPath?, hashModifier: String?)](./relationship/init%28_,deleterule,minimummodelcount,maximummodelcount,originalname,inverse,hashmodifier%29.md)
### Managing the configuration
- [var keypath: AnyKeyPath?](./relationship/keypath.md)
- [var destination: String](./relationship/destination.md)
- [var inverseName: String?](./relationship/inversename.md)
- [var inverseKeyPath: AnyKeyPath?](./relationship/inversekeypath.md)
- [var deleteRule: Schema.Relationship.DeleteRule](./relationship/deleterule-swift.property.md)
- [Schema.Relationship.DeleteRule](./relationship/deleterule-swift.enum.md)
  Describes the rule to apply when deleting a model containing references to other models.
- [var isToOneRelationship: Bool](./relationship/istoonerelationship.md)
### Determining behavior
- [var options: [Schema.Relationship.Option]](./relationship/options.md)
### Versioning
- [var hashModifier: String?](./relationship/hashmodifier.md)
### Structures
- [Schema.Relationship.Option](./relationship/option.md)
### Instance Properties
- [var maximumModelCount: Int?](./relationship/maximummodelcount.md)
- [var minimumModelCount: Int?](./relationship/minimummodelcount.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [SchemaProperty](../schemaproperty.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship)*