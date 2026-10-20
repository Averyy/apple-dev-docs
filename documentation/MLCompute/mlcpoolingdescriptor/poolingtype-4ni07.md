# poolingType

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The pooling operation type.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
var poolingType: MLCPoolingType { get }
```

## See Also

### Inspecting Pooling Descriptors
- [var kernelSizes: (height: Int, width: Int)](./kernelsizes.md)
  A tuple that contains the kernel sizes for height and width.
- [var strides: (y: Int, x: Int)](./strides.md)
  A tuple that contains the kernel strides for y and x.
- [var dilationRates: (y: Int, x: Int)](./dilationrates.md)
  A tuple that contains the dilation rates for y and x.
- [var paddingPolicy: MLCPaddingPolicy](./paddingpolicy-7p8a2.md)
  The padding policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolingdescriptor/poolingtype-4ni07)*