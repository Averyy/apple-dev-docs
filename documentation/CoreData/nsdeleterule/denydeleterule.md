# NSDeleteRule.denyDeleteRule

**Framework**: Core Data  
**Kind**: case

A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.

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
case denyDeleteRule
```

## See Also

- [NSDeleteRule.noActionDeleteRule](nsdeleterule/noactiondeleterule.md)
  A rule that prevents modification of the referenced managed objects.
- [NSDeleteRule.nullifyDeleteRule](nsdeleterule/nullifydeleterule.md)
  A rule that nullifies the inverse relationship of the referenced managed objects.
- [NSDeleteRule.cascadeDeleteRule](nsdeleterule/cascadedeleterule.md)
  A rule that deletes the referenced managed objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsdeleterule/denydeleterule)*