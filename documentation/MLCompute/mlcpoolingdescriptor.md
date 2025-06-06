# MLCPoolingDescriptor

**Framework**: ML Compute  
**Kind**: class

A configuration object you use to create a pooling layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCPoolingDescriptor
```

## Topics

### Creating Pooling Descriptors
- [convenience init(type: MLCPoolingType, kernelSizes: (height: Int, width: Int), strides: (y: Int, x: Int), dilationRates: (y: Int, x: Int), paddingPolicy: MLCPaddingPolicy)](mlcpoolingdescriptor/init(type:kernelsizes:strides:dilationrates:paddingpolicy:).md)
  Creates a pooling descriptor with the pooling function type, kernel sizes, strides, dilation rates, and padding policy that you specify.
### Inspecting Pooling Descriptors
- [var poolingType: MLCPoolingType](mlcpoolingdescriptor/poolingtype-4ni07.md)
  The pooling operation type.
- [var kernelSizes: (height: Int, width: Int)](mlcpoolingdescriptor/kernelsizes.md)
  A tuple that contains the kernel sizes for height and width.
- [var strides: (y: Int, x: Int)](mlcpoolingdescriptor/strides.md)
  A tuple that contains the kernel strides for y and x.
- [var dilationRates: (y: Int, x: Int)](mlcpoolingdescriptor/dilationrates.md)
  A tuple that contains the dilation rates for y and x.
- [var paddingPolicy: MLCPaddingPolicy](mlcpoolingdescriptor/paddingpolicy-7p8a2.md)
  The padding policy.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(descriptor: MLCPoolingDescriptor)](mlcpoolinglayer/init(descriptor:).md)
  Creates a pooling layer with the descriptor you specify.
- [enum MLCPoolingType](mlcpoolingtype-wb8j.md)
  A pooling function type for a pooling layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolingdescriptor)*