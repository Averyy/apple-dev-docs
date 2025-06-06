# control

**Framework**: Accelerate  
**Kind**: property

An 8-bit bit mask that indicates the dimension of the grouping of the dropout decision.

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
var control: UInt8
```

## See Also

- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersdropout/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersdropout/o_desc.md)
  The descriptor of the output.
- [var rate: Float](bnnslayerparametersdropout/rate.md)
  The probability that the layer drops out an element or a group of elements.
- [var seed: UInt32](bnnslayerparametersdropout/seed.md)
  The seed for the random number generator which is ignored if zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersdropout/control)*