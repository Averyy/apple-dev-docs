# NSDeleteRule.nullifyDeleteRule

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

A rule that nullifies the inverse relationship of the referenced managed objects.

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
case nullifyDeleteRule
```

```c
NSNullifyDeleteRule
```

## See Also

### Delete Rules
- [NSDeleteRule.noActionDeleteRule](./noactiondeleterule.md)
  A rule that prevents modification of the referenced managed objects.
- [NSDeleteRule.cascadeDeleteRule](./cascadedeleterule.md)
  A rule that deletes the referenced managed objects.
- [NSDeleteRule.denyDeleteRule](./denydeleterule.md)
  A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsdeleterule/nullifydeleterule)*