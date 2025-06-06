# resizeNearest(_:sizeTensor:scaleOffsetTensor:nearestRoundingMode:layout:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Resamples input images to given size using the provided scale and offset and nearest neighbor sampling See above discussion for more details.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func resizeNearest(_ imagesTensor: MPSGraphTensor, sizeTensor size: MPSGraphTensor, scaleOffsetTensor scaleOffset: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `imagesTensor`: Tensor containing input images.
- `size`: 1D Int32 or Int64 tensor. A 2-element shape as [newHeight, newWidth]
- `scaleOffset`: 1D float tensor. A 4-element shape as [scaleY, scaleX, offsetY, offsetX]
- `nearestRoundingMode`: The rounding mode to use when using nearest resampling.
- `layout`: Specifies what layout the provided tensor is in. The returned tensor will follow the same layout. Valid layouts are NHWC, NCHW, HWC, CHW, and HW.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/resizenearest(_:sizetensor:scaleoffsettensor:nearestroundingmode:layout:name:))*