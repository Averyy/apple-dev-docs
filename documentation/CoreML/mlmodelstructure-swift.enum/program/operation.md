# MLModelStructure.Program.Operation

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

A struct representing an Operation in the Program.

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
struct Operation
```

## Topics

### Accessing the properties
- [let blocks: [MLModelStructure.Program.Block]](./operation/blocks.md)
  Nested blocks for loops and conditionals, e.g., a conditional block will have two entries here.
- [let inputs: [String : MLModelStructure.Program.Argument]](./operation/inputs.md)
  The arguments to the Operation.
- [let operatorName: String](./operation/operatorname.md)
  The name of the operator, e.g., “conv”, “pool”, “softmax”, etc.
- [let outputs: [MLModelStructure.Program.NamedValueType]](./operation/outputs.md)
  The outputs of the Operation.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the program types
- [MLModelStructure.Program.Argument](./argument.md)
  A struct representing an argument in the Program.
- [MLModelStructure.Program.Block](./block.md)
  A struct representing a block in the Program.
- [MLModelStructure.Program.Function](./function.md)
  A struct representing a function in the Program.
- [MLModelStructure.Program.NamedValueType](./namedvaluetype.md)
  A struct representing a named type in a Program.
- [MLModelStructure.Program.Value](./value.md)
  A struct representing the value of a variable in the Program.
- [MLModelStructure.Program.ValueType](./valuetype.md)
  A struct representing the type of a variable in the Program.
- [MLModelStructure.Program.Binding](./binding.md)
  An enum representing a binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum/program/operation)*