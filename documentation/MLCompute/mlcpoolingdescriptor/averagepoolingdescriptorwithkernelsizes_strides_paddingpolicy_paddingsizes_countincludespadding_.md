# averagePoolingDescriptorWithKernelSizes:strides:paddingPolicy:paddingSizes:countIncludesPadding:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates an average pooling descriptor with the kernel sizes, strides, padding policy, padding sizes, and zero padding option that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) averagePoolingDescriptorWithKernelSizes:(NSArray<NSNumber *> *) kernelSizes strides:(NSArray<NSNumber *> *) strides paddingPolicy:(MLCPaddingPolicy) paddingPolicy paddingSizes:(NSArray<NSNumber *> *) paddingSizes countIncludesPadding:(BOOL) countIncludesPadding;
```

## Return Value

A pooling descriptor.

## Parameters

- `kernelSizes`: An array that contains the kernel sizes for y and x.
- `strides`: An array that contains the kernel strides for y and x.
- `paddingPolicy`: The padding policy.
- `paddingSizes`: An array that contains the padding sizes for y and x.
- `countIncludesPadding`: A Boolean that indicates whether you include zero padding in the averaging calculation.

## See Also

### Creating Pooling Descriptors
- [+ maxPoolingDescriptorWithKernelSizes:strides:paddingPolicy:paddingSizes:](./maxpoolingdescriptorwithkernelsizes_strides_paddingpolicy_paddingsizes_.md)
  Creates a descriptor for a max pooling function with the kernel sizes, strides, padding policy, and padding sizes that you specify.
- [+ maxPoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:](./maxpoolingdescriptorwithkernelsizes_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a descriptor for a max pooling function with the kernel sizes, strides, dilation rates, padding policy, and padding sizes that you specify.
- [+ averagePoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:countIncludesPadding:](./averagepoolingdescriptorwithkernelsizes_strides_dilationrates_paddingpolicy_paddingsizes_countincludespadding_.md)
  Creates an average pooling descriptor with the kernel sizes, strides, dilution rates, padding policy and sizes, and zero padding option you specify.
- [+ l2NormPoolingDescriptorWithKernelSizes:strides:paddingPolicy:paddingSizes:](./l2normpoolingdescriptorwithkernelsizes_strides_paddingpolicy_paddingsizes_.md)
  Creates a descriptor for an L2 norm pooling function with the kernel sizes, strides, padding policy, and padding sizes that you specify.
- [+ l2NormPoolingDescriptorWithKernelSizes:strides:dilationRates:paddingPolicy:paddingSizes:](./l2normpoolingdescriptorwithkernelsizes_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a descriptor for an L2 norm pooling function with the kernel sizes, strides, dilation rates, padding policy, and padding sizes you specify.
- [+ poolingDescriptorWithType:kernelSize:stride:](./poolingdescriptorwithtype_kernelsize_stride_.md)
  Creates a pooling descriptor with the pooling function, kernel size, and stride you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolingdescriptor/averagepoolingdescriptorwithkernelsizes:strides:paddingpolicy:paddingsizes:countincludespadding:)*