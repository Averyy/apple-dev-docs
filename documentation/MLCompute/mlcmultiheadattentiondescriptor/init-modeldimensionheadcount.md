# init(modelDimension:headCount:)

**Framework**: ML Compute  
**Kind**: init

Creates a multi-head attention descriptor with the model dimension and number of parallel attention heads you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(modelDimension: Int, headCount: Int)
```

## Parameters

- `modelDimension`: The total dimension of model space.
- `headCount`: The number of parallel attention heads.

## See Also

- [convenience init?(modelDimension: Int, keyDimension: Int, valueDimension: Int, headCount: Int, dropout: Float, hasBiases: Bool, hasAttentionBiases: Bool, addsZeroAttention: Bool)](mlcmultiheadattentiondescriptor/init(modeldimension:keydimension:valuedimension:headcount:dropout:hasbiases:hasattentionbiases:addszeroattention:).md)
  Creates a multi-head attention descriptor with the dimensions, number of attention heads, dropout rate, and bias and padding options you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentiondescriptor/init(modeldimension:headcount:))*