# spinClockwise

**Framework**: RealityKit  
**Kind**: property

A Boolean value that indicates whether the object orbits the center point in the clockwise direction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var spinClockwise: Bool { get set }
```

#### Discussion

The default value is `true`, which indicates that the rotation occurs in the clockwise direction. Set the value to `false` to cause the object to orbit the center point counterclockwise.

## See Also

- [var startTransform: Transform](orbitanimation/starttransform.md)
  The pose of the orbiting object at the start of the animation.
- [var axis: SIMD3<Float>](orbitanimation/axis.md)
  A 3D vector that points in the direction of the axis around which to rotate.
- [var name: String](orbitanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](orbitanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](orbitanimation/blendlayer.md)
  The order in which the framework composites the animation.
- [var rotationCount: Float](orbitanimation/rotationcount.md)
  The number of times to rotate the target entity before stopping.
- [var orientToPath: Bool](orbitanimation/orienttopath.md)
  A Boolean value that indicates whether the orbiting object updates its orientation during the animation to orient itself along the rotation path.
- [var additive: Bool](orbitanimation/additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitanimation/spinclockwise)*