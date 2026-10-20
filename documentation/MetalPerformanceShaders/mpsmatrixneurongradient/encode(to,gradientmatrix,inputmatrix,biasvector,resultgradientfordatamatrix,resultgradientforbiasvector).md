# encode(to:gradientMatrix:inputMatrix:biasVector:resultGradientForDataMatrix:resultGradientForBiasVector:)

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
func encode(to commandBuffer: any MTLCommandBuffer, gradientMatrix: MPSMatrix, inputMatrix: MPSMatrix, biasVector: MPSVector?, resultGradientForDataMatrix: MPSMatrix, resultGradientForBiasVector: MPSVector?)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer gradientMatrix:(MPSMatrix *) gradientMatrix inputMatrix:(MPSMatrix *) inputMatrix biasVector:(MPSVector *) biasVector resultGradientForDataMatrix:(MPSMatrix *) resultGradientForDataMatrix resultGradientForBiasVector:(MPSVector *) resultGradientForBiasVector;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixneurongradient/encode(to:gradientmatrix:inputmatrix:biasvector:resultgradientfordatamatrix:resultgradientforbiasvector:))*