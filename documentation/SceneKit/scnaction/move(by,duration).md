# move(by:duration:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that moves a node relative to its current position.

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
class func move(by delta: SCNVector3, duration: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) moveBy:(SCNVector3) delta duration:(NSTimeInterval) duration;
```

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`position`](../scnnode/position.md) property animates from its current position to its new position.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
SCNVector3 reverseDelta = SCNVector3Make(-delta.x, -delta.y, -delta.z);
[SCNAction moveBy: reverseDelta duration: duration];
```

## Parameters

- `delta`: A vector that describes the change to be applied to the node’s position.
- `duration`: The duration, in seconds, of the animation.

## See Also

### Creating Actions That Move a Node
- [class func moveBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](./moveby%28x,y,z,duration%29.md)
  Creates an action that moves a node relative to its current position.
- [class func move(to: SCNVector3, duration: TimeInterval) -> SCNAction](./move%28to,duration%29.md)
  Creates an action that moves a node to a new position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/move(by:duration:))*