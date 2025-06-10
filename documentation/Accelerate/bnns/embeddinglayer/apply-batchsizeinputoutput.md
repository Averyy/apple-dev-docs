# apply(batchSize:input:output:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer to a set of input objects, writing the result to a set of output objects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- tvOS 15.0+

## Declaration

```swift
func apply(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.

## See Also

- [func applyBackward(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingWeightsGradient: BNNSNDArrayDescriptor) throws](bnns/embeddinglayer/applybackward(batchsize:input:output:outputgradient:generatingweightsgradient:).md)
  Applies the layer backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/embeddinglayer/apply(batchsize:input:output:))*