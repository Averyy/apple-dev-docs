# sampleGrid(withSourceTensor:coordinateTensor:layout:normalizeCoordinates:relativeCoordinates:alignCorners:paddingMode:nearestRoundingMode:constantValue:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Samples a tensor using the coordinates provided, using nearest neighbor sampling with specified rounding mode.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- macOS 13.1+
- tvOS 16.2+
- visionOS 1.0+

## Declaration

```swift
func sampleGrid(withSourceTensor source: MPSGraphTensor, coordinateTensor coordinates: MPSGraphTensor, layout: MPSGraphTensorNamedDataLayout, normalizeCoordinates: Bool, relativeCoordinates: Bool, alignCorners: Bool, paddingMode: MPSGraphPaddingMode, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, constantValue: Double, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Given an input tensor (N, H1, W1, C) or (N, C, H1, W1) and coordinates tensor (N, H2, W2, 2) this operation outputs a tensor of size (N, H2, W2, C) or (N, C, H2, W2) by sampling the input tensor at the coordinates provided by the coordinates tensor.

## Parameters

- `source`: Tensor containing source data
- `coordinates`: A tensor (N, Hout, Wout, 2) that contains the coordinates of the samples in the source tensor that constitute the output tensor.
- `layout`: Specifies what layout the provided tensor is in. The returned tensor will follow the same layout. Valid layouts are NHWC and NCHW.
- `normalizeCoordinates`: If true, coordinates are within [-1, 1] x [-1, 1] otherwise they are in pixels in the input tensor.
- `relativeCoordinates`: If true, coordinates are relative to the postion of the pixel in the output tensor and scaled back to the input tensor size
- `alignCorners`: If true, coordinate extrema are equal to the center of edge pixels, otherwise extrema are equal to outer edge of edge pixels
- `paddingMode`: Determines how samples outside the inputTensor are evaluated (only constant, reflect, symmetric and clampToEdge are supported)
- `nearestRoundingMode`: The rounding mode to use for determining the nearest neighbor. Valid modes are roundPreferCeil, roundPreferFloor, ceil, and floor.
- `constantValue`: If paddingMode is MPSGraphPaddingModeConstant, then this constant is used for samples outside the input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/samplegrid(withsourcetensor:coordinatetensor:layout:normalizecoordinates:relativecoordinates:aligncorners:paddingmode:nearestroundingmode:constantvalue:name:))*