# Schema.Relationship.DeleteRule

**Framework**: SwiftData  
**Kind**: enum

Describes the rule to apply when deleting a model containing references to other models.

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
enum DeleteRule
```

## Mentions

- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)

## Topics

### Accessing delete rules
- [Schema.Relationship.DeleteRule.cascade](schema/relationship/deleterule-swift.enum/cascade.md)
  A rule that deletes any related models.
- [Schema.Relationship.DeleteRule.deny](schema/relationship/deleterule-swift.enum/deny.md)
  A rule that prevents the deletion of a model because it contains one or more references to other models.
- [Schema.Relationship.DeleteRule.noAction](schema/relationship/deleterule-swift.enum/noaction.md)
  A rule that doesn’t make changes to any related models.
- [Schema.Relationship.DeleteRule.nullify](schema/relationship/deleterule-swift.enum/nullify.md)
  A rule that nullifies the related model’s reference to the deleted model.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var keypath: AnyKeyPath?](schema/relationship/keypath.md)
- [var destination: String](schema/relationship/destination.md)
- [var inverseName: String?](schema/relationship/inversename.md)
- [var inverseKeyPath: AnyKeyPath?](schema/relationship/inversekeypath.md)
- [var deleteRule: Schema.Relationship.DeleteRule](schema/relationship/deleterule-swift.property.md)
- [var isToOneRelationship: Bool](schema/relationship/istoonerelationship.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum)*