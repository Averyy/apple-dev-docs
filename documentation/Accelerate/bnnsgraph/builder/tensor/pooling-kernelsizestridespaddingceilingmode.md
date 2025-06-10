# pooling(_:kernelSize:strides:padding:ceilingMode:)

**Framework**: Accelerate  
**Kind**: method

Adds a pooling operation to the current graph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func pooling(_ function: BNNSGraph.Builder.PoolingFunction, kernelSize: [Int], strides: [Int], padding: BNNSGraph.Builder.PoolingPadding, ceilingMode: BNNSGraph.Builder.CeilingMode) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This operation assumes the source tensor is in  `(N, C, spatial dimensions...)` format, where the number of spatial dimensions is either `1` or `2`

## Parameters

- `function`: An enumeration that specifies the pooling function.
- `kernelSize`: The size of the pooling kernel.
- `strides`: An array that contains the kernel stride for each spatial dimension.
- `padding`: An enumeration that specifies that the operation computes the padding from   the input and output shapes. If you specify  , pass twice the number of spatial dimensions.
- `ceilingMode`: An enumeration that specifies how the operation rounds when calculating the output size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/pooling(_:kernelsize:strides:padding:ceilingmode:))*