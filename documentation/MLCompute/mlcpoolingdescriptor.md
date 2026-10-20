# MLCPoolingDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A configuration object you use to create a pooling layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCPoolingDescriptor
```

```objc
@interface MLCPoolingDescriptor : NSObject
```

## Topics

### Creating Pooling Descriptors
- [convenience init(type: MLCPoolingType, kernelSizes: (height: Int, width: Int), strides: (y: Int, x: Int), dilationRates: (y: Int, x: Int), paddingPolicy: MLCPaddingPolicy)](./mlcpoolingdescriptor/init%28type,kernelsizes,strides,dilationrates,paddingpolicy%29.md)
  Creates a pooling descriptor with the pooling function type, kernel sizes, strides, dilation rates, and padding policy that you specify.
### Inspecting Pooling Descriptors
- [var poolingType: MLCPoolingType](./mlcpoolingdescriptor/poolingtype-4ni07.md)
  The pooling operation type.
- [var kernelSizes: (height: Int, width: Int)](./mlcpoolingdescriptor/kernelsizes.md)
  A tuple that contains the kernel sizes for height and width.
- [var strides: (y: Int, x: Int)](./mlcpoolingdescriptor/strides.md)
  A tuple that contains the kernel strides for y and x.
- [var dilationRates: (y: Int, x: Int)](./mlcpoolingdescriptor/dilationrates.md)
  A tuple that contains the dilation rates for y and x.
- [var paddingPolicy: MLCPaddingPolicy](./mlcpoolingdescriptor/paddingpolicy-7p8a2.md)
  The padding policy.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating Pooling Layers
- [convenience init(descriptor: MLCPoolingDescriptor)](./mlcpoolinglayer/init%28descriptor%29.md)
  Creates a pooling layer with the descriptor you specify.
- [enum MLCPoolingType](./mlcpoolingtype-wb8j.md)
  A pooling function type for a pooling layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolingdescriptor)*