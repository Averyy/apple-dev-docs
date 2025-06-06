# MLCGraph

**Framework**: ML Compute  
**Kind**: class

A graph of layers you use to build a training or inference graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCGraph
```

## Topics

### Adding Layers to Graphs
- [func node(with: MLCLayer, source: MLCTensor) -> MLCTensor?](mlcgraph/node(with:source:).md)
  Adds the layer and source tensor that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor]) -> MLCTensor?](mlcgraph/node(with:sources:).md)
  Adds the layer and source tensors that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor], disableUpdate: Bool) -> MLCTensor?](mlcgraph/node(with:sources:disableupdate:).md)
  Adds the layer, source tensors, and option to disable optimizer updates that you specify to the graph.
- [func node(with: MLCLayer, sources: [MLCTensor], lossLabels: [MLCTensor]) -> MLCTensor?](mlcgraph/node(with:sources:losslabels:).md)
  Adds the layer, sources, and loss labels tensors that you specify to the graph.
### Adding New Layers to Graphs
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
- [func scatter(withDimension: Int, source: MLCTensor, indices: MLCTensor, copyFrom: MLCTensor, reductionType: MLCReductionType) -> MLCTensor?](mlcgraph/scatter(withdimension:source:indices:copyfrom:reductiontype:).md)
  Adds a scatter layer to the graph.
- [func transpose(dimensions: [Int], source: MLCTensor) -> MLCTensor?](mlcgraph/transpose(dimensions:source:).md)
  Adds a new transpose layer to the graph using the dimensions and source tensor you specify.
### Associating Data with Input Tensors
- [func bindAndWriteData([String : MLCTensorData], forInputs: [String : MLCTensor], to: MLCDevice, batchSize: Int, synchronous: Bool) -> Bool](mlcgraph/bindandwritedata(_:forinputs:to:batchsize:synchronous:).md)
  Associates the given data with the input tensors, and if the device is a GPU, also copies the data to the device memory.
- [func bindAndWriteData([String : MLCTensorData], forInputs: [String : MLCTensor], to: MLCDevice, synchronous: Bool) -> Bool](mlcgraph/bindandwritedata(_:forinputs:to:synchronous:).md)
  Associates the given data with the input tensors, and if the device is a GPU, also copies the data to the device memory.
### Inspecting Graphs
- [func sourceTensors(for: MLCLayer) -> [MLCTensor]](mlcgraph/sourcetensors(for:).md)
  Gets the source tensors for a layer in the training graph.
- [func resultTensors(for: MLCLayer) -> [MLCTensor]](mlcgraph/resulttensors(for:).md)
  Gets the result tensors for a layer in the training graph.
- [var device: MLCDevice?](mlcgraph/device.md)
  The device you’ll use for compiling and executing a graph.
- [var layers: [MLCLayer]](mlcgraph/layers.md)
  An array that contains the layers in the graph.
- [var summarizedDOTDescription: String](mlcgraph/summarizeddotdescription.md)
  A DOT representation of the graph.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MLCInferenceGraph](mlcinferencegraph.md)
- [MLCTrainingGraph](mlctraininggraph.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCTrainingGraph](mlctraininggraph.md)
  A training graph that you create from one or more graph objects plus additional layers you add directly to the training graph.
- [class MLCInferenceGraph](mlcinferencegraph.md)
  An inference graph created from one or more MLCGraph instances plus additional layers added directly to the inference graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph)*