# encode(commandBuffer:inputGradientVector:inputValuesVector:inputSumOfSquaresVector:resultValuesVector:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputSumOfSquaresVector: MPSVector, resultValuesVector: MPSVector)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer inputGradientVector:(MPSVector *) inputGradientVector inputValuesVector:(MPSVector *) inputValuesVector inputSumOfSquaresVector:(MPSVector *) inputSumOfSquaresVector resultValuesVector:(MPSVector *) resultValuesVector;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerrmsprop/encode(commandbuffer:inputgradientvector:inputvaluesvector:inputsumofsquaresvector:resultvaluesvector:))*