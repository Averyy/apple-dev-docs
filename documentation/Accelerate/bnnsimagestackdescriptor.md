# BNNSImageStackDescriptor

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
struct BNNSImageStackDescriptor
```

#### Overview

Image stack descriptor (DEPRECATED, Use BNNSNDArrayDescriptor)

An image stack is a sequence of images with the same width and height. Each image in the sequence is called a channel. For example, a RGB image will be stored as three separate channels. A pixel has only one scalar value, stored using the type described by data_type.

Pixel P(c,x,y) at position (x,y) in channel c is stored in data[x + row_stride * y + image_stride * c], with x=0..width-1, y=0..height-1, c=0..channels-1. row_stride ≥ width, image_stride ≥ row_stride * height.

Int types are converted to floating point using float Y = DATA_SCALE * (float)X + DATA_BIAS, and back to integer using Int X = convert_and_saturate(Y / DATA_SCALE - DATA_BIAS)

## Topics

### Initializers
- [init()](bnnsimagestackdescriptor/init.md)
- [init(width: Int, height: Int, channels: Int, row_stride: Int, image_stride: Int, data_type: BNNSDataType)](bnnsimagestackdescriptor/init(width:height:channels:row_stride:image_stride:data_type:).md)
- [init(width: Int, height: Int, channels: Int, row_stride: Int, image_stride: Int, data_type: BNNSDataType, data_scale: Float, data_bias: Float)](bnnsimagestackdescriptor/init(width:height:channels:row_stride:image_stride:data_type:data_scale:data_bias:).md)
### Instance Properties
- [var channels: Int](bnnsimagestackdescriptor/channels.md)
- [var data_bias: Float](bnnsimagestackdescriptor/data_bias.md)
- [var data_scale: Float](bnnsimagestackdescriptor/data_scale.md)
- [var data_type: BNNSDataType](bnnsimagestackdescriptor/data_type.md)
- [var height: Int](bnnsimagestackdescriptor/height.md)
- [var image_stride: Int](bnnsimagestackdescriptor/image_stride.md)
- [var row_stride: Int](bnnsimagestackdescriptor/row_stride.md)
- [var width: Int](bnnsimagestackdescriptor/width.md)

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
- [struct BNNSVectorDescriptor](bnnsvectordescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsimagestackdescriptor)*