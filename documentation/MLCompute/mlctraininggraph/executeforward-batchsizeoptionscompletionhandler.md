# executeForward(batchSize:options:completionHandler:)

**Framework**: ML Compute  
**Kind**: method

Executes the forward pass of the training graph with the batch size, execution options, and completion handler you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func executeForward(batchSize: Int, options: MLCExecutionOptions = [], completionHandler: MLCGraphCompletionHandler? = nil) -> Bool
```

#### Return Value

`true` if the execution was successful.

## Parameters

- `batchSize`: The batch size.
- `options`: The execution options.
- `completionHandler`: The completion handler.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/executeforward(batchsize:options:completionhandler:))*