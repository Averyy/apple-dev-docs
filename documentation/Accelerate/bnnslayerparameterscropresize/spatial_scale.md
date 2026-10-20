# spatial_scale

**Framework**: Accelerate  
**Kind**: property

An additional spatial scale that mutliplies the bounding box coordinates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var spatial_scale: Float
```

## See Also

- [var normalized_coordinates: Bool](bnnslayerparameterscropresize/normalized_coordinates.md)
  A Boolean value that specifies whether the operation treats the coordinates as normalized to `0...1`.
- [var extrapolation_value: Float](bnnslayerparameterscropresize/extrapolation_value.md)
  A value that the operation uses for extrapolation. Default value is `0`.
- [var sampling_mode: BNNSLinearSamplingMode](bnnslayerparameterscropresize/sampling_mode.md)
  The sampling mode that the operation uses to select sample points.
- [var box_coordinate_mode: BNNSBoxCoordinateMode](bnnslayerparameterscropresize/box_coordinate_mode.md)
  A constant that defines the convention that the operation uses to specify the four bounding box coordinates.
- [var method: BNNSInterpolationMethod](bnnslayerparameterscropresize/method.md)
  The interpolation method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterscropresize/spatial_scale)*