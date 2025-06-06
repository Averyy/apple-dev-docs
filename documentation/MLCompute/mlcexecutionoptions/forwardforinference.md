# forwardForInference

**Framework**: ML Compute  
**Kind**: property

The option to execute the forward pass for inference only.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
static var forwardForInference: MLCExecutionOptions { get }
```

#### Discussion

If you include this option and execute a training graph using one of the `execute` methods, such as [`execute(inputsData:lossLabelsData:lossLabelWeightsData:batchSize:options:completionHandler:)`](mlctraininggraph/execute(inputsdata:losslabelsdata:losslabelweightsdata:batchsize:options:completionhandler:).md), the framework only executes the forward pass of the training graph, and it executes that forward pass for inference only.

If you include this option and execute a training graph using one of the `executeForward` methods, such as [`executeForward(batchSize:options:completionHandler:)`](mlctraininggraph/executeforward(batchsize:options:completionhandler:).md), the framework executes the forward pass for inference only.

## See Also

- [init(rawValue: UInt64)](mlcexecutionoptions/init(rawvalue:).md)
  Creates an execution option with the specified raw value.
- [static var skipWritingInputDataToDevice: MLCExecutionOptions](mlcexecutionoptions/skipwritinginputdatatodevice.md)
  The option to skip writing input data to device memory.
- [static var synchronous: MLCExecutionOptions](mlcexecutionoptions/synchronous.md)
  The option to execute the graph synchronously.
- [static var profiling: MLCExecutionOptions](mlcexecutionoptions/profiling.md)
  The option to return profiling information in the callback before returning from execution.
- [static var perLayerProfiling: MLCExecutionOptions](mlcexecutionoptions/perlayerprofiling.md)
  The option to enable additional per-layer profiling information using signposts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcexecutionoptions/forwardforinference)*