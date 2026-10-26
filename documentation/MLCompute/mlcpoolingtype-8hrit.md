# MLCPoolingType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A pooling function type for a pooling layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```c
enum MLCPoolingType : int32_t;
```

## Topics

### Enumeration Cases
- [MLCPoolingTypeMax](./mlcpoolingtype-8hrit/mlcpoolingtypemax.md)
- [MLCPoolingTypeL2Norm](./mlcpoolingtype-8hrit/mlcpoolingtypel2norm.md)
- [MLCPoolingTypeAverage](./mlcpoolingtype-8hrit/mlcpoolingtypeaverage.md)
- [MLCPoolingTypeCount](./mlcpoolingtype-8hrit/mlcpoolingtypecount.md)
- [MLCPoolingTypeDebugDescription](./mlcpoolingtypedebugdescription.md)
  A textual description of the pooling type, suitable for debugging.

## See Also

### Creating Pooling Layers
- [convenience init(descriptor: MLCPoolingDescriptor)](./mlcpoolinglayer/init%28descriptor%29.md)
  Creates a pooling layer with the descriptor you specify.
- [class MLCPoolingDescriptor](./mlcpoolingdescriptor.md)
  A configuration object you use to create a pooling layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolingtype-8hrit)*