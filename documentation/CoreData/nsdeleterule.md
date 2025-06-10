# NSDeleteRule

**Framework**: Core Data  
**Kind**: enum

Constants that determine what happens when you delete a relationship’s owning managed object.

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
enum NSDeleteRule
```

## Topics

### Delete Rules
- [NSDeleteRule.noActionDeleteRule](nsdeleterule/noactiondeleterule.md)
  A rule that prevents modification of the referenced managed objects.
- [NSDeleteRule.nullifyDeleteRule](nsdeleterule/nullifydeleterule.md)
  A rule that nullifies the inverse relationship of the referenced managed objects.
- [NSDeleteRule.cascadeDeleteRule](nsdeleterule/cascadedeleterule.md)
  A rule that deletes the referenced managed objects.
- [NSDeleteRule.denyDeleteRule](nsdeleterule/denydeleterule.md)
  A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.
### Initializers
- [init?(rawValue: UInt)](nsdeleterule/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var deleteRule: NSDeleteRule](nsrelationshipdescription/deleterule.md)
  The rule to apply when you delete the relationship’s owning managed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsdeleterule)*