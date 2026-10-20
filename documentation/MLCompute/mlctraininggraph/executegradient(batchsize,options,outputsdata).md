# executeGradient(batchSize:options:outputsData:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Executes the gradient pass of the training graph with the batch size, execution options, and output data you specify.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- tvOS 15.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
@discardableResult
func executeGradient(batchSize: Int, options: MLCExecutionOptions = [], outputsData: [String : MLCTensorData]? = nil) async throws -> TimeInterval
```

#### Return Value

The execution time if you specify [`profiling`](../mlcexecutionoptions/profiling.md).

## Parameters

- `batchSize`: The batch size.
- `options`: The execution options.
- `outputsData`: A dictionary that contains output data.

## See Also

### Executing Forward, Gradient, and Optimizer Updates
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./executeforward%28batchsize,options,completionhandler%29.md)
  Executes the forward pass of the training graph with the batch size, execution options, and completion handler you specify.
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?, completionHandler: MLCGraphCompletionHandler?) -> Bool](./executeforward%28batchsize,options,outputsdata,completionhandler%29.md)
  Executes the forward pass of the training graph with the batch size, execution options, output data, and completion handler you specify.
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?) async throws -> (result: MLCTensor?, executionTime: TimeInterval)](./executeforward%28batchsize,options,outputsdata%29.md)
  Executes the forward pass of the training graph with the batch size, execution options, and output data you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./executegradient%28batchsize,options,completionhandler%29.md)
  Executes the gradient pass of the training graph with the batch size, execution options, and completion handler you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?, completionHandler: MLCGraphCompletionHandler?) -> Bool](./executegradient%28batchsize,options,outputsdata,completionhandler%29.md)
  Executes the gradient pass of the training graph with the batch size, execution options, output data, and completion handler you specify.
- [func executeOptimizerUpdate(options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./executeoptimizerupdate%28options,completionhandler%29.md)
  Executes the optimizer update pass of the training graph with the execution options and completion handler you specify.
- [func executeOptimizerUpdate(options: MLCExecutionOptions) async throws -> TimeInterval](./executeoptimizerupdate%28options%29.md)
  Executes the optimizer update pass of the training graph with the execution options you specify.
- [func synchronizeUpdates()](./synchronizeupdates%28%29.md)
  Synchronizes updates from device memory.
- [func setTrainingTensorParameters([MLCTensorParameter]) -> Bool](./settrainingtensorparameters%28_%29.md)
  Sets the input tensor parameters, which the optimizer then updates.
- [struct MLCExecutionOptions](../mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](../mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/executegradient(batchsize:options:outputsdata:))*