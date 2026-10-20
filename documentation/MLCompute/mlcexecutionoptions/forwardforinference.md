# forwardForInference

**Framework**: ML Compute  
**Kind**: property  
**Role**: Type Property

The option to execute the forward pass for inference only.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
static var forwardForInference: MLCExecutionOptions { get }
```

```c
MLCExecutionOptionsForwardForInference
```

#### Discussion

If you include this option and execute a training graph using one of the `execute` methods, such as [`execute(inputsData:lossLabelsData:lossLabelWeightsData:batchSize:options:completionHandler:)`](../mlctraininggraph/execute%28inputsdata,losslabelsdata,losslabelweightsdata,batchsize,options,completionhandler%29.md), the framework only executes the forward pass of the training graph, and it executes that forward pass for inference only.

If you include this option and execute a training graph using one of the `executeForward` methods, such as [`executeForward(batchSize:options:completionHandler:)`](../mlctraininggraph/executeforward%28batchsize,options,completionhandler%29.md), the framework executes the forward pass for inference only.

## See Also

### Execution Options
- [init(rawValue: UInt64)](./init%28rawvalue%29.md)
  Creates an execution option with the specified raw value.
- [static var skipWritingInputDataToDevice: MLCExecutionOptions](./skipwritinginputdatatodevice.md)
  The option to skip writing input data to device memory.
- [static var synchronous: MLCExecutionOptions](./synchronous.md)
  The option to execute the graph synchronously.
- [static var profiling: MLCExecutionOptions](./profiling.md)
  The option to return profiling information in the callback before returning from execution.
- [static var perLayerProfiling: MLCExecutionOptions](./perlayerprofiling.md)
  The option to enable additional per-layer profiling information using signposts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcexecutionoptions/forwardforinference)*