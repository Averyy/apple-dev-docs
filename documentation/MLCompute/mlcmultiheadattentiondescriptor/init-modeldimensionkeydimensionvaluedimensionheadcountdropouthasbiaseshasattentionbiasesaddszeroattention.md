# init(modelDimension:keyDimension:valueDimension:headCount:dropout:hasBiases:hasAttentionBiases:addsZeroAttention:)

**Framework**: ML Compute  
**Kind**: init

Creates a multi-head attention descriptor with the dimensions, number of attention heads, dropout rate, and bias and padding options you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(modelDimension: Int, keyDimension: Int, valueDimension: Int, headCount: Int, dropout: Float, hasBiases: Bool, hasAttentionBiases: Bool, addsZeroAttention: Bool)
```

## Parameters

- `modelDimension`: The total dimension of model space.
- `keyDimension`: The total dimension of key space; the default value is equal to  .
- `valueDimension`: The total dimension of value space; the default value is equal to  .
- `headCount`: The number of parallel attention heads.
- `dropout`: The dropout rate you apply to the output projection weights; the default value is  .
- `hasBiases`: A Boolean that specifies whether you add a bias to query, key, value, and output projections; the default value is  .
- `hasAttentionBiases`: A Boolean that specifies whether you add a row of zeros to projected key and value; the default value is  .
- `addsZeroAttention`: A Boolean that specifies whether you add a row of zeros to projected key and value; the default value is  .

## See Also

- [convenience init(modelDimension: Int, headCount: Int)](mlcmultiheadattentiondescriptor/init(modeldimension:headcount:).md)
  Creates a multi-head attention descriptor with the model dimension and number of parallel attention heads you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentiondescriptor/init(modeldimension:keydimension:valuedimension:headcount:dropout:hasbiases:hasattentionbiases:addszeroattention:))*