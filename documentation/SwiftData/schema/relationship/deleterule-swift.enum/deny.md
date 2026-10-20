# Schema.Relationship.DeleteRule.deny

**Framework**: SwiftData  
**Kind**: case  
**Role**: Case

A rule that prevents the deletion of a model because it contains one or more references to other models.

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
case deny
```

## Mentions

- [Syncing model data across a person’s devices](../../../syncing-model-data-across-a-persons-devices.md)

## See Also

### Accessing delete rules
- [Schema.Relationship.DeleteRule.cascade](./cascade.md)
  A rule that deletes any related models.
- [Schema.Relationship.DeleteRule.noAction](./noaction.md)
  A rule that doesn’t make changes to any related models.
- [Schema.Relationship.DeleteRule.nullify](./nullify.md)
  A rule that nullifies the related model’s reference to the deleted model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum/deny)*