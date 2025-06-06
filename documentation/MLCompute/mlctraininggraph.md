# MLCTrainingGraph

**Framework**: ML Compute  
**Kind**: class

A training graph that you create from one or more graph objects plus additional layers you add directly to the training graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCTrainingGraph
```

#### Overview

The framework provides a family of graph-execution methods to execute a full training iteration, and methods to execute the forward pass, the gradient pass, and optimizer update, individually.

Use one of the `execute` methods to execute a full training iteration to accelerate an ML model represented as a single training graph.

Use one of the `executeForward`, `executeGradient`, or `executeOptimizerUpdatemethods` to accelerate an ML library that separates the forward pass, gradient pass, and optimizer update as separate phases.

## Topics

### Creating Training Graphs
- [convenience init(graphObjects: [MLCGraph], lossLayer: MLCLayer?, optimizer: MLCOptimizer?)](mlctraininggraph/init(graphobjects:losslayer:optimizer:).md)
  Creates a training graph with the layers from the graph objects, loss layer, and optimizer you specify.
- [Optimizers](optimizers.md)
  Create an optimizer to use with the training graph.
- [class MLCTensorParameter](mlctensorparameter.md)
  A tensor parameter object.
### Preparing Training Graphs
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?) -> Bool](mlctraininggraph/addinputs(_:losslabels:).md)
  Adds the inputs and loss label inputs that you specify to the training graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](mlctraininggraph/addinputs(_:losslabels:losslabelweights:).md)
  Adds the inputs, loss labels, and loss label weights that you specify to the training graph.
- [func addOutputs([String : MLCTensor]) -> Bool](mlctraininggraph/addoutputs(_:).md)
  Adds the outputs to the training graph you specify.
- [func stopGradient(for: [MLCTensor]) -> Bool](mlctraininggraph/stopgradient(for:).md)
  Adds the tensors that you specify, to indicate which contributions the graph excludes when computing gradients during gradient pass.
- [func compileOptimizer(MLCOptimizer) -> Bool](mlctraininggraph/compileoptimizer(_:).md)
  Compiles the optimizer to use with a training graph you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](mlctraininggraph/compile(options:device:).md)
  Compiles the training graph for the options and device you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](mlctraininggraph/compile(options:device:inputtensors:inputtensorsdata:).md)
  Compiles the training graph for the options, device, and input tensors you specify.
- [func link(with: [MLCTrainingGraph]) -> Bool](mlctraininggraph/link(with:).md)
  Links the training graphs you specify.
- [func allocateUserGradient(for: MLCTensor) -> MLCTensor?](mlctraininggraph/allocateusergradient(for:).md)
  Allocates an entry for a gradient for the result tensor you specify.
- [struct MLCGraphCompilationOptions](mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.
### Executing Training Iterations
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:batchsize:options:completionhandler:).md)
  Executes the training graph with the input data, batch size, execution options, and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:completionhandler:).md)
  Executes the training graph with the input data, output data, batch size, execution options, and completion handler that you specify.
- [func synchronizeUpdates()](mlctraininggraph/synchronizeupdates.md)
  Synchronizes updates from device memory.
- [func setTrainingTensorParameters([MLCTensorParameter]) -> Bool](mlctraininggraph/settrainingtensorparameters(_:).md)
  Sets the input tensor parameters, which the optimizer then updates.
- [struct MLCExecutionOptions](mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.
### Executing Forward, Gradient, and Optimizer Updates
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/executeforward(batchsize:options:completionhandler:).md)
  Executes the forward pass of the training graph with the batch size, execution options, and completion handler you specify.
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/executeforward(batchsize:options:outputsdata:completionhandler:).md)
  Executes the forward pass of the training graph with the batch size, execution options, output data, and completion handler you specify.
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?) async throws -> (result: MLCTensor?, executionTime: TimeInterval)](mlctraininggraph/executeforward(batchsize:options:outputsdata:).md)
  Executes the forward pass of the training graph with the batch size, execution options, and output data you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/executegradient(batchsize:options:completionhandler:).md)
  Executes the gradient pass of the training graph with the batch size, execution options, and completion handler you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/executegradient(batchsize:options:outputsdata:completionhandler:).md)
  Executes the gradient pass of the training graph with the batch size, execution options, output data, and completion handler you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?) async throws -> TimeInterval](mlctraininggraph/executegradient(batchsize:options:outputsdata:).md)
  Executes the gradient pass of the training graph with the batch size, execution options, and output data you specify.
- [func executeOptimizerUpdate(options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/executeoptimizerupdate(options:completionhandler:).md)
  Executes the optimizer update pass of the training graph with the execution options and completion handler you specify.
- [func executeOptimizerUpdate(options: MLCExecutionOptions) async throws -> TimeInterval](mlctraininggraph/executeoptimizerupdate(options:).md)
  Executes the optimizer update pass of the training graph with the execution options you specify.
- [func synchronizeUpdates()](mlctraininggraph/synchronizeupdates.md)
  Synchronizes updates from device memory.
- [func setTrainingTensorParameters([MLCTensorParameter]) -> Bool](mlctraininggraph/settrainingtensorparameters(_:).md)
  Sets the input tensor parameters, which the optimizer then updates.
- [struct MLCExecutionOptions](mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.
### Inspecting Training Graphs
- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?, with: MLCTensor) -> Bool](mlctraininggraph/bindoptimizerdata(_:devicedata:with:).md)
  Associates the optimizer and device data you specify along with the tensor.
- [var optimizer: MLCOptimizer?](mlctraininggraph/optimizer.md)
  The optimizer to use with the training graph.
- [var deviceMemorySize: Int](mlctraininggraph/devicememorysize.md)
  The device memory size in bytes for all intermediate tensors for forward, gradient passes, and optimizer updates for all layers in the training graph.
- [func gradientTensor(forInput: MLCTensor) -> MLCTensor?](mlctraininggraph/gradienttensor(forinput:).md)
  Gets the gradient tensor for the input tensor you specify.
- [func sourceGradientTensors(for: MLCLayer) -> [MLCTensor]](mlctraininggraph/sourcegradienttensors(for:).md)
  Gets the source gradient tensors for the layer in the training graph you specify.
- [func resultGradientTensors(for: MLCLayer) -> [MLCTensor]](mlctraininggraph/resultgradienttensors(for:).md)
  Gets the result gradient tensors for the layer in the training graph you specify.
- [func gradientData(forParameter: MLCTensor, layer: MLCLayer) -> Data?](mlctraininggraph/gradientdata(forparameter:layer:).md)
  Gets the gradient data for the trainable parameter and associated layer you specify.

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
- [class MLCInferenceGraph](mlcinferencegraph.md)
  An inference graph created from one or more MLCGraph instances plus additional layers added directly to the inference graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph)*