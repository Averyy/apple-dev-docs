# MLModelStructure.Program.Operation

**Framework**: Core ML  
**Kind**: struct

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
- [let blocks: [MLModelStructure.Program.Block]](mlmodelstructure-swift.enum/program/operation/blocks.md)
  Nested blocks for loops and conditionals, e.g., a conditional block will have two entries here.
- [let inputs: [String : MLModelStructure.Program.Argument]](mlmodelstructure-swift.enum/program/operation/inputs.md)
  The arguments to the Operation.
- [let operatorName: String](mlmodelstructure-swift.enum/program/operation/operatorname.md)
  The name of the operator, e.g., “conv”, “pool”, “softmax”, etc.
- [let outputs: [MLModelStructure.Program.NamedValueType]](mlmodelstructure-swift.enum/program/operation/outputs.md)
  The outputs of the Operation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLModelStructure.Program.Argument](mlmodelstructure-swift.enum/program/argument.md)
  A struct representing an argument in the Program.
- [MLModelStructure.Program.Block](mlmodelstructure-swift.enum/program/block.md)
  A struct representing a block in the Program.
- [MLModelStructure.Program.Function](mlmodelstructure-swift.enum/program/function.md)
  A struct representing a function in the Program.
- [MLModelStructure.Program.NamedValueType](mlmodelstructure-swift.enum/program/namedvaluetype.md)
  A struct representing a named type in a Program.
- [MLModelStructure.Program.Value](mlmodelstructure-swift.enum/program/value.md)
  A struct representing the value of a variable in the Program.
- [MLModelStructure.Program.ValueType](mlmodelstructure-swift.enum/program/valuetype.md)
  A struct representing the type of a variable in the Program.
- [MLModelStructure.Program.Binding](mlmodelstructure-swift.enum/program/binding.md)
  An enum representing a binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum/program/operation)*