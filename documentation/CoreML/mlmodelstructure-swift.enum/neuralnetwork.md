# MLModelStructure.NeuralNetwork

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

A struct representing the structure of a NeuralNetwork model..

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
struct NeuralNetwork
```

## Topics

### Accessing the layers
- [let layers: [MLModelStructure.NeuralNetwork.Layer]](./neuralnetwork/layers.md)
  The topologically sorted layers in the NeuralNetwork.
- [MLModelStructure.NeuralNetwork.Layer](./neuralnetwork/layer.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Model structures
- [case neuralNetwork(MLModelStructure.NeuralNetwork)](./neuralnetwork%28_%29.md)
  Represents a NeuralNetwork model, the associated value is the structure of the NeuralNetwork.
- [case pipeline(MLModelStructure.Pipeline)](./pipeline%28_%29.md)
  Represents a Pipeline model, the associated value is the structure of the Pipeline.
- [MLModelStructure.Pipeline](./pipeline.md)
  A struct representing the structure of a Pipeline model..
- [case program(MLModelStructure.Program)](./program%28_%29.md)
  Represents a MLProgram model. the associated value is the structure of the Program.
- [MLModelStructure.Program](./program.md)
  A struct representing the structure of an ML Program model.
- [MLModelStructure.unsupported](./unsupported.md)
  Represents an unsupported model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum/neuralnetwork)*