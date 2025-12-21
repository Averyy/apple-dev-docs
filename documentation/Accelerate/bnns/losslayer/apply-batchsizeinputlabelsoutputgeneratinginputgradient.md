# apply(batchSize:input:labels:output:generatingInputGradient:)

**Framework**: Accelerate  
**Kind**: method

Applies the layer to a set of input objects, writing the result to a set of output objects.

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
func apply(batchSize: Int, input: BNNSNDArrayDescriptor, labels: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, generatingInputGradient inputGradient: BNNSNDArrayDescriptor) throws
```

## Parameters

- `batchSize`: The number of input-output pairs.
- `input`: The descriptor of the input.
- `labels`: The descriptor of the labels.
- `output`: The descriptor of the output.
- `inputGradient`: The descriptor of the input gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/losslayer/apply(batchsize:input:labels:output:generatinginputgradient:))*