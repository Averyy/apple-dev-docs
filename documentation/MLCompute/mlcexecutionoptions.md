# MLCExecutionOptions

**Framework**: ML Compute  
**Kind**: struct

A bitmask that specifies the options you use when executing a graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
struct MLCExecutionOptions
```

## Topics

### Execution Options
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
- [static var forwardForInference: MLCExecutionOptions](mlcexecutionoptions/forwardforinference.md)
  The option to execute the forward pass for inference only.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [typealias MLCGraphCompletionHandler](mlcgraphcompletionhandler.md)
  A callback completion handler you execute when a graph finishes execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcexecutionoptions)*