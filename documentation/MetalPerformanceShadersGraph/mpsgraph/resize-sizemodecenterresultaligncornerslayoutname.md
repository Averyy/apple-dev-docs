# resize(_:size:mode:centerResult:alignCorners:layout:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a Resize operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func resize(_ imagesTensor: MPSGraphTensor, size: [NSNumber], mode: MPSGraphResizeMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Resamples input images to given size. Result images will be distorted if size is of different aspect ratio. Resize supports the following modes: Nearest Neighbor - values are interpolated using the closest neighbor pixel Bilinear - values are computed using bilinear interpolation of 4 neighboring pixels Destination indices are computed using direct index scaling by default, with no offset added. If the centerResult parameter is true, the destination indices will be scaled and shifted to be centered on the input image. If the alignCorners parameter is true, the corners of the result images will match the input images. Scaling will be modified to a factor of (size - 1) / (inputSize - 1). When alignCorners is true, the centerResult parameter does nothing. In order to achieve the same behavior as OpenCV’s resize and TensorFlowV2’s resize,

```md
centerResult = YES; 
alginCorners = NO; 
```

To achieve the same behavior as TensorFlowV1 resize

```md
centerResult = NO; 
```

## Parameters

- `imagesTensor`: Tensor containing input images.
- `size`: A 2-element shape as [newHeight, newWidth]
- `mode`: The resampling mode to use. If nearest sampling is specifed, RoundPreferCeil mode will be used.
- `centerResult`: Controls if the result image is centered on the input image. When NO, the result will have the top left corner aligned
- `alignCorners`: When YES, the result image will have the same value as the input image in the corners
- `layout`: Specifies what layout the provided tensor is in. The returned tensor will follow the same layout. Valid layouts are NHWC, NCHW, HWC, CHW, and HW.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/resize(_:size:mode:centerresult:aligncorners:layout:name:))*