# encode(commandBuffer:sourceMatrix:resultMatrix:pivotIndices:info:)

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
func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, resultMatrix: MPSMatrix, pivotIndices: MPSMatrix, info status: (any MTLBuffer)?)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceMatrix:(MPSMatrix *) sourceMatrix resultMatrix:(MPSMatrix *) resultMatrix pivotIndices:(MPSMatrix *) pivotIndices status:(id<MTLBuffer>) status;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdecompositionlu/encode(commandbuffer:sourcematrix:resultmatrix:pivotindices:info:))*