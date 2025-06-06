# scatter(withDimension:source:indices:copyFrom:reductionType:)

**Framework**: ML Compute  
**Kind**: method

Adds a scatter layer to the graph.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
func scatter(withDimension dimension: Int, source: MLCTensor, indices: MLCTensor, copyFrom: MLCTensor, reductionType: MLCReductionType) -> MLCTensor?
```

#### Return Value

A scatter tensor.

#### Discussion

The reductionType property must be [`MLCReductionType.none`](mlcreductiontype/none.md) or [`MLCReductionType.sum`](mlcreductiontype/sum.md).

## Parameters

- `dimension`: The dimension along which to index.
- `source`: The source tensor.
- `indices`: The index of elements to scatter.
- `copyFrom`: The source tensor whose data is first copied to the result tensor.
- `reductionType`: The reduction type applied for all values in the source tensor that the system scatters to a specific location in the result tensor.

## See Also

- [func split(source: MLCTensor, splitCount: Int, dimension: Int) -> [MLCTensor]?](mlcgraph/split(source:splitcount:dimension:).md)
  Adds a new split layer to the graph using the source tensor, number of splits, and dimension to split the source tensor that you specify.
- [func split(source: MLCTensor, splitSectionLengths: [Int], dimension: Int) -> [MLCTensor]?](mlcgraph/split(source:splitsectionlengths:dimension:).md)
  Adds a new split layer to the graph using the source tensor, lengths of each split section, and dimension to split the source tensor that you specify.
- [func concatenate(sources: [MLCTensor], dimension: Int) -> MLCTensor?](mlcgraph/concatenate(sources:dimension:).md)
  Adds a new concatenation layer to the graph using the source tensors and concatenation dimension you specify.
- [func reshape(shape: [Int], source: MLCTensor) -> MLCTensor?](mlcgraph/reshape(shape:source:).md)
  Adds a new reshape layer to the graph using the shape and source tensor you specify.
- [func gather(withDimension: Int, source: MLCTensor, indices: MLCTensor) -> MLCTensor?](mlcgraph/gather(withdimension:source:indices:).md)
  Adds a gather layer to the graph using the source tensor, dimension along which to index, and the indices you specify.
- [func transpose(dimensions: [Int], source: MLCTensor) -> MLCTensor?](mlcgraph/transpose(dimensions:source:).md)
  Adds a new transpose layer to the graph using the dimensions and source tensor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/scatter(withdimension:source:indices:copyfrom:reductiontype:))*