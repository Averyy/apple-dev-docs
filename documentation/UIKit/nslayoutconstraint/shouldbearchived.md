# shouldBeArchived

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the constraint should be archived by its owning view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shouldBeArchived: Bool { get set }
```

#### Discussion

When a view is archived, it archives some but not all constraints in its [`constraints`](uiview/constraints.md) array. The value of [`shouldBeArchived`](nslayoutconstraint/shouldbearchived.md) informs the view if a particular constraint should be archived by the view.

If a constraint is created at runtime in response to the state of the object, it isn’t appropriate to archive the constraint. Instead you archive the state that gives rise to the constraint. The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutconstraint/shouldbearchived)*