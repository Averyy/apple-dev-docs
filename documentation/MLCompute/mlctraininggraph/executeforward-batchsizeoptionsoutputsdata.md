# executeForward(batchSize:options:outputsData:)

**Framework**: ML Compute  
**Kind**: method

Executes the forward pass of the training graph with the batch size, execution options, and output data you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
@discardableResult
func executeForward(batchSize: Int, options: MLCExecutionOptions = [], outputsData: [String : MLCTensorData]? = nil) async throws -> (result: MLCTensor?, executionTime: TimeInterval)
```

#### Return Value

The result tensor, if any, and the execution time if you specify [`profiling`](mlcexecutionoptions/profiling.md).

## Parameters

- `batchSize`: The batch size.
- `options`: The execution options.
- `outputsData`: A dictionary that contains output data.

## See Also

- [func executeForward(batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/executeforward(batchsize:options:completionhandler:).md)
  Executes the forward pass of the training graph with the batch size, execution options, and completion handler you specify.
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/executeforward(batchsize:options:outputsdata:completionhandler:).md)
  Executes the forward pass of the training graph with the batch size, execution options, output data, and completion handler you specify.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/executeforward(batchsize:options:outputsdata:))*