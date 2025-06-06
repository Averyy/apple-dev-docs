# init(type:kernelSizes:strides:dilationRates:paddingPolicy:)

**Framework**: ML Compute  
**Kind**: init

Creates a pooling descriptor with the pooling function type, kernel sizes, strides, dilation rates, and padding policy that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(type: MLCPoolingType, kernelSizes: (height: Int, width: Int), strides: (y: Int, x: Int) = (y: 1, x: 1), dilationRates: (y: Int, x: Int) = (y: 1, x: 1), paddingPolicy: MLCPaddingPolicy = .same)
```

## Parameters

- `type`: The pooling function type.
- `kernelSizes`: A tuple that contains the kernel sizes for y and x.
- `strides`: A tuple that contains the kernel strides for y and x.
- `dilationRates`: A tuple that contains the dilation rates for y and x.
- `paddingPolicy`: The padding policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolingdescriptor/init(type:kernelsizes:strides:dilationrates:paddingpolicy:))*