# NSDeleteRule.cascadeDeleteRule

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

A rule that deletes the referenced managed objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case cascadeDeleteRule
```

```c
NSCascadeDeleteRule
```

## See Also

### Delete Rules
- [NSDeleteRule.noActionDeleteRule](./noactiondeleterule.md)
  A rule that prevents modification of the referenced managed objects.
- [NSDeleteRule.nullifyDeleteRule](./nullifydeleterule.md)
  A rule that nullifies the inverse relationship of the referenced managed objects.
- [NSDeleteRule.denyDeleteRule](./denydeleterule.md)
  A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsdeleterule/cascadedeleterule)*