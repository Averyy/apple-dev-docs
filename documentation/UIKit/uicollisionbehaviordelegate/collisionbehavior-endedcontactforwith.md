# collisionBehavior(_:endedContactFor:with:)

**Framework**: UIKit  
**Kind**: method

Called when a collision between two dynamic items has ended.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactFor item1: any UIDynamicItem, with item2: any UIDynamicItem)
```

## Parameters

- `behavior`: The collision behavior that owns the dynamic items that collided.
- `item1`: The first of the two dynamic items participating in the collision.
- `item2`: The second of the two dynamic items participating in the collision.

## See Also

- [func collisionBehavior(UICollisionBehavior, beganContactFor: any UIDynamicItem, withBoundaryIdentifier: (any NSCopying)?, at: CGPoint)](uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:withboundaryidentifier:at:).md)
  Called when a collision, between a dynamic item and a collision boundary, has begun.
- [func collisionBehavior(UICollisionBehavior, beganContactFor: any UIDynamicItem, with: any UIDynamicItem, at: CGPoint)](uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:with:at:).md)
  Called when a collision between two dynamic items has begun.
- [func collisionBehavior(UICollisionBehavior, endedContactFor: any UIDynamicItem, withBoundaryIdentifier: (any NSCopying)?)](uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:withboundaryidentifier:).md)
  Called when a collision between a dynamic item and a boundary has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:with:))*