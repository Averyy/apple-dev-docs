# init(input:output:dictionary:paddingIndex:maximumNorm:normType:scalesGradientByFrequency:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new embedding layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, dictionary: BNNSNDArrayDescriptor, paddingIndex: Int, maximumNorm: Float, normType: BNNS.Norm, scalesGradientByFrequency: Bool, filterParameters: BNNSFilterParameters? = nil)
```

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `dictionary`: The descriptor of the dictionary array.
- `paddingIndex`: The padding index. The operation returns a zero tensor for dictionary items with an index that corresponds to the padding index.
- `maximumNorm`: The maximum norm. If nonzero, the operation renormalizes any vector with a norm greater than   during forward lookups
- `normType`: The norm type. If   is nonzero, this value specifies the p-norm where p equals  .
- `scalesGradientByFrequency`: A Boolean value that specifies that the operation scales calculated gradients based on the number of occurrence of the corresponding index in the input.
- `filterParameters`: The filter runtime parameters.

## See Also

- [func BNNSFilterCreateLayerEmbedding(UnsafePointer<BNNSLayerParametersEmbedding>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerembedding(_:_:).md)
  Returns a new embedding layer.
- [struct Norm](bnns/norm.md)
  Constants that describe norm types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/embeddinglayer/init(input:output:dictionary:paddingindex:maximumnorm:normtype:scalesgradientbyfrequency:filterparameters:))*