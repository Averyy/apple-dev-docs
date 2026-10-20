# MPSRNNSequenceDirection

**Framework**: Metal Performance Shaders  
**Kind**: enum  
**Role**: Enumeration

Directions that a sequence of inputs can be processed by a recurrent neural network layer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum MPSRNNSequenceDirection
```

```c
enum MPSRNNSequenceDirection : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSRNNSequenceDirection.backward](./mpsrnnsequencedirection/backward.md)
- [MPSRNNSequenceDirection.forward](./mpsrnnsequencedirection/forward.md)
### Initializers
- [init?(rawValue: UInt)](./mpsrnnsequencedirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [class MPSRNNMatrixTrainingLayer](./mpsrnnmatrixtraininglayer.md)
  A layer for training recurrent neural networks on Metal Performance Shaders matrices.
- [class MPSRNNMatrixTrainingState](./mpsrnnmatrixtrainingstate.md)
  A class that holds data from a forward pass to be used in a backward pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnsequencedirection)*