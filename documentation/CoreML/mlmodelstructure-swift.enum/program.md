# MLModelStructure.Program

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

A struct representing the structure of an ML Program model.

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
struct Program
```

## Topics

### Accessing the program functions
- [let functions: [String : MLModelStructure.Program.Function]](./program/functions.md)
  The functions in the program.
### Getting the program types
- [MLModelStructure.Program.Argument](./program/argument.md)
  A struct representing an argument in the Program.
- [MLModelStructure.Program.Block](./program/block.md)
  A struct representing a block in the Program.
- [MLModelStructure.Program.Function](./program/function.md)
  A struct representing a function in the Program.
- [MLModelStructure.Program.NamedValueType](./program/namedvaluetype.md)
  A struct representing a named type in a Program.
- [MLModelStructure.Program.Operation](./program/operation.md)
  A struct representing an Operation in the Program.
- [MLModelStructure.Program.Value](./program/value.md)
  A struct representing the value of a variable in the Program.
- [MLModelStructure.Program.ValueType](./program/valuetype.md)
  A struct representing the type of a variable in the Program.
- [MLModelStructure.Program.Binding](./program/binding.md)
  An enum representing a binding.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Model structures
- [case neuralNetwork(MLModelStructure.NeuralNetwork)](./neuralnetwork%28_%29.md)
  Represents a NeuralNetwork model, the associated value is the structure of the NeuralNetwork.
- [MLModelStructure.NeuralNetwork](./neuralnetwork.md)
  A struct representing the structure of a NeuralNetwork model..
- [case pipeline(MLModelStructure.Pipeline)](./pipeline%28_%29.md)
  Represents a Pipeline model, the associated value is the structure of the Pipeline.
- [MLModelStructure.Pipeline](./pipeline.md)
  A struct representing the structure of a Pipeline model..
- [case program(MLModelStructure.Program)](./program%28_%29.md)
  Represents a MLProgram model. the associated value is the structure of the Program.
- [MLModelStructure.unsupported](./unsupported.md)
  Represents an unsupported model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum/program)*