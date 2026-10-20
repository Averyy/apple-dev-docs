# encode(commandBuffer:inputGradientVector:inputValuesVector:inputMomentumVector:inputVelocityVector:maximumVelocityVector:resultValuesVector:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, inputGradientVector: MPSVector, inputValuesVector: MPSVector, inputMomentumVector: MPSVector, inputVelocityVector: MPSVector, maximumVelocityVector: MPSVector?, resultValuesVector: MPSVector)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer inputGradientVector:(MPSVector *) inputGradientVector inputValuesVector:(MPSVector *) inputValuesVector inputMomentumVector:(MPSVector *) inputMomentumVector inputVelocityVector:(MPSVector *) inputVelocityVector maximumVelocityVector:(MPSVector *) maximumVelocityVector resultValuesVector:(MPSVector *) resultValuesVector;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizeradam/encode(commandbuffer:inputgradientvector:inputvaluesvector:inputmomentumvector:inputvelocityvector:maximumvelocityvector:resultvaluesvector:))*