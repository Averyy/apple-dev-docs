# MLCPoolingType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A pooling function type for a pooling layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
enum MLCPoolingType
```

## Topics

### Enumeration Cases
- [MLCPoolingType.max](./mlcpoolingtype-wb8j/max.md)
- [MLCPoolingType.average(countIncludesPadding:)](./mlcpoolingtype-wb8j/average%28countincludespadding%29.md)
- [MLCPoolingType.l2Norm](./mlcpoolingtype-wb8j/l2norm.md)
- [var debugDescription: String](./mlcpoolingtype-wb8j/debugdescription.md)
  A textual description of the pooling type, suitable for debugging.

## See Also

### Creating Pooling Layers
- [convenience init(descriptor: MLCPoolingDescriptor)](./mlcpoolinglayer/init%28descriptor%29.md)
  Creates a pooling layer with the descriptor you specify.
- [class MLCPoolingDescriptor](./mlcpoolingdescriptor.md)
  A configuration object you use to create a pooling layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolingtype-wb8j)*