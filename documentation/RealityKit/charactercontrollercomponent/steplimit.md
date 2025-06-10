# stepLimit

**Framework**: RealityKit  
**Kind**: property

The maximum obstacle height that the controller can move over.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var stepLimit: Float
```

#### Discussion

Specify this value relative to the entity’s coordinate system.

Changing this value after the CharacterControllerComponent has been created and added to Entity has no effect.

## See Also

- [var height: Float](charactercontrollercomponent/height.md)
  The capsule height.
- [var radius: Float](charactercontrollercomponent/radius.md)
  The capsule radius.
- [var skinWidth: Float](charactercontrollercomponent/skinwidth.md)
  An added tolerance around the character capsule.
- [var slopeLimit: Float](charactercontrollercomponent/slopelimit.md)
  The slope limit expressed as a limit angle in radians.
- [var upVector: SIMD3<Float>](charactercontrollercomponent/upvector.md)
  The y-axis direction relative to the physics origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/steplimit)*