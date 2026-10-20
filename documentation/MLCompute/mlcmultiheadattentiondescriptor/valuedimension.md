# valueDimension

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The total dimension of value space, which must be divisible by the number of heads.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var valueDimension: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger valueDimension;
```

## See Also

### Inspecting Multi-Head Attention Descriptors
- [var modelDimension: Int](./modeldimension.md)
  The model or embedding dimension.
- [var keyDimension: Int](./keydimension.md)
  The total dimension of key space, which must be divisible by the number of heads.
- [var headCount: Int](./headcount.md)
  The number of parallel attention heads.
- [var dropout: Float](./dropout.md)
  The dropout rate you apply to the output projection weights.
- [var hasBiases: Bool](./hasbiases.md)
  A Boolean that specifies whether you add a bias to query, key, value, and output projections.
- [var hasAttentionBiases: Bool](./hasattentionbiases.md)
  A Boolean that specifies whether you add an array of biases to key and value, respectively.
- [var addsZeroAttention: Bool](./addszeroattention.md)
  A Boolean that specifies whether you add a row of zeros to projected key and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentiondescriptor/valuedimension)*