# init(input:output:rate:seed:control:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new dropout layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, rate: Float, seed: UInt32, control: UInt8, filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  Dropout layers only support arrays with a data type of `float`. The input shape must be equal to the output shape.

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `rate`: The probability that the layer drops out an element or a group of elements.
- `seed`: The seed for the random number generator that the layer ignores if zero.
- `control`: An 8-bit bit mask that indicates the dimension of the grouping of the dropout decision.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/dropoutlayer/init(input:output:rate:seed:control:filterparameters:))*