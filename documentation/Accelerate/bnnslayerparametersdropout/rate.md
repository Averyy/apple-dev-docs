# rate

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The probability that the layer drops out an element or a group of elements.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
var rate: Float
```

```c
float rate;
```

## See Also

### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.
- [var seed: UInt32](./seed.md)
  The seed for the random number generator which is ignored if zero.
- [var control: UInt8](./control.md)
  An 8-bit bit mask that indicates the dimension of the grouping of the dropout decision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersdropout/rate)*