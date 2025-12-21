# init(input:output:permutation:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new permute layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, permutation: [Int], filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  The number of input dimensions must be equal to number of output dimensions.

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `permutation`: The array that defines the permutation.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/permutelayer/init(input:output:permutation:filterparameters:))*