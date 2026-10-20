# MLCMultiheadAttentionDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A configuration object you use to create a multi-head attention layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCMultiheadAttentionDescriptor
```

```objc
@interface MLCMultiheadAttentionDescriptor : NSObject
```

## Topics

### Creating Multi-Head Attention Descriptors
- [convenience init(modelDimension: Int, headCount: Int)](./mlcmultiheadattentiondescriptor/init%28modeldimension,headcount%29.md)
  Creates a multi-head attention descriptor with the model dimension and number of parallel attention heads you specify.
- [convenience init?(modelDimension: Int, keyDimension: Int, valueDimension: Int, headCount: Int, dropout: Float, hasBiases: Bool, hasAttentionBiases: Bool, addsZeroAttention: Bool)](./mlcmultiheadattentiondescriptor/init%28modeldimension,keydimension,valuedimension,headcount,dropout,hasbiases,hasattentionbiases,addszeroattention%29.md)
  Creates a multi-head attention descriptor with the dimensions, number of attention heads, dropout rate, and bias and padding options you specify.
### Inspecting Multi-Head Attention Descriptors
- [var modelDimension: Int](./mlcmultiheadattentiondescriptor/modeldimension.md)
  The model or embedding dimension.
- [var keyDimension: Int](./mlcmultiheadattentiondescriptor/keydimension.md)
  The total dimension of key space, which must be divisible by the number of heads.
- [var valueDimension: Int](./mlcmultiheadattentiondescriptor/valuedimension.md)
  The total dimension of value space, which must be divisible by the number of heads.
- [var headCount: Int](./mlcmultiheadattentiondescriptor/headcount.md)
  The number of parallel attention heads.
- [var dropout: Float](./mlcmultiheadattentiondescriptor/dropout.md)
  The dropout rate you apply to the output projection weights.
- [var hasBiases: Bool](./mlcmultiheadattentiondescriptor/hasbiases.md)
  A Boolean that specifies whether you add a bias to query, key, value, and output projections.
- [var hasAttentionBiases: Bool](./mlcmultiheadattentiondescriptor/hasattentionbiases.md)
  A Boolean that specifies whether you add an array of biases to key and value, respectively.
- [var addsZeroAttention: Bool](./mlcmultiheadattentiondescriptor/addszeroattention.md)
  A Boolean that specifies whether you add a row of zeros to projected key and value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating Multi-Head Attention Layers
- [convenience init?(descriptor: MLCMultiheadAttentionDescriptor, weights: [MLCTensor], biases: [MLCTensor]?, attentionBiases: [MLCTensor]?)](./mlcmultiheadattentionlayer/init%28descriptor,weights,biases,attentionbiases%29.md)
  Creates a multi-head attention layer with the descriptor, weights, and biases you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmultiheadattentiondescriptor)*