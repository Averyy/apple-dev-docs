# encodeForWeightsAndBias(to:gradientMatrix:inputMatrix:resultGradientForWeightMatrix:resultGradientForBiasVector:)

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
func encodeForWeightsAndBias(to commandBuffer: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, resultGradientForWeightMatrix: MPSMatrix, resultGradientForBiasVector: MPSVector?)
```

```objc
- (void) encodeGradientForWeightsAndBiasToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer gradientMatrix:(const MPSMatrix *) gradientMatrix inputMatrix:(const MPSMatrix *) inputMatrix resultGradientForWeightMatrix:(MPSMatrix *) resultGradientForWeightMatrix resultGradientForBiasVector:(MPSVector *) resultGradientForBiasVector;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfullyconnectedgradient/encodeforweightsandbias(to:gradientmatrix:inputmatrix:resultgradientforweightmatrix:resultgradientforbiasvector:))*