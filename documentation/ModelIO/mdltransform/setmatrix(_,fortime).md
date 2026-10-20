# setMatrix(_:forTime:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setMatrix(_ matrix: matrix_float4x4, forTime time: TimeInterval)
```

```objc
- (void) setMatrix:(matrix_float4x4) matrix forTime:(NSTimeInterval) time;
```

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
- [func setScale(vector_float3, forTime: TimeInterval)](./setscale%28_,fortime%29.md)
  Sets the x-, y-, and z-axis scale factors of the transform for the specified time sample.
- [func shear(atTime: TimeInterval) -> vector_float3](./shear%28attime%29.md)
  Returns the x-, y-, and z-axis shear factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setShear(vector_float3, forTime: TimeInterval)](./setshear%28_,fortime%29.md)
  Sets the x-, y-, and z-axis shear factors of the transform for the specified time sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/setmatrix(_:fortime:))*