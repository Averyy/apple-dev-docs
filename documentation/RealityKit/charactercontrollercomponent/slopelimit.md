# slopeLimit

**Framework**: RealityKit  
**Kind**: property

The slope limit expressed as a limit angle in radians.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var slopeLimit: Float
```

#### Discussion

This value represents the maximum slope that the character can move over. RealityKit applies this value to characters that are walking on static objects, but not when walking on kinematic or dynamic objects.

Changing this value after the CharacterControllerComponent has been created and added to Entity has no effect.

## See Also

- [var height: Float](charactercontrollercomponent/height.md)
  The capsule height.
- [var radius: Float](charactercontrollercomponent/radius.md)
  The capsule radius.
- [var skinWidth: Float](charactercontrollercomponent/skinwidth.md)
  An added tolerance around the character capsule.
- [var stepLimit: Float](charactercontrollercomponent/steplimit.md)
  The maximum obstacle height that the controller can move over.
- [var upVector: SIMD3<Float>](charactercontrollercomponent/upvector.md)
  The y-axis direction relative to the physics origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/slopelimit)*