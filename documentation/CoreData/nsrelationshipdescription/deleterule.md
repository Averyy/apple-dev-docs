# deleteRule

**Framework**: Core Data  
**Kind**: property

The rule to apply when you delete the relationship’s owning managed object.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var deleteRule: NSDeleteRule { get set }
```

#### Discussion

The default value is [`NSDeleteRule.nullifyDeleteRule`](nsdeleterule/nullifydeleterule.md). For possible values, see [`NSDeleteRule`](nsdeleterule.md).

## See Also

- [enum NSDeleteRule](nsdeleterule.md)
  Constants that determine what happens when you delete a relationship’s owning managed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/deleterule)*