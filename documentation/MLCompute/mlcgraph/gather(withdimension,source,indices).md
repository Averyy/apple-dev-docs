# gather(withDimension:source:indices:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Adds a gather layer to the graph using the source tensor, dimension along which to index, and the indices you specify.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```swift
func gather(withDimension dimension: Int, source: MLCTensor, indices: MLCTensor) -> MLCTensor?
```

```objc
- (MLCTensor *) gatherWithDimension:(NSUInteger) dimension source:(MLCTensor *) source indices:(MLCTensor *) indices;
```

#### Return Value

A gather tensor.

## Parameters

- `dimension`: The dimension along which to index.
- `source`: The source tensor.
- `indices`: The index of elements to gather.

## See Also

### Adding New Layers to Graphs
- [func split(source: MLCTensor, splitCount: Int, dimension: Int) -> [MLCTensor]?](./split%28source,splitcount,dimension%29.md)
  Adds a new split layer to the graph using the source tensor, number of splits, and dimension to split the source tensor that you specify.
- [func split(source: MLCTensor, splitSectionLengths: [Int], dimension: Int) -> [MLCTensor]?](./split%28source,splitsectionlengths,dimension%29.md)
  Adds a new split layer to the graph using the source tensor, lengths of each split section, and dimension to split the source tensor that you specify.
- [func concatenate(sources: [MLCTensor], dimension: Int) -> MLCTensor?](./concatenate%28sources,dimension%29.md)
  Adds a new concatenation layer to the graph using the source tensors and concatenation dimension you specify.
- [func reshape(shape: [Int], source: MLCTensor) -> MLCTensor?](./reshape%28shape,source%29.md)
  Adds a new reshape layer to the graph using the shape and source tensor you specify.
- [func scatter(withDimension: Int, source: MLCTensor, indices: MLCTensor, copyFrom: MLCTensor, reductionType: MLCReductionType) -> MLCTensor?](./scatter%28withdimension,source,indices,copyfrom,reductiontype%29.md)
  Adds a scatter layer to the graph.
- [func transpose(dimensions: [Int], source: MLCTensor) -> MLCTensor?](./transpose%28dimensions,source%29.md)
  Adds a new transpose layer to the graph using the dimensions and source tensor you specify.
- [- splitWithSource:splitSectionLengths:dimension:](./splitwithsource_splitsectionlengths_dimension_.md)
  Adds a new split layer to the graph using the source tensor, lengths of each split section, and dimension to split the source tensor that you specify.
- [- selectWithSources:condition:](./selectwithsources_condition_.md)
  Adds a select layer to the graph using the condition mask and source tensors you specify.
- [- reshapeWithShape:source:](./reshapewithshape_source_.md)
  Adds a new reshape layer to the graph using the shape and source tensor you specify.
- [- transposeWithDimensions:source:](./transposewithdimensions_source_.md)
  Adds a new transpose layer to the graph using the dimensions and source tensor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/gather(withdimension:source:indices:))*