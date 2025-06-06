# move(by:duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that moves a node relative to its current position.

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
class func move(by delta: SCNVector3, duration: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`position`](scnnode/position.md) property animates from its current position to its new position.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
SCNVector3 reverseDelta = SCNVector3Make(-delta.x, -delta.y, -delta.z);
[SCNAction moveBy: reverseDelta duration: duration];
```

## Parameters

- `delta`: A vector that describes the change to be applied to the node’s position.
- `duration`: The duration, in seconds, of the animation.

## See Also

- [class func moveBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/moveby(x:y:z:duration:).md)
  Creates an action that moves a node relative to its current position.
- [class func move(to: SCNVector3, duration: TimeInterval) -> SCNAction](scnaction/move(to:duration:).md)
  Creates an action that moves a node to a new position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/move(by:duration:))*