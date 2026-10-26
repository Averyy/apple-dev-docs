# transposeWithDimensions:source:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Adds a new transpose layer to the graph using the dimensions and source tensor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
- (MLCTensor *) transposeWithDimensions:(NSArray<NSNumber *> *) dimensions source:(MLCTensor *) source;
```

#### Return Value

A result tensor.

#### Discussion

The dimensions array specifies the input axis source for each output axis. In other words, the `n`th element in the dimensions array specifies the input axis source for the `n`th axis in the output.

> **Note**:  The batch dimension is typically axis 0, which you can’t transpose.

## Parameters

- `dimensions`: An array representing the desired ordering of dimensions.
- `source`: The source tensor.

## See Also

### Adding New Layers to Graphs
- [func split(source: MLCTensor, splitCount: Int, dimension: Int) -> [MLCTensor]?](./split%28source,splitcount,dimension%29.md)
  Adds a new split layer to the graph using the source tensor, number of splits, and dimension to split the source tensor that you specify.
- [- splitWithSource:splitSectionLengths:dimension:](./splitwithsource_splitsectionlengths_dimension_.md)
  Adds a new split layer to the graph using the source tensor, lengths of each split section, and dimension to split the source tensor that you specify.
- [- selectWithSources:condition:](./selectwithsources_condition_.md)
  Adds a select layer to the graph using the condition mask and source tensors you specify.
- [func concatenate(sources: [MLCTensor], dimension: Int) -> MLCTensor?](./concatenate%28sources,dimension%29.md)
  Adds a new concatenation layer to the graph using the source tensors and concatenation dimension you specify.
- [- reshapeWithShape:source:](./reshapewithshape_source_.md)
  Adds a new reshape layer to the graph using the shape and source tensor you specify.
- [func gather(withDimension: Int, source: MLCTensor, indices: MLCTensor) -> MLCTensor?](./gather%28withdimension,source,indices%29.md)
  Adds a gather layer to the graph using the source tensor, dimension along which to index, and the indices you specify.
- [func scatter(withDimension: Int, source: MLCTensor, indices: MLCTensor, copyFrom: MLCTensor, reductionType: MLCReductionType) -> MLCTensor?](./scatter%28withdimension,source,indices,copyfrom,reductiontype%29.md)
  Adds a scatter layer to the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/transposewithdimensions:source:)*