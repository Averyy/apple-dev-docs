# execute(inputsData:outputsData:batchSize:options:completionHandler:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Executes the inference graph with the inputs and outputs data, batch size, execution options, and completion handler that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func execute(inputsData: [String : MLCTensorData], outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions = [], completionHandler: MLCGraphCompletionHandler? = nil) -> Bool
```

```objc
- (BOOL) executeWithInputsData:(NSDictionary<NSString *,MLCTensorData *> *) inputsData outputsData:(NSDictionary<NSString *,MLCTensorData *> *) outputsData batchSize:(NSUInteger) batchSize options:(MLCExecutionOptions) options completionHandler:(MLCGraphCompletionHandler) completionHandler;
```

#### Return Value

`true` if the execution was successful.

#### Discussion

When executing an inference graph, if an optimizer is specified, the optimizer update is applied.

For variable length sequences for LSTMs/RNNs, use the key `“sortedSequenceLengths”` and pass in tensor data created by using one of the [`MLCTensor`](../mlctensor.md) sequence length initializers as the value.

If [`synchronous`](../mlcexecutionoptions/synchronous.md) is specified in `options`, this method returns after the graph is executed. Otherwise, this method returns after the graph is queued for execution. The completion handler is called after the graph has finished execution.

## Parameters

- `inputsData`: A dictionary that contains input data.
- `outputsData`: A dictionary that contains output data.
- `batchSize`: The batch size.
- `options`: The execution options.
- `completionHandler`: The completion handler.

## See Also

### Executing Inference Graphs
- [func execute(inputsData: [String : MLCTensorData], batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./execute%28inputsdata,batchsize,options,completionhandler%29.md)
  Executes the inference graph with the inputs data, batch size, execution options, and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./execute%28inputsdata,losslabelsdata,losslabelweightsdata,batchsize,options,completionhandler%29.md)
  Executes the inference graph with the input data, batch size, execution options and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./execute%28inputsdata,losslabelsdata,losslabelweightsdata,outputsdata,batchsize,options,completionhandler%29.md)
  Executes the inference graph with the input and output data, batch size, execution options, and completion handler that you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions) async throws -> (result: MLCTensor?, executionTime: TimeInterval)](./execute%28inputsdata,losslabelsdata,losslabelweightsdata,outputsdata,batchsize,options%29.md)
  Executes the inference graph with the input and output data, batch size, and execution options you specify.
- [struct MLCExecutionOptions](../mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](../mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinferencegraph/execute(inputsdata:outputsdata:batchsize:options:completionhandler:))*