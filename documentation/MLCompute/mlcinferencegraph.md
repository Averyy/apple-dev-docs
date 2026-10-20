# MLCInferenceGraph

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

An inference graph created from one or more MLCGraph instances plus additional layers added directly to the inference graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCInferenceGraph
```

```objc
@interface MLCInferenceGraph : MLCGraph
```

## Topics

### Creating Inference Graphs
- [convenience init(graphObjects: [MLCGraph])](./mlcinferencegraph/init%28graphobjects%29.md)
  Creates an inference graph with the layers from the graph objects you specify.
### Preparing Inference Graphs
- [func addInputs([String : MLCTensor]) -> Bool](./mlcinferencegraph/addinputs%28_%29.md)
  Adds the inputs you specify to the inference graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](./mlcinferencegraph/addinputs%28_,losslabels,losslabelweights%29.md)
  Adds the inputs, loss labels, and loss label weights that you specify to the inference graph.
- [func addOutputs([String : MLCTensor]) -> Bool](./mlcinferencegraph/addoutputs%28_%29.md)
  Adds the outputs you specify to the inference graph.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](./mlcinferencegraph/compile%28options,device%29.md)
  Compiles the inference graph for the options and device you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](./mlcinferencegraph/compile%28options,device,inputtensors,inputtensorsdata%29.md)
  Compiles the inference graph for the options, device, and input tensors you specify.
- [func link(with: [MLCInferenceGraph]) -> Bool](./mlcinferencegraph/link%28with%29.md)
  Links the inference graphs you specify.
- [struct MLCGraphCompilationOptions](./mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.
### Executing Inference Graphs
- [func execute(inputsData: [String : MLCTensorData], batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlcinferencegraph/execute%28inputsdata,batchsize,options,completionhandler%29.md)
  Executes the inference graph with the inputs data, batch size, execution options, and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlcinferencegraph/execute%28inputsdata,outputsdata,batchsize,options,completionhandler%29.md)
  Executes the inference graph with the inputs and outputs data, batch size, execution options, and completion handler that you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlcinferencegraph/execute%28inputsdata,losslabelsdata,losslabelweightsdata,batchsize,options,completionhandler%29.md)
  Executes the inference graph with the input data, batch size, execution options and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlcinferencegraph/execute%28inputsdata,losslabelsdata,losslabelweightsdata,outputsdata,batchsize,options,completionhandler%29.md)
  Executes the inference graph with the input and output data, batch size, execution options, and completion handler that you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions) async throws -> (result: MLCTensor?, executionTime: TimeInterval)](./mlcinferencegraph/execute%28inputsdata,losslabelsdata,losslabelweightsdata,outputsdata,batchsize,options%29.md)
  Executes the inference graph with the input and output data, batch size, and execution options you specify.
- [struct MLCExecutionOptions](./mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](./mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.
### Inspecting Inference Graphs
- [var deviceMemorySize: Int](./mlcinferencegraph/devicememorysize.md)
  The device memory size in bytes for all intermediate tensors in the inference graph.
### Initializers
- [convenience init()](./mlcinferencegraph/init%28%29.md)

## Relationships

### Inherits From
- [MLCGraph](./mlcgraph.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Graphs
- [class MLCGraph](./mlcgraph.md)
  A graph of layers you use to build a training or inference graph.
- [class MLCTrainingGraph](./mlctraininggraph.md)
  A training graph that you create from one or more graph objects plus additional layers you add directly to the training graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinferencegraph)*