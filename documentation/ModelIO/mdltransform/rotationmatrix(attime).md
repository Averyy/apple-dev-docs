# rotationMatrix(atTime:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (matrix_float4x4) rotationMatrixAtTime:(NSTimeInterval) time;
```

## Return Value

The orientation, as a rotation matrix, of the transform.

## Discussion

A rotation matrix provides the same information as the vector returned by the [`rotation(atTime:)`](./rotation%28attime%29.md) method, but in a form more convenient for multiplying with position vectors.

Together with the translation, scale, and shear factors, rotation information defines the local coordinate space for any object affected by the transform, relative to a parent coordinate space. To work with the complete transform, use the [`localTransform(atTime:)`](../mdltransformcomponent/localtransform%28attime%29.md) and [`setLocalTransform(_:forTime:)`](../mdltransformcomponent/setlocaltransform%28_,fortime%29.md) methods.

Requesting a sample outside the time range clamps results to the [`minimumTime`](../mdltransformcomponent/minimumtime.md) or [`maximumTime`](../mdltransformcomponent/maximumtime.md) sample. Some asset formats support continuous sampling with interpolation for times between the samples stored in the asset; others are discrete. For an asset with discrete time information, requesting a sample time in between the samples stored in the asset returns data for the immediately preceding time.

## Parameters

- `time`: The time sample for which to request information.

## See Also

### Using Factors of an Animated Transform
- [func translation(atTime: TimeInterval) -> vector_float3](./translation%28attime%29.md)
  Returns the x-, y-, and z-axis offsets of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setTranslation(vector_float3, forTime: TimeInterval)](./settranslation%28_,fortime%29.md)
  Sets the x-, y-, and z-axis offsets of the transform for the specified time sample.
- [func rotation(atTime: TimeInterval) -> vector_float3](./rotation%28attime%29.md)
  Returns the orientation of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setRotation(vector_float3, forTime: TimeInterval)](./setrotation%28_,fortime%29.md)
  Sets the orientation of the transform for the specified time sample.
- [func scale(atTime: TimeInterval) -> vector_float3](./scale%28attime%29.md)
  Returns the x-, y-, and z-axis scale factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setScale(vector_float3, forTime: TimeInterval)](./setscale%28_,fortime%29.md)
  Sets the x-, y-, and z-axis scale factors of the transform for the specified time sample.
- [func shear(atTime: TimeInterval) -> vector_float3](./shear%28attime%29.md)
  Returns the x-, y-, and z-axis shear factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setShear(vector_float3, forTime: TimeInterval)](./setshear%28_,fortime%29.md)
  Sets the x-, y-, and z-axis shear factors of the transform for the specified time sample.
- [func setMatrix(matrix_float4x4, forTime: TimeInterval)](./setmatrix%28_,fortime%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/rotationmatrix(attime:))*