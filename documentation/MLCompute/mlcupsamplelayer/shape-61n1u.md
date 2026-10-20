# shape

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

An array that contains the dimensions of the result tensor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
var shape: [Int] { get }
```

## See Also

### Inspecting Upsample Layers
- [var sampleMode: MLCSampleMode](./samplemode.md)
  The upsampling algorithm type.
- [var alignsCorners: Bool](./alignscorners.md)
  A Boolean that indicates whether the layer aligns the corner pixels of the input and output tensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcupsamplelayer/shape-61n1u)*