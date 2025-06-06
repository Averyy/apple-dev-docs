# reshape(shape:source:)

**Framework**: ML Compute  
**Kind**: method

Adds a new reshape layer to the graph using the shape and source tensor you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func reshape(shape: [Int], source: MLCTensor) -> MLCTensor?
```

#### Return Value

A result tensor.

## Parameters

- `shape`: An array representing the shape of result tensor.
- `source`: The source tensor.

## See Also

- [func split(source: MLCTensor, splitCount: Int, dimension: Int) -> [MLCTensor]?](mlcgraph/split(source:splitcount:dimension:).md)
  Adds a new split layer to the graph using the source tensor, number of splits, and dimension to split the source tensor that you specify.
- [func split(source: MLCTensor, splitSectionLengths: [Int], dimension: Int) -> [MLCTensor]?](mlcgraph/split(source:splitsectionlengths:dimension:).md)
  Adds a new split layer to the graph using the source tensor, lengths of each split section, and dimension to split the source tensor that you specify.
- [func concatenate(sources: [MLCTensor], dimension: Int) -> MLCTensor?](mlcgraph/concatenate(sources:dimension:).md)
  Adds a new concatenation layer to the graph using the source tensors and concatenation dimension you specify.
- [func gather(withDimension: Int, source: MLCTensor, indices: MLCTensor) -> MLCTensor?](mlcgraph/gather(withdimension:source:indices:).md)
  Adds a gather layer to the graph using the source tensor, dimension along which to index, and the indices you specify.
- [func scatter(withDimension: Int, source: MLCTensor, indices: MLCTensor, copyFrom: MLCTensor, reductionType: MLCReductionType) -> MLCTensor?](mlcgraph/scatter(withdimension:source:indices:copyfrom:reductiontype:).md)
  Adds a scatter layer to the graph.
- [func transpose(dimensions: [Int], source: MLCTensor) -> MLCTensor?](mlcgraph/transpose(dimensions:source:).md)
  Adds a new transpose layer to the graph using the dimensions and source tensor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/reshape(shape:source:))*