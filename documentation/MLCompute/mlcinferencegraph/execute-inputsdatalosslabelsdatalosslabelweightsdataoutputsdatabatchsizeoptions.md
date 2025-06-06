# execute(inputsData:lossLabelsData:lossLabelWeightsData:outputsData:batchSize:options:)

**Framework**: ML Compute  
**Kind**: method

Executes the inference graph with the input and output data, batch size, and execution options you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
@discardableResult
func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]? = nil, lossLabelWeightsData: [String : MLCTensorData]? = nil, outputsData: [String : MLCTensorData]? = nil, batchSize: Int, options: MLCExecutionOptions = []) async throws -> (result: MLCTensor?, executionTime: TimeInterval)
```

#### Return Value

The result tensor, if any, and the execution time if you specify [`profiling`](mlcexecutionoptions/profiling.md).

## Parameters

- `inputsData`: A dictionary that contains input data.
- `lossLabelsData`: A dictionary that contains loss label data.
- `lossLabelWeightsData`: A dictionary that contains loss label weight data.
- `outputsData`: A dictionary that contains output data.
- `batchSize`: The batch size.
- `options`: The execution options.

## See Also

- [func execute(inputsData: [String : MLCTensorData], batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the inputs data, batch size, execution options, and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:outputsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the inputs and outputs data, batch size, execution options, and completion handler that you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the input data, batch size, execution options and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the input and output data, batch size, execution options, and completion handler that you specify.
- [struct MLCExecutionOptions](mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinferencegraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:))*