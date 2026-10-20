# encode(to:gradientMatrix:forwardOutputMatrix:resultMatrix:)

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
func encode(to commandBuffer: any MTLCommandBuffer, gradientMatrix: MPSMatrix, forwardOutputMatrix: MPSMatrix, resultMatrix: MPSMatrix)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer gradientMatrix:(MPSMatrix *) gradientMatrix forwardOutputMatrix:(MPSMatrix *) forwardOutputMatrix resultMatrix:(MPSMatrix *) resultMatrix;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsoftmaxgradient/encode(to:gradientmatrix:forwardoutputmatrix:resultmatrix:))*