# moveBy(x:y:z:duration:)

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
class func moveBy(x deltaX: CGFloat, y deltaY: CGFloat, z deltaZ: CGFloat, duration: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) moveByX:(CGFloat) deltaX y:(CGFloat) deltaY z:(CGFloat) deltaZ duration:(NSTimeInterval) duration;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`position`](../scnnode/position.md) property animates from its current position to its new position.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
[SCNAction moveByX: -deltaX y: -deltaY z: -deltaZ duration: duration];
```

## Parameters

- `deltaX`: The distance to move the node in the X direction of its parent node’s local coordinate space.
- `deltaY`: The distance to move the node in the Y direction of its parent node’s local coordinate space.
- `deltaZ`: The distance to move the node in the Z direction of its parent node’s local coordinate space.
- `duration`: The duration, in seconds, of the animation.

## See Also

### Creating Actions That Move a Node
- [class func move(by: SCNVector3, duration: TimeInterval) -> SCNAction](./move%28by,duration%29.md)
  Creates an action that moves a node relative to its current position.
- [class func move(to: SCNVector3, duration: TimeInterval) -> SCNAction](./move%28to,duration%29.md)
  Creates an action that moves a node to a new position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/moveby(x:y:z:duration:))*