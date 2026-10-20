# init(weights:biases:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
init(weights: any MTLBuffer, biases: (any MTLBuffer)?)
```

```objc
- (instancetype) initWithWeights:(id<MTLBuffer>) weights biases:(id<MTLBuffer>) biases;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionweightsandbiasesstate/init(weights:biases:))*