# move(to:duration:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that moves a node to a new position.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class func move(to location: SCNVector3, duration: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) moveTo:(SCNVector3) location duration:(NSTimeInterval) duration;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`position`](../scnnode/position.md) property animates from its current position to its new position.

This action is not reversible; the reverse of this action has the same duration but does not move the node.

## Parameters

- `location`: The coordinates for the node’s new position in its parent node’s local coordinate space.
- `duration`: The duration, in seconds, of the animation.

## See Also

### Creating Actions That Move a Node
- [class func moveBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](./moveby%28x,y,z,duration%29.md)
  Creates an action that moves a node relative to its current position.
- [class func move(by: SCNVector3, duration: TimeInterval) -> SCNAction](./move%28by,duration%29.md)
  Creates an action that moves a node relative to its current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/move(to:duration:))*