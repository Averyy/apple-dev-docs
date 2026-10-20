# Schema.Relationship.DeleteRule.nullify

**Framework**: SwiftData  
**Kind**: case  
**Role**: Case

A rule that nullifies the related model’s reference to the deleted model.

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
case nullify
```

## See Also

### Accessing delete rules
- [Schema.Relationship.DeleteRule.cascade](./cascade.md)
  A rule that deletes any related models.
- [Schema.Relationship.DeleteRule.deny](./deny.md)
  A rule that prevents the deletion of a model because it contains one or more references to other models.
- [Schema.Relationship.DeleteRule.noAction](./noaction.md)
  A rule that doesn’t make changes to any related models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum/nullify)*