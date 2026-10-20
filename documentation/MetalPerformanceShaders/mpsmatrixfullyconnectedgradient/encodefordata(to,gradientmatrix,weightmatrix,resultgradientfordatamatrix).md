# encodeForData(to:gradientMatrix:weightMatrix:resultGradientForDataMatrix:)

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
func encodeForData(to commandBuffer: any MTLCommandBuffer, gradientMatrix: MPSMatrix, weightMatrix: MPSMatrix, resultGradientForDataMatrix: MPSMatrix)
```

```objc
- (void) encodeGradientForDataToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer gradientMatrix:(const MPSMatrix *) gradientMatrix weightMatrix:(const MPSMatrix *) weightMatrix resultGradientForDataMatrix:(MPSMatrix *) resultGradientForDataMatrix;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfullyconnectedgradient/encodefordata(to:gradientmatrix:weightmatrix:resultgradientfordatamatrix:))*