# rotateTo(x:y:z:duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that rotates the node to absolute angles in each of the three principal axes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func rotateTo(x xAngle: CGFloat, y yAngle: CGFloat, z zAngle: CGFloat, duration: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`rotation`](scnnode/rotation.md) property animates to the new angle. Calling this method is equivalent to calling [`rotateTo(x:y:z:duration:usesShortestUnitArc:)`](scnaction/rotateto(x:y:z:duration:usesshortestunitarc:).md) and passing [`false`](https://developer.apple.com/documentation/Swift/false) for the `shortestUnitArc` parameter.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `xAngle`: The amount to rotate the node counterclockwise around the x-axis of its local coordinate space, in radians.
- `yAngle`: The amount to rotate the node counterclockwise around the y-axis of its local coordinate space, in radians.
- `zAngle`: The amount to rotate the node counterclockwise around the z-axis of its local coordinate space, in radians.
- `duration`: The duration, in seconds, of the animation.

## See Also

- [class func rotateBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/rotateby(x:y:z:duration:).md)
  Creates an action that rotates the node in each of the three principal axes by angles relative to its current orientation.
- [class func rotateTo(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval, usesShortestUnitArc: Bool) -> SCNAction](scnaction/rotateto(x:y:z:duration:usesshortestunitarc:).md)
  Creates an action that rotates the node to absolute angles in each of the three principal axes.
- [class func rotate(by: CGFloat, around: SCNVector3, duration: TimeInterval) -> SCNAction](scnaction/rotate(by:around:duration:).md)
  Creates an action that rotates the node by an angle around a specified axis.
- [class func rotate(toAxisAngle: SCNVector4, duration: TimeInterval) -> SCNAction](scnaction/rotate(toaxisangle:duration:).md)
  Creates an action that rotates the node to an absolute angle around a specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/rotateto(x:y:z:duration:))*