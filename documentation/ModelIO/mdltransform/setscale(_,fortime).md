# setScale(_:forTime:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Sets the x-, y-, and z-axis scale factors of the transform for the specified time sample.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setScale(_ scale: vector_float3, forTime time: TimeInterval)
```

```objc
- (void) setScale:(vector_float3) scale forTime:(NSTimeInterval) time;
```

#### Discussion

Together with the translation, rotation, and shear factors, a scale factor defines the local coordinate space for any object affected by the transform, relative to a parent coordinate space. To work with the complete transform, use the [`localTransform(atTime:)`](../mdltransformcomponent/localtransform%28attime%29.md) and [`setLocalTransform(_:forTime:)`](../mdltransformcomponent/setlocaltransform%28_,fortime%29.md) methods.

Setting a new scale synthesizes a complete transform matrix by combining the new translation with the [`translation(atTime:)`](./translation%28attime%29.md), [`rotation(atTime:)`](./rotation%28attime%29.md), and [`shear(atTime:)`](./shear%28attime%29.md) factors for the specified time. If the new time is outside the range of the [`minimumTime`](../mdltransformcomponent/minimumtime.md) and [`maximumTime`](../mdltransformcomponent/maximumtime.md) properties, this method updates those values to reflect the range of time samples stored in the transform object.

## Parameters

- `scale`: The scale factors to set for the transform relative to its parent coordinate space.
- `time`: The time sample with which to associate transform information.

## See Also

### Using Factors of an Animated Transform
- [func translation(atTime: TimeInterval) -> vector_float3](./translation%28attime%29.md)
  Returns the x-, y-, and z-axis offsets of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setTranslation(vector_float3, forTime: TimeInterval)](./settranslation%28_,fortime%29.md)
  Sets the x-, y-, and z-axis offsets of the transform for the specified time sample.
- [func rotation(atTime: TimeInterval) -> vector_float3](./rotation%28attime%29.md)
  Returns the orientation of the transform relative to its parent coordinate space, as of the specified time sample.
- [func rotationMatrix(atTime: TimeInterval) -> matrix_float4x4](./rotationmatrix%28attime%29.md)
  Returns the orientation of the transform as a rotation matrix, as of the specified time sample.
- [func setRotation(vector_float3, forTime: TimeInterval)](./setrotation%28_,fortime%29.md)
  Sets the orientation of the transform for the specified time sample.
- [func scale(atTime: TimeInterval) -> vector_float3](./scale%28attime%29.md)
  Returns the x-, y-, and z-axis scale factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func shear(atTime: TimeInterval) -> vector_float3](./shear%28attime%29.md)
  Returns the x-, y-, and z-axis shear factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setShear(vector_float3, forTime: TimeInterval)](./setshear%28_,fortime%29.md)
  Sets the x-, y-, and z-axis shear factors of the transform for the specified time sample.
- [func setMatrix(matrix_float4x4, forTime: TimeInterval)](./setmatrix%28_,fortime%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/setscale(_:fortime:))*