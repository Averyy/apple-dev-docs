# hasAttentionBiases

**Framework**: ML Compute  
**Kind**: property

A Boolean that specifies whether you add an array of biases to key and value, respectively.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var hasAttentionBiases: Bool { get }
```

## See Also

- [var modelDimension: Int](mlcmultiheadattentiondescriptor/modeldimension.md)
  The model or embedding dimension.
- [var keyDimension: Int](mlcmultiheadattentiondescriptor/keydimension.md)
  The total dimension of key space, which must be divisible by the number of heads.
- [var valueDimension: Int](mlcmultiheadattentiondescriptor/valuedimension.md)
  The total dimension of value space, which must be divisible by the number of heads.
- [var headCount: Int](mlcmultiheadattentiondescriptor/headcount.md)
  The number of parallel attention heads.
- [var dropout: Float](mlcmultiheadattentiondescriptor/dropout.md)
  The dropout rate you apply to the output projection weights.
- [var hasBiases: Bool](mlcmultiheadattentiondescriptor/hasbiases.md)
  A Boolean that specifies whether you add a bias to query, key, value, and output projections.
- [var addsZeroAttention: Bool](mlcmultiheadattentiondescriptor/addszeroattention.md)
  A Boolean that specifies whether you add a row of zeros to projected key and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentiondescriptor/hasattentionbiases)*