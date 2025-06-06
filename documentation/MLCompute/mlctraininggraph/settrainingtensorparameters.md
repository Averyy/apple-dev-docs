# setTrainingTensorParameters(_:)

**Framework**: ML Compute  
**Kind**: method

Sets the input tensor parameters, which the optimizer then updates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func setTrainingTensorParameters(_ parameters: [MLCTensorParameter]) -> Bool
```

#### Return Value

`true` if the operation was successful.

## Parameters

- `parameters`: An array that contains the input tensor parameters.

## See Also

- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:batchsize:options:completionhandler:).md)
  Executes the training graph with the input data, batch size, execution options, and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:completionhandler:).md)
  Executes the training graph with the input data, output data, batch size, execution options, and completion handler that you specify.
- [func synchronizeUpdates()](mlctraininggraph/synchronizeupdates.md)
  Synchronizes updates from device memory.
- [struct MLCExecutionOptions](mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/settrainingtensorparameters(_:))*