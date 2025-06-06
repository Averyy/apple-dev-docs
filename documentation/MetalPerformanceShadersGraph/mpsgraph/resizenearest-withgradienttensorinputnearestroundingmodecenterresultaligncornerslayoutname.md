# resizeNearest(withGradientTensor:input:nearestRoundingMode:centerResult:alignCorners:layout:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a Resize gradient operation and returns the result tensor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func resizeNearest(withGradientTensor gradient: MPSGraphTensor, input: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Computes the gradient for the forward pass Resize op with identical parameters. See discussion of resizeTensor for more in depth description of resize paramters.

## Parameters

- `gradient`: Incoming gradient tensor
- `input`: Forward pass input tensor
- `nearestRoundingMode`: The rounding mode to use when using nearest resampling.
- `centerResult`: Controls if the result image is centered on the input image. When NO, the result will have the top left corner aligned
- `alignCorners`: When YES, the result image will have the same value as the input image in the corners
- `layout`: Specifies what layout the provided tensor is in. The returned tensor will follow the same layout. Valid layouts are NHWC, NCHW, HWC, CHW, and HW.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/resizenearest(withgradienttensor:input:nearestroundingmode:centerresult:aligncorners:layout:name:))*