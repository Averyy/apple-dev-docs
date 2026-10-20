# encode(commandBuffer:sourceMatrix:resultMatrix:status:)

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
func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, resultMatrix: MPSMatrix, status: (any MTLBuffer)?)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceMatrix:(MPSMatrix *) sourceMatrix resultMatrix:(MPSMatrix *) resultMatrix status:(id<MTLBuffer>) status;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdecompositioncholesky/encode(commandbuffer:sourcematrix:resultmatrix:status:))*