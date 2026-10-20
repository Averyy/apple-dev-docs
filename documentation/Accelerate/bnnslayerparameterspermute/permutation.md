# permutation

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The tuple that defines the permutation.

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
var permutation: (Int, Int, Int, Int, Int, Int, Int, Int)
```

```c
size_t permutation[8];
```

#### Discussion

Use the permutation array to specify the input axis source for the corresponding output axis source. For example, a permutation array [2,1,0] applied on a [`BNNSDataLayoutImageCHW`](../bnnsdatalayoutimagechw.md) tensor results in axis reverse (that is, output axis 0 is input axis 2, output axis 1 is input axis 1, and output axis 2 is input axis 0).

## See Also

### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspermute/permutation)*