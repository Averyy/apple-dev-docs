# executeForward(batchSize:options:outputsData:completionHandler:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Executes the forward pass of the training graph with the batch size, execution options, output data, and completion handler you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func executeForward(batchSize: Int, options: MLCExecutionOptions = [], outputsData: [String : MLCTensorData]?, completionHandler: MLCGraphCompletionHandler? = nil) -> Bool
```

```objc
- (BOOL) executeForwardWithBatchSize:(NSUInteger) batchSize options:(MLCExecutionOptions) options outputsData:(NSDictionary<NSString *,MLCTensorData *> *) outputsData completionHandler:(MLCGraphCompletionHandler) completionHandler;
```

#### Return Value

`true` if the execution was successful.

## Parameters

- `batchSize`: The batch size.
- `options`: The execution options.
- `outputsData`: A dictionary that contains output data.
- `completionHandler`: The completion handler.

## See Also

### Executing Forward, Gradient, and Optimizer Updates
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./executeforward%28batchsize,options,completionhandler%29.md)
  Executes the forward pass of the training graph with the batch size, execution options, and completion handler you specify.
- [func executeForward(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?) async throws -> (result: MLCTensor?, executionTime: TimeInterval)](./executeforward%28batchsize,options,outputsdata%29.md)
  Executes the forward pass of the training graph with the batch size, execution options, and output data you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./executegradient%28batchsize,options,completionhandler%29.md)
  Executes the gradient pass of the training graph with the batch size, execution options, and completion handler you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?, completionHandler: MLCGraphCompletionHandler?) -> Bool](./executegradient%28batchsize,options,outputsdata,completionhandler%29.md)
  Executes the gradient pass of the training graph with the batch size, execution options, output data, and completion handler you specify.
- [func executeGradient(batchSize: Int, options: MLCExecutionOptions, outputsData: [String : MLCTensorData]?) async throws -> TimeInterval](./executegradient%28batchsize,options,outputsdata%29.md)
  Executes the gradient pass of the training graph with the batch size, execution options, and output data you specify.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/executeforward(batchsize:options:outputsdata:completionhandler:))*