# move(to:duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that moves a node to a new position.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func move(to location: SCNVector3, duration: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`position`](scnnode/position.md) property animates from its current position to its new position.

This action is not reversible; the reverse of this action has the same duration but does not move the node.

## Parameters

- `location`: The coordinates for the node’s new position in its parent node’s local coordinate space.
- `duration`: The duration, in seconds, of the animation.

## See Also

- [class func moveBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/moveby(x:y:z:duration:).md)
  Creates an action that moves a node relative to its current position.
- [class func move(by: SCNVector3, duration: TimeInterval) -> SCNAction](scnaction/move(by:duration:).md)
  Creates an action that moves a node relative to its current position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/move(to:duration:))*