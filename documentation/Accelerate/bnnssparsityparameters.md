# BNNSSparsityParameters

**Framework**: Accelerate  
**Kind**: struct

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct BNNSSparsityParameters
```

#### Overview

Parameters to describe sparsity attributes

use this data structure as hint for BNNSNDArrayFullyConnectedSparsify for BNNSSparsityTypeUnstructured, sparsity_ratio is numerator / denominator

## Topics

### Initializers
- [init()](bnnssparsityparameters/init.md)
- [init(flags: UInt64, sparsity_ratio: (UInt32, UInt32), sparsity_type: BNNSSparsityType, target_system: BNNSTargetSystem)](bnnssparsityparameters/init(flags:sparsity_ratio:sparsity_type:target_system:).md)
### Instance Properties
- [var flags: UInt64](bnnssparsityparameters/flags.md)
- [var sparsity_ratio: (UInt32, UInt32)](bnnssparsityparameters/sparsity_ratio.md)
- [var sparsity_type: BNNSSparsityType](bnnssparsityparameters/sparsity_type.md)
- [var target_system: BNNSTargetSystem](bnnssparsityparameters/target_system.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct BNNSDataType](bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSSparsityType](bnnssparsitytype.md)
- [struct BNNSTargetSystem](bnnstargetsystem.md)
- [struct bnns_graph_argument_t](bnns_graph_argument_t.md)
  Describes data associated with an input or output argument
- [struct BNNSImageStackDescriptor](bnnsimagestackdescriptor.md)
- [struct BNNSVectorDescriptor](bnnsvectordescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnssparsityparameters)*