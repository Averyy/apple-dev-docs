# frames

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

An array of double-precision values in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var frames: [Double] { get set }
```

Available when `Value` is `Double`.

## Discussion

This array contains sequential values for the animated property when [`bindTarget`](../animationdefinition/bindtarget.md) is an array of `Double` values.

## See Also

### Defining frames data
- [var frames: [JointTransforms]](./frames-4eeex.md)
  An array of joint transforms in which each element represents a discrete state of the target entity at a given point in the animation’s timeline.
- [var frames: [Transform]](./frames-4qotl.md)
  An array of transforms in which each element represents a discrete state of the target entity at a given point in the animation’s timeline.
- [var frames: [Float]](./frames-2j4nj.md)
  An array of floating-point values in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [simd_quatf]](./frames-2h6tu.md)
  An array of quaternions in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [SIMD2<Float>]](./frames-9luwf.md)
  An array of floating-point pairs in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [SIMD3<Float>]](./frames-1zxo.md)
  An array of floating-point triplets in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.
- [var frames: [SIMD4<Float>]](./frames-2ywfx.md)
  An array of floating-point quadruples in which each element represents a discrete state of the animated property at a given point in the animation’s timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/frames-2hobp)*