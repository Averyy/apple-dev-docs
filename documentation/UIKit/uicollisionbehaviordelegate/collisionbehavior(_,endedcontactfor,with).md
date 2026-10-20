# collisionBehavior(_:endedContactFor:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when a collision between two dynamic items has ended.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactFor item1: any UIDynamicItem, with item2: any UIDynamicItem)
```

```objc
- (void) collisionBehavior:(UICollisionBehavior *) behavior endedContactForItem:(id<UIDynamicItem>) item1 withItem:(id<UIDynamicItem>) item2;
```

## Parameters

- `behavior`: The collision behavior that owns the dynamic items that collided.
- `item1`: The first of the two dynamic items participating in the collision.
- `item2`: The second of the two dynamic items participating in the collision.

## See Also

### Responding to UIKit Dynamics collisions
- [func collisionBehavior(UICollisionBehavior, beganContactFor: any UIDynamicItem, withBoundaryIdentifier: (any NSCopying)?, at: CGPoint)](./collisionbehavior%28_,begancontactfor,withboundaryidentifier,at%29.md)
  Called when a collision, between a dynamic item and a collision boundary, has begun.
- [func collisionBehavior(UICollisionBehavior, beganContactFor: any UIDynamicItem, with: any UIDynamicItem, at: CGPoint)](./collisionbehavior%28_,begancontactfor,with,at%29.md)
  Called when a collision between two dynamic items has begun.
- [func collisionBehavior(UICollisionBehavior, endedContactFor: any UIDynamicItem, withBoundaryIdentifier: (any NSCopying)?)](./collisionbehavior%28_,endedcontactfor,withboundaryidentifier%29.md)
  Called when a collision between a dynamic item and a boundary has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:with:))*