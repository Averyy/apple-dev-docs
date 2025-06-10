# collisionBehavior(_:endedContactFor:withBoundaryIdentifier:)

**Framework**: UIKit  
**Kind**: method

Called when a collision between a dynamic item and a boundary has ended.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactFor item: any UIDynamicItem, withBoundaryIdentifier identifier: (any NSCopying)?)
```

## Parameters

- `behavior`: The collision behavior that owns the dynamic item that has ended contact.
- `item`: The dynamic item that collided.
- `identifier`: The identifier of the boundary that the dynamic item collided with.

## See Also

- [func collisionBehavior(UICollisionBehavior, beganContactFor: any UIDynamicItem, withBoundaryIdentifier: (any NSCopying)?, at: CGPoint)](uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:withboundaryidentifier:at:).md)
  Called when a collision, between a dynamic item and a collision boundary, has begun.
- [func collisionBehavior(UICollisionBehavior, beganContactFor: any UIDynamicItem, with: any UIDynamicItem, at: CGPoint)](uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:with:at:).md)
  Called when a collision between two dynamic items has begun.
- [func collisionBehavior(UICollisionBehavior, endedContactFor: any UIDynamicItem, with: any UIDynamicItem)](uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:with:).md)
  Called when a collision between two dynamic items has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:withboundaryidentifier:))*