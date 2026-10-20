# encode(commandBuffer:sourceMatrix:rightHandSideMatrix:solutionMatrix:)

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
func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, rightHandSideMatrix: MPSMatrix, solutionMatrix: MPSMatrix)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceMatrix:(MPSMatrix *) sourceMatrix rightHandSideMatrix:(MPSMatrix *) rightHandSideMatrix solutionMatrix:(MPSMatrix *) solutionMatrix;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsolvecholesky/encode(commandbuffer:sourcematrix:righthandsidematrix:solutionmatrix:))*