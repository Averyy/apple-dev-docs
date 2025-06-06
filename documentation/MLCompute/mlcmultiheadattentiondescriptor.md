# MLCMultiheadAttentionDescriptor

**Framework**: ML Compute  
**Kind**: class

A configuration object you use to create a multi-head attention layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCMultiheadAttentionDescriptor
```

## Topics

### Creating Multi-Head Attention Descriptors
- [convenience init(modelDimension: Int, headCount: Int)](mlcmultiheadattentiondescriptor/init(modeldimension:headcount:).md)
  Creates a multi-head attention descriptor with the model dimension and number of parallel attention heads you specify.
- [convenience init?(modelDimension: Int, keyDimension: Int, valueDimension: Int, headCount: Int, dropout: Float, hasBiases: Bool, hasAttentionBiases: Bool, addsZeroAttention: Bool)](mlcmultiheadattentiondescriptor/init(modeldimension:keydimension:valuedimension:headcount:dropout:hasbiases:hasattentionbiases:addszeroattention:).md)
  Creates a multi-head attention descriptor with the dimensions, number of attention heads, dropout rate, and bias and padding options you specify.
### Inspecting Multi-Head Attention Descriptors
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
- [var hasAttentionBiases: Bool](mlcmultiheadattentiondescriptor/hasattentionbiases.md)
  A Boolean that specifies whether you add an array of biases to key and value, respectively.
- [var addsZeroAttention: Bool](mlcmultiheadattentiondescriptor/addszeroattention.md)
  A Boolean that specifies whether you add a row of zeros to projected key and value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init?(descriptor: MLCMultiheadAttentionDescriptor, weights: [MLCTensor], biases: [MLCTensor]?, attentionBiases: [MLCTensor]?)](mlcmultiheadattentionlayer/init(descriptor:weights:biases:attentionbiases:).md)
  Creates a multi-head attention layer with the descriptor, weights, and biases you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentiondescriptor)*