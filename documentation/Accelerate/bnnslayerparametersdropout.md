# BNNSLayerParametersDropout

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a dropout layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct BNNSLayerParametersDropout
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, rate: Float, seed: UInt32, control: UInt8)](bnnslayerparametersdropout/init(i_desc:o_desc:rate:seed:control:).md)
  Returns a new dropout layer parameters structure from the specified parameters.
- [init()](bnnslayerparametersdropout/init.md)
  Returns a new dropout layer parameters structure.
### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersdropout/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersdropout/o_desc.md)
  The descriptor of the output.
- [var rate: Float](bnnslayerparametersdropout/rate.md)
  The probability that the layer drops out an element or a group of elements.
- [var seed: UInt32](bnnslayerparametersdropout/seed.md)
  The seed for the random number generator which is ignored if zero.
- [var control: UInt8](bnnslayerparametersdropout/control.md)
  An 8-bit bit mask that indicates the dimension of the grouping of the dropout decision.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class DropoutLayer](bnns/dropoutlayer.md)
  A layer object that wraps a dropout filter and manages its deinitialization.
- [func BNNSFilterCreateLayerDropout(UnsafePointer<BNNSLayerParametersDropout>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerdropout(_:_:).md)
  Returns a new dropout layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersdropout)*