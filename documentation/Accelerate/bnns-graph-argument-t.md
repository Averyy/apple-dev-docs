# bnns_graph_argument_t

**Framework**: Accelerate  
**Kind**: struct

Describes data associated with an input or output argument

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct bnns_graph_argument_t
```

#### Overview

Exactly one of descriptor or data_ptr should be set based on the configuration specified with `BNNSGraphContextSetArgumentType()`

## Topics

### Initializers
- [init()](bnns_graph_argument_t/init.md)
### Instance Properties
- [var data_ptr: UnsafeMutableRawPointer?](bnns_graph_argument_t/data_ptr-89cqn.md)
- [var data_ptr_size: Int](bnns_graph_argument_t/data_ptr_size.md)
  size in bytes of `data_ptr`, if set
- [var descriptor: UnsafeMutablePointer<BNNSNDArrayDescriptor>?](bnns_graph_argument_t/descriptor-8d2bd.md)
- [var tensor: UnsafeMutablePointer<BNNSTensor>?](bnns_graph_argument_t/tensor-6l2lt.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct BNNSDataType](bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSSparsityParameters](bnnssparsityparameters.md)
- [struct BNNSSparsityType](bnnssparsitytype.md)
- [struct BNNSTargetSystem](bnnstargetsystem.md)
- [struct BNNSImageStackDescriptor](bnnsimagestackdescriptor.md)
- [struct BNNSVectorDescriptor](bnnsvectordescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_argument_t)*