# MPSRNNMatrixTrainingLayer

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A layer for training recurrent neural networks on Metal Performance Shaders matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNMatrixTrainingLayer
```

```objc
@interface MPSRNNMatrixTrainingLayer : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsrnnmatrixtraininglayer/init%28coder,device%29.md)
- [init(device: any MTLDevice, rnnDescriptor: MPSRNNDescriptor, trainableWeights: NSMutableArray)](./mpsrnnmatrixtraininglayer/init%28device,rnndescriptor,trainableweights%29.md)
### Instance Properties
- [var accumulateWeightGradients: Bool](./mpsrnnmatrixtraininglayer/accumulateweightgradients.md)
- [var inputFeatureChannels: Int](./mpsrnnmatrixtraininglayer/inputfeaturechannels.md)
- [var outputFeatureChannels: Int](./mpsrnnmatrixtraininglayer/outputfeaturechannels.md)
- [var recurrentOutputIsTemporary: Bool](./mpsrnnmatrixtraininglayer/recurrentoutputistemporary.md)
- [var storeAllIntermediateStates: Bool](./mpsrnnmatrixtraininglayer/storeallintermediatestates.md)
- [var trainingStateIsTemporary: Bool](./mpsrnnmatrixtraininglayer/trainingstateistemporary.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsrnnmatrixtraininglayer/copy%28with,device%29.md)
- [func createTemporaryWeightGradientMatrices(NSMutableArray, dataType: MPSDataType, commandBuffer: any MTLCommandBuffer)](./mpsrnnmatrixtraininglayer/createtemporaryweightgradientmatrices%28_,datatype,commandbuffer%29.md)
- [func createWeightGradientMatrices(NSMutableArray, dataType: MPSDataType)](./mpsrnnmatrixtraininglayer/createweightgradientmatrices%28_,datatype%29.md)
- [func createWeightMatrices(NSMutableArray)](./mpsrnnmatrixtraininglayer/createweightmatrices%28_%29.md)
- [func encodeCopyWeights(commandBuffer: any MTLCommandBuffer, weights: [MPSMatrix], matrixId: MPSRNNMatrixId, matrix: MPSMatrix, copyFromWeightsToMatrix: Bool, matrixOffset: MTLOrigin)](./mpsrnnmatrixtraininglayer/encodecopyweights%28commandbuffer,weights,matrixid,matrix,copyfromweightstomatrix,matrixoffset%29.md)
- [func encodeForwardSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], trainingStates: NSMutableArray, weights: [MPSMatrix])](./mpsrnnmatrixtraininglayer/encodeforwardsequence%28commandbuffer,sourcematrices,destinationmatrices,trainingstates,weights%29.md)
- [func encodeForwardSequence(commandBuffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationMatrices: [MPSMatrix], destinationOffsets: UnsafeMutablePointer<Int>?, trainingStates: NSMutableArray, recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?, weights: [MPSMatrix])](./mpsrnnmatrixtraininglayer/encodeforwardsequence%28commandbuffer,sourcematrices,sourceoffsets,destinationmatrices,destinationoffsets,trainingstates,recurrentinputstate,recurrentoutputstates,weights%29.md)
- [func encodeGradientSequence(commandBuffer: any MTLCommandBuffer, forwardSources: [MPSMatrix], forwardSourceOffsets: UnsafeMutablePointer<Int>?, sourceGradients: [MPSMatrix], sourceOffsets: UnsafeMutablePointer<Int>?, destinationGradients: [MPSMatrix]?, destinationOffsets: UnsafeMutablePointer<Int>?, weightGradients: [MPSMatrix]?, trainingStates: [MPSRNNMatrixTrainingState], recurrentInputState: MPSRNNRecurrentMatrixState?, recurrentOutputStates: NSMutableArray?, weights: [MPSMatrix])](./mpsrnnmatrixtraininglayer/encodegradientsequence%28commandbuffer,forwardsources,forwardsourceoffsets,sourcegradients,sourceoffsets,destinationgradients,destinationoffsets,weightgradients,trainingstates,recurrentinputstate,recurrentoutputstates,weights%29.md)
- [func encodeGradientSequence(commandBuffer: any MTLCommandBuffer, forwardSources: [MPSMatrix], sourceGradients: [MPSMatrix], destinationGradients: [MPSMatrix]?, weightGradients: [MPSMatrix]?, trainingStates: [MPSRNNMatrixTrainingState], weights: [MPSMatrix])](./mpsrnnmatrixtraininglayer/encodegradientsequence%28commandbuffer,forwardsources,sourcegradients,destinationgradients,weightgradients,trainingstates,weights%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Recurrent Neural Networks
- [class MPSRNNImageInferenceLayer](./mpsrnnimageinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders images.
- [class MPSRNNMatrixInferenceLayer](./mpsrnnmatrixinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders matrices.
- [class MPSRNNSingleGateDescriptor](./mpsrnnsinglegatedescriptor.md)
  A description of a simple recurrent block or layer.
- [class MPSGRUDescriptor](./mpsgrudescriptor.md)
  A description of a gated recurrent unit block or layer.
- [class MPSLSTMDescriptor](./mpslstmdescriptor.md)
  A description of a long short-term memory block or layer.
- [enum MPSRNNSequenceDirection](./mpsrnnsequencedirection.md)
  Directions that a sequence of inputs can be processed by a recurrent neural network layer.
- [class MPSRNNMatrixTrainingState](./mpsrnnmatrixtrainingstate.md)
  A class that holds data from a forward pass to be used in a backward pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixtraininglayer)*