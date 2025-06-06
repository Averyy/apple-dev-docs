# Schema.Relationship.DeleteRule.noAction

**Framework**: SwiftData  
**Kind**: case

A rule that doesn’t make changes to any related models.

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
case noAction
```

#### Discussion

Ensure that you take the appropriate action on any related models when using this delete rule, such as deleting them or nullifying their references to the deleted model. Otherwise, your data will be in an inconsistent state and may reference models that don’t exist.

## See Also

- [Schema.Relationship.DeleteRule.cascade](schema/relationship/deleterule-swift.enum/cascade.md)
  A rule that deletes any related models.
- [Schema.Relationship.DeleteRule.deny](schema/relationship/deleterule-swift.enum/deny.md)
  A rule that prevents the deletion of a model because it contains one or more references to other models.
- [Schema.Relationship.DeleteRule.nullify](schema/relationship/deleterule-swift.enum/nullify.md)
  A rule that nullifies the related model’s reference to the deleted model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum/noaction)*