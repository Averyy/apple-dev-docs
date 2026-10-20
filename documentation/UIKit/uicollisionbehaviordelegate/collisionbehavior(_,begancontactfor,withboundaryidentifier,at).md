# collisionBehavior(_:beganContactFor:withBoundaryIdentifier:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when a collision, between a dynamic item and a collision boundary, has begun.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func collisionBehavior(_ behavior: UICollisionBehavior, beganContactFor item: any UIDynamicItem, withBoundaryIdentifier identifier: (any NSCopying)?, at p: CGPoint)
```

```objc
- (void) collisionBehavior:(UICollisionBehavior *) behavior beganContactForItem:(id<UIDynamicItem>) item withBoundaryIdentifier:(id<NSCopying>) identifier atPoint:(CGPoint) p;
```

## Parameters

- `behavior`: The collision behavior that owns the dynamic item that has started contact with a boundary.
- `item`: The dynamic item that has started contact with a boundary.
- `identifier`: The identifier of the boundary that the dynamic item has started contact with.
- `p`: The collision point on the boundary.

## See Also

### Responding to UIKit Dynamics collisions
- [func collisionBehavior(UICollisionBehavior, beganContactFor: any UIDynamicItem, with: any UIDynamicItem, at: CGPoint)](./collisionbehavior%28_,begancontactfor,with,at%29.md)
  Called when a collision between two dynamic items has begun.
- [func collisionBehavior(UICollisionBehavior, endedContactFor: any UIDynamicItem, withBoundaryIdentifier: (any NSCopying)?)](./collisionbehavior%28_,endedcontactfor,withboundaryidentifier%29.md)
  Called when a collision between a dynamic item and a boundary has ended.
- [func collisionBehavior(UICollisionBehavior, endedContactFor: any UIDynamicItem, with: any UIDynamicItem)](./collisionbehavior%28_,endedcontactfor,with%29.md)
  Called when a collision between two dynamic items has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:withboundaryidentifier:at:))*