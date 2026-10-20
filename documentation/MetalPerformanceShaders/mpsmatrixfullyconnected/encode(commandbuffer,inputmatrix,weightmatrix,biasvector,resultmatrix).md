# encode(commandBuffer:inputMatrix:weightMatrix:biasVector:resultMatrix:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, weightMatrix: MPSMatrix, biasVector: MPSVector?, resultMatrix: MPSMatrix)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer inputMatrix:(MPSMatrix *) inputMatrix weightMatrix:(MPSMatrix *) weightMatrix biasVector:(MPSVector *) biasVector resultMatrix:(MPSMatrix *) resultMatrix;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfullyconnected/encode(commandbuffer:inputmatrix:weightmatrix:biasvector:resultmatrix:))*