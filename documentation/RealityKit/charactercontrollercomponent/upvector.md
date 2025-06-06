# upVector

**Framework**: RealityKit  
**Kind**: property

The y-axis direction relative to the physics origin.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var upVector: SIMD3<Float>
```

#### Discussion

Rotates the object so that the vertical height is along the up vector. Normalize and specify the vector in , the coordinate system of the physics simulation.

## See Also

- [var height: Float](charactercontrollercomponent/height.md)
  The capsule height.
- [var radius: Float](charactercontrollercomponent/radius.md)
  The capsule radius.
- [var skinWidth: Float](charactercontrollercomponent/skinwidth.md)
  An added tolerance around the character capsule.
- [var slopeLimit: Float](charactercontrollercomponent/slopelimit.md)
  The slope limit expressed as a limit angle in radians.
- [var stepLimit: Float](charactercontrollercomponent/steplimit.md)
  The maximum obstacle height that the controller can move over.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/upvector)*