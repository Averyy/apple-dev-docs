# frames

**Framework**: RealityKit  
**Kind**: property

An array of floating-point values in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var frames: [Float] { get set }
```

#### Discussion

This array contains sequential values for the animated property when [`bindTarget`](animationdefinition/bindtarget.md) is an array of `Float` values.

## See Also

- [var frames: [JointTransforms]](sampledanimation/frames-4eeex.md)
  An array of joint transforms in which each element represents a discrete state of the target entity at a given point in the animation’s timeline.
- [var frames: [Transform]](sampledanimation/frames-4qotl.md)
  An array of transforms in which each element represents a discrete state of the target entity at a given point in the animation’s timeline.
- [var frames: [Double]](sampledanimation/frames-2hobp.md)
  An array of double-precision values in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [simd_quatf]](sampledanimation/frames-2h6tu.md)
  An array of quaternions in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [SIMD2<Float>]](sampledanimation/frames-9luwf.md)
  An array of floating-point pairs in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [SIMD3<Float>]](sampledanimation/frames-1zxo.md)
  An array of floating-point triplets in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [SIMD4<Float>]](sampledanimation/frames-2ywfx.md)
  An array of floating-point quadruples in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/frames-2j4nj)*