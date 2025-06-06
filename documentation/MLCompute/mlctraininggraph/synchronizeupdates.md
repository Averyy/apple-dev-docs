# synchronizeUpdates()

**Framework**: ML Compute  
**Kind**: method

Synchronizes updates from device memory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func synchronizeUpdates()
```

#### Discussion

This method synchronizes the weights/biases from convolution, fully connected and LSTM layers, and tensor parameters, from device memory to host memory.

## See Also

- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:batchsize:options:completionhandler:).md)
  Executes the training graph with the input data, batch size, execution options, and completion handler you specify.
- [func execute(inputsData: [String : MLCTensorData], lossLabelsData: [String : MLCTensorData]?, lossLabelWeightsData: [String : MLCTensorData]?, outputsData: [String : MLCTensorData]?, batchSize: Int, options: MLCExecutionOptions, completionHandler: MLCGraphCompletionHandler?) -> Bool](mlctraininggraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:outputsdata:batchsize:options:completionhandler:).md)
  Executes the training graph with the input data, output data, batch size, execution options, and completion handler that you specify.
- [func setTrainingTensorParameters([MLCTensorParameter]) -> Bool](mlctraininggraph/settrainingtensorparameters(_:).md)
  Sets the input tensor parameters, which the optimizer then updates.
- [struct MLCExecutionOptions](mlcexecutionoptions.md)
  A bitmask that specifies the options you use when executing a graph.
- [typealias MLCGraphCompletionHandler](mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/synchronizeupdates())*