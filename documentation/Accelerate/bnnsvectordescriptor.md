# BNNSVectorDescriptor

**Framework**: Accelerate  
**Kind**: struct

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct BNNSVectorDescriptor
```

#### Overview

Represents a vector of dimension size. Each vector element is a scalar value, stored using the type specified in data_type.

Component V(i) at index i is stored in data[i], with i=0..size-1.

Int types are converted to floating point using float Y = DATA_SCALE * (float)X + DATA_BIAS, and back to integer using Int X = convert_and_saturate(Y / DATA_SCALE - DATA_BIAS)

## Topics

### Initializers
- [init()](bnnsvectordescriptor/init.md)
- [init(size: Int, data_type: BNNSDataType)](bnnsvectordescriptor/init(size:data_type:).md)
- [init(size: Int, data_type: BNNSDataType, data_scale: Float, data_bias: Float)](bnnsvectordescriptor/init(size:data_type:data_scale:data_bias:).md)
### Instance Properties
- [var data_bias: Float](bnnsvectordescriptor/data_bias.md)
- [var data_scale: Float](bnnsvectordescriptor/data_scale.md)
- [var data_type: BNNSDataType](bnnsvectordescriptor/data_type.md)
- [var size: Int](bnnsvectordescriptor/size.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct BNNSDataType](bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSSparsityParameters](bnnssparsityparameters.md)
- [struct BNNSSparsityType](bnnssparsitytype.md)
- [struct BNNSTargetSystem](bnnstargetsystem.md)
- [struct bnns_graph_argument_t](bnns_graph_argument_t.md)
  Describes data associated with an input or output argument
- [struct BNNSImageStackDescriptor](bnnsimagestackdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsvectordescriptor)*