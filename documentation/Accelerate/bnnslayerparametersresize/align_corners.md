# align_corners

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether to align the corners of the upscaling grid to the center of scaling dimensions instead of to the edges.

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
var align_corners: Bool
```

```c
bool align_corners;
```

## See Also

### Instance Properties
- [var method: BNNSInterpolationMethod](./method.md)
  The interpolation method for resizing.
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersresize/align_corners)*