# removeChildBehavior(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes a child dynamic behavior from a custom dynamic behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func removeChildBehavior(_ behavior: UIDynamicBehavior)
```

```objc
- (void) removeChildBehavior:(UIDynamicBehavior *) behavior;
```

#### Discussion

This method applies only to custom subclasses of the [`UIDynamicBehavior`](../uidynamicbehavior.md) class. UIKit concrete dynamic behaviors (such as an instance of [`UICollisionBehavior`](../uicollisionbehavior.md)) cannot have child behaviors.

## Parameters

- `behavior`: The child dynamic behavior you want to remove.

  The parent behavior ignores your use of this method if you:

  - Provide a `nil` value
  - Provide a behavior instance that is not a child of the parent behavior

## See Also

### Configuring a dynamic behavior
- [var action: (() -> Void)?](./action.md)
  The block you want to execute during dynamic animation.
- [func addChildBehavior(UIDynamicBehavior)](./addchildbehavior%28_%29.md)
  Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [var childBehaviors: [UIDynamicBehavior]](./childbehaviors.md)
  Returns the array of dynamic behaviors that are children of a custom dynamic behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicbehavior/removechildbehavior(_:))*