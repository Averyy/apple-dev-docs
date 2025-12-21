# skinWidth

**Framework**: RealityKit  
**Kind**: property

An added tolerance around the character capsule.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var skinWidth: Float
```

#### Discussion

A small skin, known as the , is maintained around the controller’s volume to avoid rounding and precision issues with collision detection. Specify this value relative to the entity’s coordinate system.

## See Also

- [var height: Float](charactercontrollercomponent/height.md)
  The capsule height.
- [var radius: Float](charactercontrollercomponent/radius.md)
  The capsule radius.
- [var slopeLimit: Float](charactercontrollercomponent/slopelimit.md)
  The slope limit expressed as a limit angle in radians.
- [var stepLimit: Float](charactercontrollercomponent/steplimit.md)
  The maximum obstacle height that the controller can move over.
- [var upVector: SIMD3<Float>](charactercontrollercomponent/upvector.md)
  The y-axis direction relative to the physics origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/skinwidth)*