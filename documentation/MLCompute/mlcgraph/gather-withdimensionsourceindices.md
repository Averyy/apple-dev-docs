# gather(withDimension:source:indices:)

**Framework**: ML Compute  
**Kind**: method

Adds a gather layer to the graph using the source tensor, dimension along which to index, and the indices you specify.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
func gather(withDimension dimension: Int, source: MLCTensor, indices: MLCTensor) -> MLCTensor?
```

#### Return Value

A gather tensor.

## Parameters

- `dimension`: The dimension along which to index.
- `source`: The source tensor.
- `indices`: The index of elements to gather.

## See Also

- [func split(source: MLCTensor, splitCount: Int, dimension: Int) -> [MLCTensor]?](mlcgraph/split(source:splitcount:dimension:).md)
  Adds a new split layer to the graph using the source tensor, number of splits, and dimension to split the source tensor that you specify.
- [func split(source: MLCTensor, splitSectionLengths: [Int], dimension: Int) -> [MLCTensor]?](mlcgraph/split(source:splitsectionlengths:dimension:).md)
  Adds a new split layer to the graph using the source tensor, lengths of each split section, and dimension to split the source tensor that you specify.
- [func concatenate(sources: [MLCTensor], dimension: Int) -> MLCTensor?](mlcgraph/concatenate(sources:dimension:).md)
  Adds a new concatenation layer to the graph using the source tensors and concatenation dimension you specify.
- [func reshape(shape: [Int], source: MLCTensor) -> MLCTensor?](mlcgraph/reshape(shape:source:).md)
  Adds a new reshape layer to the graph using the shape and source tensor you specify.
- [func scatter(withDimension: Int, source: MLCTensor, indices: MLCTensor, copyFrom: MLCTensor, reductionType: MLCReductionType) -> MLCTensor?](mlcgraph/scatter(withdimension:source:indices:copyfrom:reductiontype:).md)
  Adds a scatter layer to the graph.
- [func transpose(dimensions: [Int], source: MLCTensor) -> MLCTensor?](mlcgraph/transpose(dimensions:source:).md)
  Adds a new transpose layer to the graph using the dimensions and source tensor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/gather(withdimension:source:indices:))*