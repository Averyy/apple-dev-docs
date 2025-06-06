# init(normalized_coordinates:spatial_scale:extrapolation_value:sampling_mode:box_coordinate_mode:method:)

**Framework**: Accelerate  
**Kind**: init

Creates a new layer parameters structure.

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
init(normalized_coordinates: Bool, spatial_scale: Float, extrapolation_value: Float, sampling_mode: BNNSLinearSamplingMode, box_coordinate_mode: BNNSBoxCoordinateMode, method: BNNSInterpolationMethod)
```

## Parameters

- `normalized_coordinates`: A Boolean value that specifies whether the operation treats the coordinates as normalized to  .
- `spatial_scale`: An additional spatial scale that mutliplies the bounding box coordinates.
- `extrapolation_value`: A value that the operation uses for extrapolation. Default value is  .
- `sampling_mode`: The sampling mode that the operation uses to select sample points.
- `box_coordinate_mode`: A constant that defines the convention for the operation uses to specify the four bounding box coordinates.
- `method`: The interpolation method.

## See Also

- [init()](bnnslayerparameterscropresize/init.md)
  Creates a new empty layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterscropresize/init(normalized_coordinates:spatial_scale:extrapolation_value:sampling_mode:box_coordinate_mode:method:))*