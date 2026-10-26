# MLCGraph

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A graph of layers you use to build a training or inference graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCGraph
```

```objc
@interface MLCGraph : NSObject
```

## Topics

### Adding Layers to Graphs
- [func node(with: MLCLayer, source: MLCTensor) -> MLCTensor?](./mlcgraph/node%28with,source%29.md)
  Adds the layer and source tensor that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor]) -> MLCTensor?](./mlcgraph/node%28with,sources%29.md)
  Adds the layer and source tensors that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor], disableUpdate: Bool) -> MLCTensor?](./mlcgraph/node%28with,sources,disableupdate%29.md)
  Adds the layer, source tensors, and option to disable optimizer updates that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor], lossLabels: [MLCTensor]) -> MLCTensor?](./mlcgraph/node%28with,sources,losslabels%29.md)
  Adds the layer, sources, and loss labels tensors that you specify to the graph.
### Adding New Layers to Graphs
- [func split(source: MLCTensor, splitCount: Int, dimension: Int) -> [MLCTensor]?](./mlcgraph/split%28source,splitcount,dimension%29.md)
  Adds a new split layer to the graph using the source tensor, number of splits, and dimension to split the source tensor that you specify.
- [func split(source: MLCTensor, splitSectionLengths: [Int], dimension: Int) -> [MLCTensor]?](./mlcgraph/split%28source,splitsectionlengths,dimension%29.md)
  Adds a new split layer to the graph using the source tensor, lengths of each split section, and dimension to split the source tensor that you specify.
- [func concatenate(sources: [MLCTensor], dimension: Int) -> MLCTensor?](./mlcgraph/concatenate%28sources,dimension%29.md)
  Adds a new concatenation layer to the graph using the source tensors and concatenation dimension you specify.
- [func reshape(shape: [Int], source: MLCTensor) -> MLCTensor?](./mlcgraph/reshape%28shape,source%29.md)
  Adds a new reshape layer to the graph using the shape and source tensor you specify.
- [func gather(withDimension: Int, source: MLCTensor, indices: MLCTensor) -> MLCTensor?](./mlcgraph/gather%28withdimension,source,indices%29.md)
  Adds a gather layer to the graph using the source tensor, dimension along which to index, and the indices you specify.
- [func scatter(withDimension: Int, source: MLCTensor, indices: MLCTensor, copyFrom: MLCTensor, reductionType: MLCReductionType) -> MLCTensor?](./mlcgraph/scatter%28withdimension,source,indices,copyfrom,reductiontype%29.md)
  Adds a scatter layer to the graph.
- [func transpose(dimensions: [Int], source: MLCTensor) -> MLCTensor?](./mlcgraph/transpose%28dimensions,source%29.md)
  Adds a new transpose layer to the graph using the dimensions and source tensor you specify.
- [- splitWithSource:splitSectionLengths:dimension:](./mlcgraph/splitwithsource_splitsectionlengths_dimension_.md)
  Adds a new split layer to the graph using the source tensor, lengths of each split section, and dimension to split the source tensor that you specify.
- [- selectWithSources:condition:](./mlcgraph/selectwithsources_condition_.md)
  Adds a select layer to the graph using the condition mask and source tensors you specify.
- [- reshapeWithShape:source:](./mlcgraph/reshapewithshape_source_.md)
  Adds a new reshape layer to the graph using the shape and source tensor you specify.
- [- transposeWithDimensions:source:](./mlcgraph/transposewithdimensions_source_.md)
  Adds a new transpose layer to the graph using the dimensions and source tensor you specify.
### Associating Data with Input Tensors
- [func bindAndWriteData([String : MLCTensorData], forInputs: [String : MLCTensor], to: MLCDevice, batchSize: Int, synchronous: Bool) -> Bool](./mlcgraph/bindandwritedata%28_,forinputs,to,batchsize,synchronous%29.md)
  Associates the given data with the input tensors, and if the device is a GPU, also copies the data to the device memory.
- [func bindAndWriteData([String : MLCTensorData], forInputs: [String : MLCTensor], to: MLCDevice, synchronous: Bool) -> Bool](./mlcgraph/bindandwritedata%28_,forinputs,to,synchronous%29.md)
  Associates the given data with the input tensors, and if the device is a GPU, also copies the data to the device memory.
### Inspecting Graphs
- [func sourceTensors(for: MLCLayer) -> [MLCTensor]](./mlcgraph/sourcetensors%28for%29.md)
  Gets the source tensors for a layer in the training graph.
- [func resultTensors(for: MLCLayer) -> [MLCTensor]](./mlcgraph/resulttensors%28for%29.md)
  Gets the result tensors for a layer in the training graph.
- [var device: MLCDevice?](./mlcgraph/device.md)
  The device you’ll use for compiling and executing a graph.
- [var layers: [MLCLayer]](./mlcgraph/layers.md)
  An array that contains the layers in the graph.
- [var summarizedDOTDescription: String](./mlcgraph/summarizeddotdescription.md)
  A DOT representation of the graph.
### Creating Graphs
- [+ graph](./mlcgraph/graph.md)
  Creates a new graph.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MLCInferenceGraph](./mlcinferencegraph.md)
- [MLCTrainingGraph](./mlctraininggraph.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Graphs
- [class MLCTrainingGraph](./mlctraininggraph.md)
  A training graph that you create from one or more graph objects plus additional layers you add directly to the training graph.
- [class MLCInferenceGraph](./mlcinferencegraph.md)
  An inference graph created from one or more MLCGraph instances plus additional layers added directly to the inference graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph)*