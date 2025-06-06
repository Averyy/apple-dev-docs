# rotationMatrix(atTime:)

**Framework**: Model I/O  
**Kind**: method

Returns the orientation of the transform as a rotation matrix, as of the specified time sample.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func rotationMatrix(atTime time: TimeInterval) -> matrix_float4x4
```

#### Return Value

The orientation, as a rotation matrix, of the transform.

#### Discussion

A rotation matrix provides the same information as the vector returned by the [`rotation(atTime:)`](mdltransform/rotation(attime:).md) method, but in a form more convenient for multiplying with position vectors.

Together with the translation, scale, and shear factors, rotation information defines the local coordinate space for any object affected by the transform, relative to a parent coordinate space. To work with the complete transform, use the [`localTransform(atTime:)`](mdltransformcomponent/localtransform(attime:).md) and [`setLocalTransform(_:forTime:)`](mdltransformcomponent/setlocaltransform(_:fortime:).md) methods.

Requesting a sample outside the time range clamps results to the [`minimumTime`](mdltransformcomponent/minimumtime.md) or [`maximumTime`](mdltransformcomponent/maximumtime.md) sample. Some asset formats support continuous sampling with interpolation for times between the samples stored in the asset; others are discrete. For an asset with discrete time information, requesting a sample time in between the samples stored in the asset returns data for the immediately preceding time.

## Parameters

- `time`: The time sample for which to request information.

## See Also

- [func translation(atTime: TimeInterval) -> vector_float3](mdltransform/translation(attime:).md)
  Returns the x-, y-, and z-axis offsets of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setTranslation(vector_float3, forTime: TimeInterval)](mdltransform/settranslation(_:fortime:).md)
  Sets the x-, y-, and z-axis offsets of the transform for the specified time sample.
- [func rotation(atTime: TimeInterval) -> vector_float3](mdltransform/rotation(attime:).md)
  Returns the orientation of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setRotation(vector_float3, forTime: TimeInterval)](mdltransform/setrotation(_:fortime:).md)
  Sets the orientation of the transform for the specified time sample.
- [func scale(atTime: TimeInterval) -> vector_float3](mdltransform/scale(attime:).md)
  Returns the x-, y-, and z-axis scale factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setScale(vector_float3, forTime: TimeInterval)](mdltransform/setscale(_:fortime:).md)
  Sets the x-, y-, and z-axis scale factors of the transform for the specified time sample.
- [func shear(atTime: TimeInterval) -> vector_float3](mdltransform/shear(attime:).md)
  Returns the x-, y-, and z-axis shear factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setShear(vector_float3, forTime: TimeInterval)](mdltransform/setshear(_:fortime:).md)
  Sets the x-, y-, and z-axis shear factors of the transform for the specified time sample.
- [func setMatrix(matrix_float4x4, forTime: TimeInterval)](mdltransform/setmatrix(_:fortime:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/rotationmatrix(attime:))*