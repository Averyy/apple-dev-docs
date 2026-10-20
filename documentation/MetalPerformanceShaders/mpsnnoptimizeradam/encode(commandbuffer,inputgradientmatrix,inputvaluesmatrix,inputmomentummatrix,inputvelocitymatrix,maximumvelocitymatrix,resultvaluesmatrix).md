# encode(commandBuffer:inputGradientMatrix:inputValuesMatrix:inputMomentumMatrix:inputVelocityMatrix:maximumVelocityMatrix:resultValuesMatrix:)

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
func encode(commandBuffer: any MTLCommandBuffer, inputGradientMatrix: MPSMatrix, inputValuesMatrix: MPSMatrix, inputMomentumMatrix: MPSMatrix, inputVelocityMatrix: MPSMatrix, maximumVelocityMatrix: MPSMatrix?, resultValuesMatrix: MPSMatrix)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer inputGradientMatrix:(MPSMatrix *) inputGradientMatrix inputValuesMatrix:(MPSMatrix *) inputValuesMatrix inputMomentumMatrix:(MPSMatrix *) inputMomentumMatrix inputVelocityMatrix:(MPSMatrix *) inputVelocityMatrix maximumVelocityMatrix:(MPSMatrix *) maximumVelocityMatrix resultValuesMatrix:(MPSMatrix *) resultValuesMatrix;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizeradam/encode(commandbuffer:inputgradientmatrix:inputvaluesmatrix:inputmomentummatrix:inputvelocitymatrix:maximumvelocitymatrix:resultvaluesmatrix:))*