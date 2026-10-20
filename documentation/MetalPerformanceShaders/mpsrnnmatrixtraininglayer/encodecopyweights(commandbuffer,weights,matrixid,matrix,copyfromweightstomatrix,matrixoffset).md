# encodeCopyWeights(commandBuffer:weights:matrixId:matrix:copyFromWeightsToMatrix:matrixOffset:)

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
func encodeCopyWeights(commandBuffer: any MTLCommandBuffer, weights: [MPSMatrix], matrixId: MPSRNNMatrixId, matrix: MPSMatrix, copyFromWeightsToMatrix: Bool, matrixOffset: MTLOrigin)
```

```objc
- (void) encodeCopyWeightsToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer weights:(NSArray<MPSMatrix *> *) weights matrixId:(MPSRNNMatrixId) matrixId matrix:(MPSMatrix *) matrix copyFromWeightsToMatrix:(BOOL) copyFromWeightsToMatrix matrixOffset:(MTLOrigin) matrixOffset;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixtraininglayer/encodecopyweights(commandbuffer:weights:matrixid:matrix:copyfromweightstomatrix:matrixoffset:))*