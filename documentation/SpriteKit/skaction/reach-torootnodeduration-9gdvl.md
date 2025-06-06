# reach(to:rootNode:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that performs an inverse kinematic reach.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func reach(to position: CGPoint, rootNode root: SKNode, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

This action is typically used to implement character animation across a series of moving parts. When the action executes, it performs an inverse kinematic calculation to determine new rotation values for the target node and any of its ancestors up to and including the root node. Each node is rotated around its anchor point in an attempt to get the targeted node’s position closer to the intended destination. Each node’s rotation value is constrained by that node’s [`reachConstraints`](sknode/reachconstraints.md) property. If the action cannot successfully reach the target position, it gets the node as close as it can to the target position.

This action is not reversible; the reverse of this action is the same action.

## Parameters

- `position`: The intended destination for the node, specified in the scene’s coordinate system.
- `root`: The highest level ancestor of the target node that should be rotated.
- `duration`: The length of the animation.

## See Also

- [Working with Inverse Kinematics](working-with-inverse-kinematics.md)
  Gain fine-tuned control of objects that are connected by joints.
- [class func reach(to: CGPoint, rootNode: SKNode, velocity: CGFloat) -> SKAction](skaction/reach(to:rootnode:velocity:)-8xv45.md)
  Creates an action that performs an inverse kinematic reach.
- [class func reach(to: SKNode, rootNode: SKNode, duration: TimeInterval) -> SKAction](skaction/reach(to:rootnode:duration:)-1db76.md)
  Creates an action that performs an inverse kinematic reach.
- [class func reach(to: SKNode, rootNode: SKNode, velocity: CGFloat) -> SKAction](skaction/reach(to:rootnode:velocity:)-7gbvx.md)
  Creates an action that performs an inverse kinematic reach.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/reach(to:rootnode:duration:)-9gdvl)*