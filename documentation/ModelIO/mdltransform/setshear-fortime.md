# setShear(_:forTime:)

**Framework**: Model I/O  
**Kind**: method

Sets the x-, y-, and z-axis shear factors of the transform for the specified time sample.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setShear(_ shear: vector_float3, forTime time: TimeInterval)
```

#### Discussion

Together with the translation, rotation, and scale factors, a shear vector defines the local coordinate space for any object affected by the transform, relative to a parent coordinate space. To work with the complete transform, use the [`localTransform(atTime:)`](mdltransformcomponent/localtransform(attime:).md) and [`setLocalTransform(_:forTime:)`](mdltransformcomponent/setlocaltransform(_:fortime:).md) methods.

Setting a new shear synthesizes a complete transform matrix by combining the new translation with the [`translation(atTime:)`](mdltransform/translation(attime:).md), [`rotation(atTime:)`](mdltransform/rotation(attime:).md), and [`scale(atTime:)`](mdltransform/scale(attime:).md) factors for the specified time. If the new time is outside the range of the [`minimumTime`](mdltransformcomponent/minimumtime.md) and [`maximumTime`](mdltransformcomponent/maximumtime.md) properties, this method updates those values to reflect the range of time samples stored in the transform object.

## Parameters

- `shear`: The shear factors to set for the transform relative to its parent coordinate space.
- `time`: The time sample with which to associate transform information.

## See Also

- [func translation(atTime: TimeInterval) -> vector_float3](mdltransform/translation(attime:).md)
  Returns the x-, y-, and z-axis offsets of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setTranslation(vector_float3, forTime: TimeInterval)](mdltransform/settranslation(_:fortime:).md)
  Sets the x-, y-, and z-axis offsets of the transform for the specified time sample.
- [func rotation(atTime: TimeInterval) -> vector_float3](mdltransform/rotation(attime:).md)
  Returns the orientation of the transform relative to its parent coordinate space, as of the specified time sample.
- [func rotationMatrix(atTime: TimeInterval) -> matrix_float4x4](mdltransform/rotationmatrix(attime:).md)
  Returns the orientation of the transform as a rotation matrix, as of the specified time sample.
- [func setRotation(vector_float3, forTime: TimeInterval)](mdltransform/setrotation(_:fortime:).md)
  Sets the orientation of the transform for the specified time sample.
- [func scale(atTime: TimeInterval) -> vector_float3](mdltransform/scale(attime:).md)
  Returns the x-, y-, and z-axis scale factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setScale(vector_float3, forTime: TimeInterval)](mdltransform/setscale(_:fortime:).md)
  Sets the x-, y-, and z-axis scale factors of the transform for the specified time sample.
- [func shear(atTime: TimeInterval) -> vector_float3](mdltransform/shear(attime:).md)
  Returns the x-, y-, and z-axis shear factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setMatrix(matrix_float4x4, forTime: TimeInterval)](mdltransform/setmatrix(_:fortime:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/setshear(_:fortime:))*