# encodeForwardSequence(commandBuffer:sourceMatrices:destinationMatrices:trainingStates:weights:)

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
func encodeForwardSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], trainingStates: NSMutableArray, weights: [MPSMatrix])
```

```objc
- (void) encodeForwardSequenceToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceMatrices:(NSArray<MPSMatrix *> *) sourceMatrices destinationMatrices:(NSArray<MPSMatrix *> *) destinationMatrices trainingStates:(NSMutableArray<MPSRNNMatrixTrainingState *> *) trainingStates weights:(NSArray<MPSMatrix *> *) weights;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixtraininglayer/encodeforwardsequence(commandbuffer:sourcematrices:destinationmatrices:trainingstates:weights:))*