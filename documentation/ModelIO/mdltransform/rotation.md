# rotation

**Framework**: Model I/O  
**Kind**: property

The orientation, as a vector of Euler angles in radians, of the transform relative to its parent coordinate space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rotation: vector_float3 { get set }
```

#### Discussion

The three components of this vector describe counterclockwise rotation around the corresponding axes. In a coordinate system where the negative z-axis direction is considered “forward”, these components are pitch (rotation about the x-axis), yaw (rotation about the y-axis), and roll (rotation about the z-axis).

Together with the [`translation`](mdltransform/translation.md), [`scale`](mdltransform/scale.md), and [`shear`](mdltransform/shear.md) properties, this property defines the local coordinate space for any object affected by the transform, relative to a parent coordinate space. Use the [`matrix`](mdltransformcomponent/matrix.md) property to work with the complete transform.

If the transform includes time-based information, reading this property returns the rotation as of the earliest time sample (as reported by the [`minimumTime`](mdltransformcomponent/minimumtime.md) property). Writing to this property erases any time-sampled data for the rotation factor. To work with time-sampled data from an animated transform, use the [`rotation(atTime:)`](mdltransform/rotation(attime:).md) and [`setRotation(_:forTime:)`](mdltransform/setrotation(_:fortime:).md) methods.

## See Also

- [var translation: vector_float3](mdltransform/translation.md)
  The x-, y-, and z-axis offsets of the transform relative to its parent coordinate space.
- [var scale: vector_float3](mdltransform/scale.md)
  The x-, y-, and z-axis scale factors of the transform relative to its parent coordinate space.
- [var shear: vector_float3](mdltransform/shear.md)
  The x-, y-, and z-axis shear factors of the transform relative to its parent coordinate space.
- [func setIdentity()](mdltransform/setidentity.md)
  Sets all factors of the transform to those of the identity transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/rotation)*