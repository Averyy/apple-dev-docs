# MLCGraphCompletionHandler

**Framework**: ML Compute  
**Kind**: typealias

A callback completion handler you execute when a graph finishes execution.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
typealias MLCGraphCompletionHandler = (MLCTensor?, (any Error)?, TimeInterval) -> Void
```

## Parameters

- `resultTensor`: The result tensor.
- `error`: An error if one occured, otherwise  .
- `executionTime`: The execution time.

## See Also

- [func execute(inputsData: [String : MLCTensorData], batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the inputs data, batch size, execution options, and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:outputsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the inputs and outputs data, batch size, execution options, and completion handler that you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the input data, batch size, execution options and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlcinferencegraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:completionhandler:).md)
  Executes the inference graph with the input and output data, batch size, execution options, and completion handler that you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions) async throws -> (result: MLCTensor?, executionTime: TimeInterval)](mlcinferencegraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:).md)
  Executes the inference graph with the input and output data, batch size, and execution options you specify.
- [struct MLCExecutionOptions](mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompletionhandler)*