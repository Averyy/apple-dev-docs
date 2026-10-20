# init(method:i_desc:o_desc:align_corners:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new resize-layer parameters structure from the specified parameters.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
init(method: BNNSInterpolationMethod, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, align_corners: Bool)
```

#### Discussion

> ❗ **Important**:  The number of input dimensions must be equal to number of output dimensions. The resize must be in same direction for all dimensions.

## Parameters

- `method`: The interpolation method for resizing.
- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `align_corners`: A Boolean value that specifies whether to align the corners of the upscaling grid to the center of scaling dimensions instead of to the edges.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Returns a new resize-layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersresize/init(method:i_desc:o_desc:align_corners:))*