# init(alpha:beta:transA:transB:quadratic:a_is_weights:b_is_weights:iA_desc:iB_desc:o_desc:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new broadcast matrix multiply layer parameters structure from the specified parameters.

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
init(alpha: Float, beta: Float, transA: Bool, transB: Bool, quadratic: Bool, a_is_weights: Bool, b_is_weights: Bool, iA_desc: BNNSNDArrayDescriptor, iB_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor)
```

## Parameters

- `alpha`: A value to scale the result.
- `beta`: A value, that must be either 0.0 or 1.0, you use to scale the existing output before the operation adds it to the result.
- `transA`: A Boolean value that transposes the last two dimensions of matrix *A*.
- `transB`: A Boolean value that transposes the last two dimensions of matrix *B*.
- `quadratic`: A Boolean value that determines whether the operation multiplies matrix *A* by itself.
- `a_is_weights`: A Boolean value that determines whether to treat matrix *A* as weights.
- `b_is_weights`: A Boolean value that determines whether to treat matrix *B* as weights.
- `iA_desc`: The descriptor of matrix *A*.
- `iB_desc`: The descriptor of matrix *B*.
- `o_desc`: The descriptor of the output.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Returns a new broadcast matrix multiply layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersbroadcastmatmul/init(alpha:beta:transa:transb:quadratic:a_is_weights:b_is_weights:ia_desc:ib_desc:o_desc:))*