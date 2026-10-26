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
- [+ maxPoolingDescriptorWithKernelSizes:strides:paddingPolicy:paddingSizes:](./mlcpoolingdescriptor/maxpoolingdescriptorwithkernelsizes_strides_paddingpolicy_paddingsizes_.md)
  Creates a descriptor for a max pooling function with the kernel sizes, strides, padding policy, and padding sizes that you specify.
- [+ maxPoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:](./mlcpoolingdescriptor/maxpoolingdescriptorwithkernelsizes_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a descriptor for a max pooling function with the kernel sizes, strides, dilation rates, padding policy, and padding sizes that you specify.
- [+ averagePoolingDescriptorWithKernelSizes:strides:paddingPolicy:paddingSizes:countIncludesPadding:](./mlcpoolingdescriptor/averagepoolingdescriptorwithkernelsizes_strides_paddingpolicy_paddingsizes_countincludespadding_.md)
  Creates an average pooling descriptor with the kernel sizes, strides, padding policy, padding sizes, and zero padding option that you specify.
- [+ averagePoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:countIncludesPadding:](./mlcpoolingdescriptor/averagepoolingdescriptorwithkernelsizes_strides_dilationrates_paddingpolicy_paddingsizes_countincludespadding_.md)
  Creates an average pooling descriptor with the kernel sizes, strides, dilution rates, padding policy and sizes, and zero padding option you specify.
- [+ l2NormPoolingDescriptorWithKernelSizes:strides:paddingPolicy:paddingSizes:](./mlcpoolingdescriptor/l2normpoolingdescriptorwithkernelsizes_strides_paddingpolicy_paddingsizes_.md)
  Creates a descriptor for an L2 norm pooling function with the kernel sizes, strides, padding policy, and padding sizes that you specify.
- [+ l2NormPoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:](./mlcpoolingdescriptor/l2normpoolingdescriptorwithkernelsizes_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a descriptor for an L2 norm pooling function with the kernel sizes, strides, dilation rates, padding policy, and padding sizes you specify.
- [+ poolingDescriptorWithType:kernelSize:stride:](./mlcpoolingdescriptor/poolingdescriptorwithtype_kernelsize_stride_.md)
  Creates a pooling descriptor with the pooling function, kernel size, and stride you specify.
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
- [poolingType](./mlcpoolingdescriptor/poolingtype-9daku.md)
  The pooling operation type.
- [kernelWidth](./mlcpoolingdescriptor/kernelwidth.md)
  The pooling kernel size in x.
- [kernelHeight](./mlcpoolingdescriptor/kernelheight.md)
  The pooling kernel size in y.
- [strideInX](./mlcpoolingdescriptor/strideinx.md)
  The stride of the kernel in x.
- [strideInY](./mlcpoolingdescriptor/strideiny.md)
  The stride of the kernel in y.
- [dilationRateInX](./mlcpoolingdescriptor/dilationrateinx.md)
  The kernel dilation rate, or stride of elements, in x.
- [dilationRateInY](./mlcpoolingdescriptor/dilationrateiny.md)
  The kernel dilation rate, or stride of elements, in y.
- [paddingPolicy](./mlcpoolingdescriptor/paddingpolicy-1e6rg.md)
  The padding policy.
- [paddingSizeInX](./mlcpoolingdescriptor/paddingsizeinx.md)
  The padding size in x, left and right, to use if the padding policy is to use padding size.
- [paddingSizeInY](./mlcpoolingdescriptor/paddingsizeiny.md)
  The padding size in y, top and bottom, to use if the padding policy is to use padding size.
- [countIncludesPadding](./mlcpoolingdescriptor/countincludespadding.md)
  A Boolean that indicates whether you include zero padding in the averaging calculation.

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
- [MLCPoolingType](./mlcpoolingtype-8hrit.md)
  A pooling function type for a pooling layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolingdescriptor)*