# NSDeleteRule.noActionDeleteRule

**Framework**: Core Data  
**Kind**: case

A rule that prevents modification of the referenced managed objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case noActionDeleteRule
```

#### Discussion

If you use this delete rule, make sure you delete any referenced managed objects or nullify their inverse relationships. Otherwise, those objects will reference an object that doesn’t exist, and your persistent store will be in an inconsistent state.

## See Also

- [NSDeleteRule.nullifyDeleteRule](nsdeleterule/nullifydeleterule.md)
  A rule that nullifies the inverse relationship of the referenced managed objects.
- [NSDeleteRule.cascadeDeleteRule](nsdeleterule/cascadedeleterule.md)
  A rule that deletes the referenced managed objects.
- [NSDeleteRule.denyDeleteRule](nsdeleterule/denydeleterule.md)
  A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsdeleterule/noactiondeleterule)*