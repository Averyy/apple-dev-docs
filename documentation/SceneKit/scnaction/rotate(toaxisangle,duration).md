# rotate(toAxisAngle:duration:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that rotates the node to an absolute angle around a specified axis.

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
class func rotate(toAxisAngle axisAngle: SCNVector4, duration: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) rotateToAxisAngle:(SCNVector4) axisAngle duration:(NSTimeInterval) duration;
```

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`rotation`](../scnnode/rotation.md) property animates to the new angle.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `axisAngle`: A four-component vector whose first three components are a vector in the node’s local coordinate space specifying an axis and whose fourth component is the amount to rotate the node counterclockwise around that axis, in radians.
- `duration`: The duration, in seconds, of the animation.

## See Also

### Creating Actions That Rotate a Node
- [class func rotateBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](./rotateby%28x,y,z,duration%29.md)
  Creates an action that rotates the node in each of the three principal axes by angles relative to its current orientation.
- [class func rotateTo(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](./rotateto%28x,y,z,duration%29.md)
  Creates an action that rotates the node to absolute angles in each of the three principal axes.
- [class func rotateTo(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval, usesShortestUnitArc: Bool) -> SCNAction](./rotateto%28x,y,z,duration,usesshortestunitarc%29.md)
  Creates an action that rotates the node to absolute angles in each of the three principal axes.
- [class func rotate(by: CGFloat, around: SCNVector3, duration: TimeInterval) -> SCNAction](./rotate%28by,around,duration%29.md)
  Creates an action that rotates the node by an angle around a specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/rotate(toaxisangle:duration:))*