# iA_desc

**Framework**: Accelerate  
**Kind**: property

The descriptor of matrix .

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
var iA_desc: BNNSNDArrayDescriptor
```

## See Also

- [var alpha: Float](bnnslayerparametersbroadcastmatmul/alpha.md)
  A value to scale the result.
- [var beta: Float](bnnslayerparametersbroadcastmatmul/beta.md)
  A value, that must be either 0.0 or 1.0, you use to scale the existing output before the operation adds it to the result.
- [var transA: Bool](bnnslayerparametersbroadcastmatmul/transa.md)
  A Boolean value that transposes the last two dimensions of matrix .
- [var transB: Bool](bnnslayerparametersbroadcastmatmul/transb.md)
  A Boolean value that transposes the last two dimensions of matrix .
- [var quadratic: Bool](bnnslayerparametersbroadcastmatmul/quadratic.md)
  A Boolean value that determines whether the operation multiplies matrix  by itself.
- [var a_is_weights: Bool](bnnslayerparametersbroadcastmatmul/a_is_weights.md)
  A Boolean value that determines whether to treat matrix  as weights.
- [var b_is_weights: Bool](bnnslayerparametersbroadcastmatmul/b_is_weights.md)
  A Boolean value that determines whether to treat matrix  as weights.
- [var iB_desc: BNNSNDArrayDescriptor](bnnslayerparametersbroadcastmatmul/ib_desc.md)
  The descriptor of matrix .
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersbroadcastmatmul/o_desc.md)
  The descriptor of the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersbroadcastmatmul/ia_desc)*