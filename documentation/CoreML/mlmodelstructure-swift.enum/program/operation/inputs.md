# inputs

**Framework**: Core ML  
**Kind**: property

The arguments to the Operation.

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
let inputs: [String : MLModelStructure.Program.Argument]
```

## See Also

- [let blocks: [MLModelStructure.Program.Block]](mlmodelstructure-swift.enum/program/operation/blocks.md)
  Nested blocks for loops and conditionals, e.g., a conditional block will have two entries here.
- [let operatorName: String](mlmodelstructure-swift.enum/program/operation/operatorname.md)
  The name of the operator, e.g., “conv”, “pool”, “softmax”, etc.
- [let outputs: [MLModelStructure.Program.NamedValueType]](mlmodelstructure-swift.enum/program/operation/outputs.md)
  The outputs of the Operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum/program/operation/inputs)*