# skinWidth

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

An added tolerance around the character capsule.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var skinWidth: Float
```

## Discussion

A small skin, known as the *contact offset*, is maintained around the controller’s volume to avoid rounding and precision issues with collision detection. Specify this value relative to the entity’s coordinate system.

## See Also

### Configuring a character
- [var height: Float](./height.md)
  The capsule height.
- [var radius: Float](./radius.md)
  The capsule radius.
- [var slopeLimit: Float](./slopelimit.md)
  The slope limit expressed as a limit angle in radians.
- [var stepLimit: Float](./steplimit.md)
  The maximum obstacle height that the controller can move over.
- [var upVector: SIMD3<Float>](./upvector.md)
  The y-axis direction relative to the physics origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/skinwidth)*