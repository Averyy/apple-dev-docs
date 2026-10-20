# rotateTo(x:y:z:duration:usesShortestUnitArc:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that rotates the node to absolute angles in each of the three principal axes.

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
class func rotateTo(x xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration: TimeInterval, usesShortestUnitArc shortestUnitArc: Bool) -> SCNAction
```

```objc
+ (SCNAction *) rotateToX:(CGFloat) xAngle y:(CGFloat) yAngle z:(CGFloat) zAngle duration:(NSTimeInterval) duration shortestUnitArc:(BOOL) shortestUnitArc;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`rotation`](../scnnode/rotation.md) property animates to the new angle.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `xAngle`: The amount to rotate the node counterclockwise around the x-axis of its local coordinate space, in radians.
- `yAngle`: The amount to rotate the node counterclockwise around the y-axis of its local coordinate space, in radians.
- `zAngle`: The amount to rotate the node counterclockwise around the z-axis of its local coordinate space, in radians.
- `duration`: The duration, in seconds, of the animation.
- `shortestUnitArc`: If [`false`](../../Swift/false.md) (the default), the animation interpolates each component of the node’s rotation between its current value and the new value. If [`true`](../../Swift/true.md), the animation makes the most direct rotation possible from the node’s current orientation to the new orientation.

## See Also

### Creating Actions That Rotate a Node
- [class func rotateBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](./rotateby%28x,y,z,duration%29.md)
  Creates an action that rotates the node in each of the three principal axes by angles relative to its current orientation.
- [class func rotateTo(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](./rotateto%28x,y,z,duration%29.md)
  Creates an action that rotates the node to absolute angles in each of the three principal axes.
- [class func rotate(by: CGFloat, around: SCNVector3, duration: TimeInterval) -> SCNAction](./rotate%28by,around,duration%29.md)
  Creates an action that rotates the node by an angle around a specified axis.
- [class func rotate(toAxisAngle: SCNVector4, duration: TimeInterval) -> SCNAction](./rotate%28toaxisangle,duration%29.md)
  Creates an action that rotates the node to an absolute angle around a specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/rotateto(x:y:z:duration:usesshortestunitarc:))*