# BNNSVectorDescriptor

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 10.0+ - Deprecated in 14.0
- iPadOS 10.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.12+ - Deprecated in 11.0
- tvOS 10.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.0

> **Deprecated**: BNNS switched to new Layer Parameters data structures

## Declaration

```swift
struct BNNSVectorDescriptor
```

```c
typedef struct { ... } BNNSVectorDescriptor;
```

#### Overview

Vector format descriptor (DEPRECATED, Use BNNSNDArrayDescriptor)

Represents a vector of dimension size. Each vector element is a scalar value, stored using the type specified in data_type.

Component V(i) at index i is stored in data[i], with i=0..size-1.

Int types are converted to floating point using float Y = DATA_SCALE * (float)X + DATA_BIAS, and back to integer using Int X = convert_and_saturate(Y / DATA_SCALE - DATA_BIAS)

## Topics

### Initializers
- [init()](./bnnsvectordescriptor/init%28%29.md)
- [init(size: Int, data_type: BNNSDataType)](./bnnsvectordescriptor/init%28size,data_type%29.md)
- [init(size: Int, data_type: BNNSDataType, data_scale: Float, data_bias: Float)](./bnnsvectordescriptor/init%28size,data_type,data_scale,data_bias%29.md)
### Instance Properties
- [var data_bias: Float](./bnnsvectordescriptor/data_bias.md)
- [var data_scale: Float](./bnnsvectordescriptor/data_scale.md)
- [var data_type: BNNSDataType](./bnnsvectordescriptor/data_type.md)
- [var size: Int](./bnnsvectordescriptor/size.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Structures
- [struct BNNSDataType](./bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSSparsityParameters](./bnnssparsityparameters.md)
- [struct BNNSSparsityType](./bnnssparsitytype.md)
- [struct BNNSTargetSystem](./bnnstargetsystem.md)
- [struct bnns_graph_argument_t](./bnns_graph_argument_t.md)
  Describes data associated with an input or output argument
- [struct BNNSImageStackDescriptor](./bnnsimagestackdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsvectordescriptor)*