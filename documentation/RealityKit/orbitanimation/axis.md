# axis

**Framework**: RealityKit  
**Kind**: property

A 3D vector that points in the direction of the axis around which to rotate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var axis: SIMD3<Float> { get set }
```

#### Discussion

You can rotate an object around any axis. For example, if you set a `1` in the vector’s x-coordinate, rotation occurs around the x-axis, as in the following code.

```swift
orbitAnimation.axis = SIMD3<Float>(x: 1.0, y: 0.0, z: 0.0)
```

## See Also

- [var startTransform: Transform](orbitanimation/starttransform.md)
  The pose of the orbiting object at the start of the animation.
- [var name: String](orbitanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](orbitanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](orbitanimation/blendlayer.md)
  The order in which the framework composites the animation.
- [var rotationCount: Float](orbitanimation/rotationcount.md)
  The number of times to rotate the target entity before stopping.
- [var spinClockwise: Bool](orbitanimation/spinclockwise.md)
  A Boolean value that indicates whether the object orbits the center point in the clockwise direction.
- [var orientToPath: Bool](orbitanimation/orienttopath.md)
  A Boolean value that indicates whether the orbiting object updates its orientation during the animation to orient itself along the rotation path.
- [var additive: Bool](orbitanimation/additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/orbitanimation/axis)*