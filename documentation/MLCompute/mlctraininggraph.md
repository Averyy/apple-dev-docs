# MLCTrainingGraph

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A training graph that you create from one or more graph objects plus additional layers you add directly to the training graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCTrainingGraph
```

```objc
@interface MLCTrainingGraph : MLCGraph
```

## Overview

The framework provides a family of graph-execution methods to execute a full training iteration, and methods to execute the forward pass, the gradient pass, and optimizer update, individually.

Use one of the `execute` methods to execute a full training iteration to accelerate an ML model represented as a single training graph.

Use one of the `executeForward`, `executeGradient`, or `executeOptimizerUpdatemethods` to accelerate an ML library that separates the forward pass, gradient pass, and optimizer update as separate phases.

## Topics

### Creating Training Graphs
- [convenience init(graphObjects: [MLCGraph], lossLayer: MLCLayer?, optimizer: MLCOptimizer?)](./mlctraininggraph/init%28graphobjects,losslayer,optimizer%29.md)
  Creates a training graph with the layers from the graph objects, loss layer, and optimizer you specify.
- [Optimizers](./optimizers.md)
  Create an optimizer to use with the training graph.
- [class MLCTensorParameter](./mlctensorparameter.md)
  A tensor parameter object.
### Preparing Training Graphs
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?) -> Bool](./mlctraininggraph/addinputs%28_,losslabels%29.md)
  Adds the inputs and loss label inputs that you specify to the training graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](./mlctraininggraph/addinputs%28_,losslabels,losslabelweights%29.md)
  Adds the inputs, loss labels, and loss label weights that you specify to the training graph.
- [func addOutputs([String : MLCTensor]) -> Bool](./mlctraininggraph/addoutputs%28_%29.md)
  Adds the outputs to the training graph you specify.
- [func stopGradient(for: [MLCTensor]) -> Bool](./mlctraininggraph/stopgradient%28for%29.md)
  Adds the tensors that you specify, to indicate which contributions the graph excludes when computing gradients during gradient pass.
- [func compileOptimizer(MLCOptimizer) -> Bool](./mlctraininggraph/compileoptimizer%28_%29.md)
  Compiles the optimizer to use with a training graph you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](./mlctraininggraph/compile%28options,device%29.md)
  Compiles the training graph for the options and device you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](./mlctraininggraph/compile%28options,device,inputtensors,inputtensorsdata%29.md)
  Compiles the training graph for the options, device, and input tensors you specify.
- [func link(with: [MLCTrainingGraph]) -> Bool](./mlctraininggraph/link%28with%29.md)
  Links the training graphs you specify.
- [func allocateUserGradient(for: MLCTensor) -> MLCTensor?](./mlctraininggraph/allocateusergradient%28for%29.md)
  Allocates an entry for a gradient for the result tensor you specify.
- [struct MLCGraphCompilationOptions](./mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.
### Executing Training Iterations
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlctraininggraph/execute%28inputsdata,losslabelsdata,losslabelweightsdata,batchsize,options,completionhandler%29.md)
  Executes the training graph with the input data, batch size, execution options, and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlctraininggraph/execute%28inputsdata,losslabelsdata,losslabelweightsdata,outputsdata,batchsize,options,completionhandler%29.md)
  Executes the training graph with the input data, output data, batch size, execution options, and completion handler that you specify.
- [func synchronizeUpdates()](./mlctraininggraph/synchronizeupdates%28%29.md)
  Synchronizes updates from device memory.
- [func setTrainingTensorParameters([MLCTensorParameter]) -> Bool](./mlctraininggraph/settrainingtensorparameters%28_%29.md)
  Sets the input tensor parameters, which the optimizer then updates.
- [struct MLCExecutionOptions](./mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](./mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.
### Executing Forward, Gradient, and Optimizer Updates
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlctraininggraph/executeforward%28batchsize,options,completionhandler%29.md)
  Executes the forward pass of the training graph with the batch size, execution options, and completion handler you specify.
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlctraininggraph/executeforward%28batchsize,options,outputsdata,completionhandler%29.md)
  Executes the forward pass of the training graph with the batch size, execution options, output data, and completion handler you specify.
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?) async throws -> (result: MLCTensor?, executionTime: TimeInterval)](./mlctraininggraph/executeforward%28batchsize,options,outputsdata%29.md)
  Executes the forward pass of the training graph with the batch size, execution options, and output data you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlctraininggraph/executegradient%28batchsize,options,completionhandler%29.md)
  Executes the gradient pass of the training graph with the batch size, execution options, and completion handler you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlctraininggraph/executegradient%28batchsize,options,outputsdata,completionhandler%29.md)
  Executes the gradient pass of the training graph with the batch size, execution options, output data, and completion handler you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?) async throws -> TimeInterval](./mlctraininggraph/executegradient%28batchsize,options,outputsdata%29.md)
  Executes the gradient pass of the training graph with the batch size, execution options, and output data you specify.
- [func executeOptimizerUpdate(options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./mlctraininggraph/executeoptimizerupdate%28options,completionhandler%29.md)
  Executes the optimizer update pass of the training graph with the execution options and completion handler you specify.
- [func executeOptimizerUpdate(options: MLCExecutionOptions) async throws -> TimeInterval](./mlctraininggraph/executeoptimizerupdate%28options%29.md)
  Executes the optimizer update pass of the training graph with the execution options you specify.
- [func synchronizeUpdates()](./mlctraininggraph/synchronizeupdates%28%29.md)
  Synchronizes updates from device memory.
- [func setTrainingTensorParameters([MLCTensorParameter]) -> Bool](./mlctraininggraph/settrainingtensorparameters%28_%29.md)
  Sets the input tensor parameters, which the optimizer then updates.
- [struct MLCExecutionOptions](./mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](./mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.
### Inspecting Training Graphs
- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?, with: MLCTensor) -> Bool](./mlctraininggraph/bindoptimizerdata%28_,devicedata,with%29.md)
  Associates the optimizer and device data you specify along with the tensor.
- [var optimizer: MLCOptimizer?](./mlctraininggraph/optimizer.md)
  The optimizer to use with the training graph.
- [var deviceMemorySize: Int](./mlctraininggraph/devicememorysize.md)
  The device memory size in bytes for all intermediate tensors for forward, gradient passes, and optimizer updates for all layers in the training graph.
- [func gradientTensor(forInput: MLCTensor) -> MLCTensor?](./mlctraininggraph/gradienttensor%28forinput%29.md)
  Gets the gradient tensor for the input tensor you specify.
- [func sourceGradientTensors(for: MLCLayer) -> [MLCTensor]](./mlctraininggraph/sourcegradienttensors%28for%29.md)
  Gets the source gradient tensors for the layer in the training graph you specify.
- [func resultGradientTensors(for: MLCLayer) -> [MLCTensor]](./mlctraininggraph/resultgradienttensors%28for%29.md)
  Gets the result gradient tensors for the layer in the training graph you specify.
- [func gradientData(forParameter: MLCTensor, layer: MLCLayer) -> Data?](./mlctraininggraph/gradientdata%28forparameter,layer%29.md)
  Gets the gradient data for the trainable parameter and associated layer you specify.

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
- [class MLCInferenceGraph](./mlcinferencegraph.md)
  An inference graph created from one or more MLCGraph instances plus additional layers added directly to the inference graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph)*