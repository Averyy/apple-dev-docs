# applyBackward(batchSize:inputA:inputB:output:outputGradient:generatingInputAGradient:generatingInputBGradient:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer backward to generate input gradients.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient inputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient inputBGradient: BNNSNDArrayDescriptor) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `inputA`: The descriptor of matrix  .
- `inputB`: The descriptor of matrix  .
- `output`: The descriptor of the output.
- `outputGradient`: The descriptor of the output gradient.
- `inputAGradient`: The descriptor of the matrix   gradient.
- `inputBGradient`: The descriptor of the matrix   gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/broadcastmatrixmultiplylayer/applybackward(batchsize:inputa:inputb:output:outputgradient:generatinginputagradient:generatinginputbgradient:))*