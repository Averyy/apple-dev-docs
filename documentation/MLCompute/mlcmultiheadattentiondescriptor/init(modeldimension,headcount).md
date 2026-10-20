# init(modelDimension:headCount:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a multi-head attention descriptor with the model dimension and number of parallel attention heads you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(modelDimension: Int, headCount: Int)
```

```objc
+ (instancetype) descriptorWithModelDimension:(NSUInteger) modelDimension headCount:(NSUInteger) headCount;
```

## Parameters

- `modelDimension`: The total dimension of model space.
- `headCount`: The number of parallel attention heads.

## See Also

### Creating Multi-Head Attention Descriptors
- [convenience init?(modelDimension: Int, keyDimension: Int, valueDimension: Int, headCount: Int, dropout: Float, hasBiases: Bool, hasAttentionBiases: Bool, addsZeroAttention: Bool)](./init%28modeldimension,keydimension,valuedimension,headcount,dropout,hasbiases,hasattentionbiases,addszeroattention%29.md)
  Creates a multi-head attention descriptor with the dimensions, number of attention heads, dropout rate, and bias and padding options you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentiondescriptor/init(modeldimension:headcount:))*