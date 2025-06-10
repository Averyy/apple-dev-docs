# init(i_desc:o_desc:permutation:)

**Framework**: Accelerate  
**Kind**: init

Returns a new permute layer parameters structure from the specified parameters.

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
init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, permutation: (Int, Int, Int, Int, Int, Int, Int, Int))
```

#### Discussion

Use the permutation array to specify the input axis source for the corresponding output axis source. For example, a permutation array [2,1,0] applied on a [`BNNSDataLayoutImageCHW`](bnnsdatalayoutimagechw.md) tensor results in axis reverse (that is, output axis 0 is input axis 2, output axis 1 is input axis 1, and output axis 2 is input axis 0).

> ❗ **Important**:  The number of input dimensions must be equal to number of output dimensions.

## Parameters

- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `permutation`: The tuple that defines the permutation.

## See Also

- [init()](bnnslayerparameterspermute/init.md)
  Returns a new permute layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspermute/init(i_desc:o_desc:permutation:))*