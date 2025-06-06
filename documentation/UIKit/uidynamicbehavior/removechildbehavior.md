# removeChildBehavior(_:)

**Framework**: UIKit  
**Kind**: method

Removes a child dynamic behavior from a custom dynamic behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeChildBehavior(_ behavior: UIDynamicBehavior)
```

#### Discussion

This method applies only to custom subclasses of the [`UIDynamicBehavior`](uidynamicbehavior.md) class. UIKit concrete dynamic behaviors (such as an instance of [`UICollisionBehavior`](uicollisionbehavior.md)) cannot have child behaviors.

## Parameters

- `behavior`: The parent behavior ignores your use of this method if you:

## See Also

- [var action: (() -> Void)?](uidynamicbehavior/action.md)
  The block you want to execute during dynamic animation.
- [func addChildBehavior(UIDynamicBehavior)](uidynamicbehavior/addchildbehavior(_:).md)
  Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [var childBehaviors: [UIDynamicBehavior]](uidynamicbehavior/childbehaviors.md)
  Returns the array of dynamic behaviors that are children of a custom dynamic behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicbehavior/removechildbehavior(_:))*