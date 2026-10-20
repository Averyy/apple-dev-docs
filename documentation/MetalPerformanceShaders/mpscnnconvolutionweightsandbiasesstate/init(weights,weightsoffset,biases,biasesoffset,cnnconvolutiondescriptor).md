# init(weights:weightsOffset:biases:biasesOffset:cnnConvolutionDescriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(weights: any MTLBuffer, weightsOffset: Int, biases: (any MTLBuffer)?, biasesOffset: Int, cnnConvolutionDescriptor descriptor: MPSCNNConvolutionDescriptor)
```

```objc
- (instancetype) initWithWeights:(id<MTLBuffer>) weights weightsOffset:(NSUInteger) weightsOffset biases:(id<MTLBuffer>) biases biasesOffset:(NSUInteger) biasesOffset cnnConvolutionDescriptor:(MPSCNNConvolutionDescriptor *) descriptor;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionweightsandbiasesstate/init(weights:weightsoffset:biases:biasesoffset:cnnconvolutiondescriptor:))*