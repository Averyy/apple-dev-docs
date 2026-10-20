# Schema.Relationship.DeleteRule

**Framework**: SwiftData  
**Kind**: enum  
**Role**: Enumeration

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

- [Preserving your app’s model data across launches](../../preserving-your-apps-model-data-across-launches.md)

## Topics

### Accessing delete rules
- [Schema.Relationship.DeleteRule.cascade](./deleterule-swift.enum/cascade.md)
  A rule that deletes any related models.
- [Schema.Relationship.DeleteRule.deny](./deleterule-swift.enum/deny.md)
  A rule that prevents the deletion of a model because it contains one or more references to other models.
- [Schema.Relationship.DeleteRule.noAction](./deleterule-swift.enum/noaction.md)
  A rule that doesn’t make changes to any related models.
- [Schema.Relationship.DeleteRule.nullify](./deleterule-swift.enum/nullify.md)
  A rule that nullifies the related model’s reference to the deleted model.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)

## See Also

### Managing the configuration
- [var keypath: AnyKeyPath?](./keypath.md)
- [var destination: String](./destination.md)
- [var inverseName: String?](./inversename.md)
- [var inverseKeyPath: AnyKeyPath?](./inversekeypath.md)
- [var deleteRule: Schema.Relationship.DeleteRule](./deleterule-swift.property.md)
- [var isToOneRelationship: Bool](./istoonerelationship.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum)*