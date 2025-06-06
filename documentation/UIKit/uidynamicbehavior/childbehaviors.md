# childBehaviors

**Framework**: UIKit  
**Kind**: property

Returns the array of dynamic behaviors that are children of a custom dynamic behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var childBehaviors: [UIDynamicBehavior] { get }
```

#### Discussion

Only custom subclasses of the class can have child behaviors.

## See Also

- [var action: (() -> Void)?](uidynamicbehavior/action.md)
  The block you want to execute during dynamic animation.
- [func addChildBehavior(UIDynamicBehavior)](uidynamicbehavior/addchildbehavior(_:).md)
  Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [func removeChildBehavior(UIDynamicBehavior)](uidynamicbehavior/removechildbehavior(_:).md)
  Removes a child dynamic behavior from a custom dynamic behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicbehavior/childbehaviors)*