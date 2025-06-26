# apply(batchSize:input:labels:output:weights:broadcastsWeights:generatingInputGradient:)

**Framework**: Accelerate  
**Kind**: method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
func apply(batchSize: Int, input: BNNSNDArrayDescriptor, labels: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, broadcastsWeights: Bool, generatingInputGradient inputGradient: BNNSNDArrayDescriptor) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/losslayer/apply(batchsize:input:labels:output:weights:broadcastsweights:generatinginputgradient:))*