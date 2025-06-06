# init(method:i_desc:o_desc:align_corners:)

**Framework**: Accelerate  
**Kind**: init

Returns a new resize-layer parameters structure from the specified parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(method: BNNSInterpolationMethod, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, align_corners: Bool)
```

#### Discussion

> ❗ **Important**:  The number of input dimensions must be equal to number of output dimensions. The resize must be in same direction for all dimensions.

 The number of input dimensions must be equal to number of output dimensions. The resize must be in same direction for all dimensions.

## Parameters

- `method`: The interpolation method for resizing.
- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `align_corners`: A Boolean value that specifies whether to align the corners of the upscaling grid to the center of scaling dimensions instead of to the edges.

## See Also

- [init()](bnnslayerparametersresize/init.md)
  Returns a new resize-layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersresize/init(method:i_desc:o_desc:align_corners:))*