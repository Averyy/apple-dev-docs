# init(i_desc:o_desc:rate:seed:control:)

**Framework**: Accelerate  
**Kind**: init

Returns a new dropout layer parameters structure from the specified parameters.

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
init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, rate: Float, seed: UInt32, control: UInt8)
```

#### Discussion

> ❗ **Important**:  Dropout layers only support arrays with a data type of `float`. The input shape must be equal to the output shape.

## Parameters

- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `rate`: The probability that the layer drops out an element or a group of elements.
- `seed`: The seed for the random number generator that the layer ignores if zero.
- `control`: An 8-bit bit mask that indicates the dimension of the grouping of the dropout decision.

## See Also

- [init()](bnnslayerparametersdropout/init.md)
  Returns a new dropout layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersdropout/init(i_desc:o_desc:rate:seed:control:))*