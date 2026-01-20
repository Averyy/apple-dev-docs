# MPSRNNImageInferenceLayer

**Framework**: Metal Performance Shaders  
**Kind**: class

A recurrent neural network layer for inference on Metal Performance Shaders images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNImageInferenceLayer
```

#### Overview

The [`MPSRNNImageInferenceLayer`](mpsrnnimageinferencelayer.md) specifies a recurrent neural network layer for inference on [`MPSImage`](mpsimage.md) objects. Two types of recurrent layers are supported:

- [`MPSRNNImageInferenceLayer`](mpsrnnimageinferencelayer.md)—Operates with convolutions on images.
- [`MPSRNNMatrixInferenceLayer`](mpsrnnmatrixinferencelayer.md)—Operates on matrices.

You can use [`MPSRNNImageInferenceLayer`](mpsrnnimageinferencelayer.md) to implement the latter by using 1 x 1 images, but due to image size restrictions and performance, [`MPSRNNMatrixInferenceLayer`](mpsrnnmatrixinferencelayer.md) is the better choice for linear recurrent layers.

[`MPSRNNImageInferenceLayer`](mpsrnnimageinferencelayer.md) is initialized using either of the following:

- A single [`MPSRNNDescriptor`](mpsrnndescriptor.md) instance, which further specifies the recurrent network layer.
- An array of [`MPSRNNDescriptor`](mpsrnndescriptor.md) instances, which specifies a stack of recurrent layers that can operate in parallel a subset of the inputs in a sequence of inputs and recurrent outputs.

Stacks with bidirectionally traversing encode functions don’t support starting from a previous set of recurrent states. However, you can achieve this effect by defining two separate unidirectional stacks of layers, running the same input sequence on them separately (one forward and one backward), and ultimately combining the two result sequences.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsrnnimageinferencelayer/init(coder:device:).md)
- [init(device: any MTLDevice, rnnDescriptor: MPSRNNDescriptor)](mpsrnnimageinferencelayer/init(device:rnndescriptor:).md)
- [init(device: any MTLDevice, rnnDescriptors: [MPSRNNDescriptor])](mpsrnnimageinferencelayer/init(device:rnndescriptors:).md)
- [class MPSRNNDescriptor](mpsrnndescriptor.md)
  A description of a recursive neural network block or layer.
### Instance Properties
- [var bidirectionalCombineMode: MPSRNNBidirectionalCombineMode](mpsrnnimageinferencelayer/bidirectionalcombinemode.md)
- [enum MPSRNNBidirectionalCombineMode](mpsrnnbidirectionalcombinemode.md)
  Modes that define how two images or matrices are combined.
- [var numberOfLayers: Int](mpsrnnimageinferencelayer/numberoflayers.md)
- [var recurrentOutputIsTemporary: Bool](mpsrnnimageinferencelayer/recurrentoutputistemporary.md)
- [var storeAllIntermediateStates: Bool](mpsrnnimageinferencelayer/storeallintermediatestates.md)
- [var inputFeatureChannels: Int](mpsrnnimageinferencelayer/inputfeaturechannels.md)
- [var outputFeatureChannels: Int](mpsrnnimageinferencelayer/outputfeaturechannels.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsrnnimageinferencelayer/copy(with:device:).md)
- [func encodeBidirectionalSequence(commandBuffer: any MTLCommandBuffer, sourceSequence: [MPSImage], destinationForwardImages: [MPSImage], destinationBackwardImages: [MPSImage]?)](mpsrnnimageinferencelayer/encodebidirectionalsequence(commandbuffer:sourcesequence:destinationforwardimages:destinationbackwardimages:).md)
- [func encodeSequence(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationImages: [MPSImage], recurrentInputState: MPSRNNRecurrentImageState?, recurrentOutputStates: NSMutableArray?)](mpsrnnimageinferencelayer/encodesequence(commandbuffer:sourceimages:destinationimages:recurrentinputstate:recurrentoutputstates:).md)
- [class MPSRNNRecurrentImageState](mpsrnnrecurrentimagestate.md)
  A class that holds all the data that’s passed from one sequence iteration of the image-based recurrent neural network layer (stack) to the next.

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSRNNMatrixInferenceLayer](mpsrnnmatrixinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders matrices.
- [class MPSRNNSingleGateDescriptor](mpsrnnsinglegatedescriptor.md)
  A description of a simple recurrent block or layer.
- [class MPSGRUDescriptor](mpsgrudescriptor.md)
  A description of a gated recurrent unit block or layer.
- [class MPSLSTMDescriptor](mpslstmdescriptor.md)
  A description of a long short-term memory block or layer.
- [enum MPSRNNSequenceDirection](mpsrnnsequencedirection.md)
  Directions that a sequence of inputs can be processed by a recurrent neural network layer.
- [class MPSRNNMatrixTrainingLayer](mpsrnnmatrixtraininglayer.md)
  A layer for training recurrent neural networks on Metal Performance Shaders matrices.
- [class MPSRNNMatrixTrainingState](mpsrnnmatrixtrainingstate.md)
  A class that holds data from a forward pass to be used in a backward pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnimageinferencelayer)*