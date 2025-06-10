# conv(weight:strides:bias:padding:dilations:groupCount:)

**Framework**: Accelerate  
**Kind**: method

Adds a convolution operation to the current graph.

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
func conv(weight: some BNNSGraph.Builder.OperationParameter<T>, strides: [Int], bias: some BNNSGraph.Builder.OperationParameter<T>, padding: BNNSGraph.Builder.ConvolutionPadding, dilations: [Int]? = nil, groupCount: Int = 1) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This operation assumes the source tensor is in  `(N, C, spatial dimensions...)` format, where the number of spatial dimensions is either `1` or `2`.

## Parameters

- `weight`: The convolution weights.
- `strides`: An array that contains the kernel stride for each spatial dimension.
- `bias`: The bias.
- `padding`: An enumeration that specifies that the operation computes the padding from   the input and output shapes. If you specify  , pass twice the number of spatial dimensions.
- `dilations`: An array that contains the kernel dilation for each spatial dimension.
- `groupCount`: The number of convolution groups. Pass   to specify non-grouped   convolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/conv(weight:strides:bias:padding:dilations:groupcount:))*