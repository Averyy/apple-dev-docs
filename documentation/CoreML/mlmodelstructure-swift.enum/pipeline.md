# MLModelStructure.Pipeline

**Framework**: Core ML  
**Kind**: struct

A struct representing the structure of a Pipeline model..

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
struct Pipeline
```

## Topics

### Accessing the pipeline model
- [let subModelNames: [String]](mlmodelstructure-swift.enum/pipeline/submodelnames.md)
  The names of the sub models in the Pipeline.
- [let subModels: [MLModelStructure]](mlmodelstructure-swift.enum/pipeline/submodels.md)
  The structure of sub models in the Pipeline.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case neuralNetwork(MLModelStructure.NeuralNetwork)](mlmodelstructure-swift.enum/neuralnetwork(_:).md)
  Represents a NeuralNetwork model, the associated value is the structure of the NeuralNetwork.
- [MLModelStructure.NeuralNetwork](mlmodelstructure-swift.enum/neuralnetwork.md)
  A struct representing the structure of a NeuralNetwork model..
- [case pipeline(MLModelStructure.Pipeline)](mlmodelstructure-swift.enum/pipeline(_:).md)
  Represents a Pipeline model, the associated value is the structure of the Pipeline.
- [case program(MLModelStructure.Program)](mlmodelstructure-swift.enum/program(_:).md)
  Represents a MLProgram model. the associated value is the structure of the Program.
- [MLModelStructure.Program](mlmodelstructure-swift.enum/program.md)
  A struct representing the structure of an ML Program model.
- [MLModelStructure.unsupported](mlmodelstructure-swift.enum/unsupported.md)
  Represents an unsupported model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum/pipeline)*