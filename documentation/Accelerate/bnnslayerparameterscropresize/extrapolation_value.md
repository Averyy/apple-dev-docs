# extrapolation_value

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A value that the operation uses for extrapolation. Default value is `0`.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
var extrapolation_value: Float
```

```c
float extrapolation_value;
```

## See Also

### Instance Properties
- [var normalized_coordinates: Bool](./normalized_coordinates.md)
  A Boolean value that specifies whether the operation treats the coordinates as normalized to `0...1`.
- [var spatial_scale: Float](./spatial_scale.md)
  An additional spatial scale that mutliplies the bounding box coordinates.
- [var sampling_mode: BNNSLinearSamplingMode](./sampling_mode.md)
  The sampling mode that the operation uses to select sample points.
- [var box_coordinate_mode: BNNSBoxCoordinateMode](./box_coordinate_mode.md)
  A constant that defines the convention that the operation uses to specify the four bounding box coordinates.
- [var method: BNNSInterpolationMethod](./method.md)
  The interpolation method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterscropresize/extrapolation_value)*