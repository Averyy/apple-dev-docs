# rotate(by:around:duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that rotates the node by an angle around a specified axis.

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
class func rotate(by angle: CGFloat, around axis: SCNVector3, duration: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`rotation`](scnnode/rotation.md) property animates to the new angle.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
[SCNAction rotateByAngle: -angle aroundAxis: axis duration: sec];
```

## Parameters

- `angle`: The amount to rotate the node counterclockwise around the specified axis, in radians.
- `axis`: A vector in the node’s local coordinate space whose direction specifies the axis of rotation.
- `duration`: The duration, in seconds, of the animation.

## See Also

- [class func rotateBy(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/rotateby(x:y:z:duration:).md)
  Creates an action that rotates the node in each of the three principal axes by angles relative to its current orientation.
- [class func rotateTo(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/rotateto(x:y:z:duration:).md)
  Creates an action that rotates the node to absolute angles in each of the three principal axes.
- [class func rotateTo(x: CGFloat, y: CGFloat, z: CGFloat, duration: TimeInterval, usesShortestUnitArc: Bool) -> SCNAction](scnaction/rotateto(x:y:z:duration:usesshortestunitarc:).md)
  Creates an action that rotates the node to absolute angles in each of the three principal axes.
- [class func rotate(toAxisAngle: SCNVector4, duration: TimeInterval) -> SCNAction](scnaction/rotate(toaxisangle:duration:).md)
  Creates an action that rotates the node to an absolute angle around a specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/rotate(by:around:duration:))*