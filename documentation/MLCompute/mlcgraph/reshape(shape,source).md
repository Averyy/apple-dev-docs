# reshape(shape:source:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Adds a new reshape layer to the graph using the shape and source tensor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
func reshape(shape: [Int], source: MLCTensor) -> MLCTensor?
```

## Return Value

A result tensor.

## Parameters

- `shape`: An array representing the shape of result tensor.
- `source`: The source tensor.

## See Also

### Adding New Layers to Graphs
- [func split(source: MLCTensor, splitCount: Int, dimension: Int) -> [MLCTensor]?](./split%28source,splitcount,dimension%29.md)
  Adds a new split layer to the graph using the source tensor, number of splits, and dimension to split the source tensor that you specify.
- [func split(source: MLCTensor, splitSectionLengths: [Int], dimension: Int) -> [MLCTensor]?](./split%28source,splitsectionlengths,dimension%29.md)
  Adds a new split layer to the graph using the source tensor, lengths of each split section, and dimension to split the source tensor that you specify.
- [func concatenate(sources: [MLCTensor], dimension: Int) -> MLCTensor?](./concatenate%28sources,dimension%29.md)
  Adds a new concatenation layer to the graph using the source tensors and concatenation dimension you specify.
- [func gather(withDimension: Int, source: MLCTensor, indices: MLCTensor) -> MLCTensor?](./gather%28withdimension,source,indices%29.md)
  Adds a gather layer to the graph using the source tensor, dimension along which to index, and the indices you specify.
- [func scatter(withDimension: Int, source: MLCTensor, indices: MLCTensor, copyFrom: MLCTensor, reductionType: MLCReductionType) -> MLCTensor?](./scatter%28withdimension,source,indices,copyfrom,reductiontype%29.md)
  Adds a scatter layer to the graph.
- [func transpose(dimensions: [Int], source: MLCTensor) -> MLCTensor?](./transpose%28dimensions,source%29.md)
  Adds a new transpose layer to the graph using the dimensions and source tensor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/reshape(shape:source:))*