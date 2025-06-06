# collisionDelegate

**Framework**: UIKit  
**Kind**: property

The delegate object that you want to respond to collisions for the collision behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var collisionDelegate: (any UICollisionBehaviorDelegate)? { get set }
```

## See Also

- [protocol UICollisionBehaviorDelegate](uicollisionbehaviordelegate.md)
  To respond to UIKit dynamic item collisions, configure a custom class to adopt the [`UICollisionBehaviorDelegate`](uicollisionbehaviordelegate.md) protocol. Then, in a collision behavior (an instance of the [`UICollisionBehavior`](uicollisionbehavior.md) class), set the delegate to be an instance of your custom class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehavior/collisiondelegate)*