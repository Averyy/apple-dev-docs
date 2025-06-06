# MLCInferenceGraph

**Framework**: ML Compute  
**Kind**: class

An inference graph created from one or more MLCGraph instances plus additional layers added directly to the inference graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCInferenceGraph
```

## Topics

### Creating Inference Graphs
- [convenience init(graphObjects: [MLCGraph])](mlcinferencegraph/init(graphobjects:).md)
  Creates an inference graph with the layers from the graph objects you specify.
### Preparing Inference Graphs
- [func addInputs([String : MLCTensor]) -> Bool](mlcinferencegraph/addinputs(_:).md)
  Adds the inputs you specify to the inference graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](mlcinferencegraph/addinputs(_:losslabels:losslabelweights:).md)
  Adds the inputs, loss labels, and loss label weights that you specify to the inference graph.
- [func addOutputs([String : MLCTensor]) -> Bool](mlcinferencegraph/addoutputs(_:).md)
  Adds the outputs you specify to the inference graph.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](mlcinferencegraph/compile(options:device:).md)
  Compiles the inference graph for the options and device you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](mlcinferencegraph/compile(options:device:inputtensors:inputtensorsdata:).md)
  Compiles the inference graph for the options, device, and input tensors you specify.
- [func link(with: [MLCInferenceGraph]) -> Bool](mlcinferencegraph/link(with:).md)
  Links the inference graphs you specify.
- [struct MLCGraphCompilationOptions](mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.
### Executing Inference Graphs
- [func execute(inputsData: [String : MLCTensorData], batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the inputs data, batch size, execution options, and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:outputsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the inputs and outputs data, batch size, execution options, and completion handler that you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the input data, batch size, execution options and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the input and output data, batch size, execution options, and completion handler that you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions) async throws -> (result: MLCTensor?, executionTime: TimeInterval)](mlcinferencegraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:).md)
  Executes the inference graph with the input and output data, batch size, and execution options you specify.
- [struct MLCExecutionOptions](mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.
### Inspecting Inference Graphs
- [var deviceMemorySize: Int](mlcinferencegraph/devicememorysize.md)
  The device memory size in bytes for all intermediate tensors in the inference graph.

## Relationships

### Inherits From
- [MLCGraph](mlcgraph.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCGraph](mlcgraph.md)
  A graph of layers you use to build a training or inference graph.
- [class MLCTrainingGraph](mlctraininggraph.md)
  A training graph that you create from one or more graph objects plus additional layers you add directly to the training graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinferencegraph)*