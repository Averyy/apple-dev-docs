# Schema.Relationship.DeleteRule.cascade

**Framework**: SwiftData  
**Kind**: case

A rule that deletes any related models.

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
case cascade
```

## See Also

- [Schema.Relationship.DeleteRule.deny](schema/relationship/deleterule-swift.enum/deny.md)
  A rule that prevents the deletion of a model because it contains one or more references to other models.
- [Schema.Relationship.DeleteRule.noAction](schema/relationship/deleterule-swift.enum/noaction.md)
  A rule that doesn’t make changes to any related models.
- [Schema.Relationship.DeleteRule.nullify](schema/relationship/deleterule-swift.enum/nullify.md)
  A rule that nullifies the related model’s reference to the deleted model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum/cascade)*