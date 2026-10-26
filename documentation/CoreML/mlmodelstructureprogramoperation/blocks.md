# blocks

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

Nested blocks for loops and conditionals, e.g., a conditional block will have two entries here.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<MLModelStructureProgramBlock *> * blocks;
```

## See Also

### Accessing the program operation properties
- [inputs](./inputs.md)
  The arguments to the Operation.
- [operatorName](./operatorname.md)
  The name of the operator, e.g., “conv”, “pool”, “softmax”, etc.
- [outputs](./outputs.md)
  The outputs of the Operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructureprogramoperation/blocks)*