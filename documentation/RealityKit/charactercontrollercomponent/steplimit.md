# stepLimit

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The maximum obstacle height that the controller can move over.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var stepLimit: Float
```

#### Discussion

Specify this value relative to the entity’s coordinate system.

Changing this value after the CharacterControllerComponent has been created and added to Entity has no effect.

## See Also

### Configuring a character
- [var height: Float](./height.md)
  The capsule height.
- [var radius: Float](./radius.md)
  The capsule radius.
- [var skinWidth: Float](./skinwidth.md)
  An added tolerance around the character capsule.
- [var slopeLimit: Float](./slopelimit.md)
  The slope limit expressed as a limit angle in radians.
- [var upVector: SIMD3<Float>](./upvector.md)
  The y-axis direction relative to the physics origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/steplimit)*