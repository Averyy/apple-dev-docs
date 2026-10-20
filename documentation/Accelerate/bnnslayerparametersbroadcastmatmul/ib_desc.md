# iB_desc

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The descriptor of matrix *B*.

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
var iB_desc: BNNSNDArrayDescriptor
```

```c
BNNSNDArrayDescriptor iB_desc;
```

## See Also

### Instance Properties
- [var alpha: Float](./alpha.md)
  A value to scale the result.
- [var beta: Float](./beta.md)
  A value, that must be either 0.0 or 1.0, you use to scale the existing output before the operation adds it to the result.
- [var transA: Bool](./transa.md)
  A Boolean value that transposes the last two dimensions of matrix *A*.
- [var transB: Bool](./transb.md)
  A Boolean value that transposes the last two dimensions of matrix *B*.
- [var quadratic: Bool](./quadratic.md)
  A Boolean value that determines whether the operation multiplies matrix *A* by itself.
- [var a_is_weights: Bool](./a_is_weights.md)
  A Boolean value that determines whether to treat matrix *A* as weights.
- [var b_is_weights: Bool](./b_is_weights.md)
  A Boolean value that determines whether to treat matrix *B* as weights.
- [var iA_desc: BNNSNDArrayDescriptor](./ia_desc.md)
  The descriptor of matrix *A*.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersbroadcastmatmul/ib_desc)*