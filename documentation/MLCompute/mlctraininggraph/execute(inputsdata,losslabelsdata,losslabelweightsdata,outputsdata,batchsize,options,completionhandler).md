# execute(inputsData:lossLabelsData:lossLabelWeightsData:outputsData:batchSize:options:completionHandler:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Executes the training graph with the input data, output data, batch size, execution options, and completion handler that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions = [], completionHandler: MLCGraphCompletionHandler? = nil) -> Bool
```

```objc
- (BOOL) executeWithInputsData:(NSDictionary<NSString *,MLCTensorData *> *) inputsData lossLabelsData:(NSDictionary<NSString *,MLCTensorData *> *) lossLabelsData lossLabelWeightsData:(NSDictionary<NSString *,MLCTensorData *> *) lossLabelWeightsData outputsData:(NSDictionary<NSString *,MLCTensorData *> *) outputsData batchSize:(NSUInteger) batchSize options:(MLCExecutionOptions) options completionHandler:(MLCGraphCompletionHandler) completionHandler;
```

#### Return Value

`true` if the execution was successful.

#### Discussion

When you execute a training iteration, if you specified an optimizer when you created the graph, the framework applies the optimizer update.

For variable length sequences for LSTMs/RNNs, use the key “`sortedSequenceLength`” and pass in tensor data created by using one of the [`MLCTensor`](../mlctensor.md) sequence length initializers as the value.

If you include [`synchronous`](../mlcexecutionoptions/synchronous.md) in `options`, the execution method only returns after the graph has finished execution. Otherwise, the execution method returns once the framework enqueues the graph for execution. However, the completion handler is still not called until after the graph has finished execution.

## Parameters

- `inputsData`: A dictionary that contains input data.
- `lossLabelsData`: A dictionary that contains loss labels data.
- `lossLabelWeightsData`: A dictionary that contains loss label weights data.
- `outputsData`: A dictionary that contains output data.
- `batchSize`: The batch size.
- `options`: The execution options.
- `completionHandler`: The completion handler.

## See Also

### Executing Training Iterations
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](./execute%28inputsdata,losslabelsdata,losslabelweightsdata,batchsize,options,completionhandler%29.md)
  Executes the training graph with the input data, batch size, execution options, and completion handler you specify.
- [func synchronizeUpdates()](./synchronizeupdates%28%29.md)
  Synchronizes updates from device memory.
- [func setTrainingTensorParameters([MLCTensorParameter]) -> Bool](./settrainingtensorparameters%28_%29.md)
  Sets the input tensor parameters, which the optimizer then updates.
- [struct MLCExecutionOptions](../mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](../mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:completionhandler:))*