# init(modelDimension:keyDimension:valueDimension:headCount:dropout:hasBiases:hasAttentionBiases:addsZeroAttention:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a multi-head attention descriptor with the dimensions, number of attention heads, dropout rate, and bias and padding options you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(modelDimension: Int, keyDimension: Int, valueDimension: Int, headCount: Int, dropout: Float, hasBiases: Bool, hasAttentionBiases: Bool, addsZeroAttention: Bool)
```

```objc
+ (instancetype) descriptorWithModelDimension:(NSUInteger) modelDimension keyDimension:(NSUInteger) keyDimension valueDimension:(NSUInteger) valueDimension headCount:(NSUInteger) headCount dropout:(float) dropout hasBiases:(BOOL) hasBiases hasAttentionBiases:(BOOL) hasAttentionBiases addsZeroAttention:(BOOL) addsZeroAttention;
```

## Parameters

- `modelDimension`: The total dimension of model space.
- `keyDimension`: The total dimension of key space; the default value is equal to `modelDimension`.
- `valueDimension`: The total dimension of value space; the default value is equal to `modelDimension`.
- `headCount`: The number of parallel attention heads.
- `dropout`: The dropout rate you apply to the output projection weights; the default value is `0.0`.
- `hasBiases`: A Boolean that specifies whether you add a bias to query, key, value, and output projections; the default value is `true`.
- `hasAttentionBiases`: A Boolean that specifies whether you add a row of zeros to projected key and value; the default value is `false`.
- `addsZeroAttention`: A Boolean that specifies whether you add a row of zeros to projected key and value; the default value is `false`.

## See Also

### Creating Multi-Head Attention Descriptors
- [convenience init(modelDimension: Int, headCount: Int)](./init%28modeldimension,headcount%29.md)
  Creates a multi-head attention descriptor with the model dimension and number of parallel attention heads you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentiondescriptor/init(modeldimension:keydimension:valuedimension:headcount:dropout:hasbiases:hasattentionbiases:addszeroattention:))*