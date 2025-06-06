# skipWritingInputDataToDevice

**Framework**: ML Compute  
**Kind**: property

The option to skip writing input data to device memory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
static var skipWritingInputDataToDevice: MLCExecutionOptions { get }
```

#### Discussion

Include this option to prevent writing the input tensors to device memory associated with these tensors when the framework executes the graph.

## See Also

- [init(rawValue: UInt64)](mlcexecutionoptions/init(rawvalue:).md)
  Creates an execution option with the specified raw value.
- [static var synchronous: MLCExecutionOptions](mlcexecutionoptions/synchronous.md)
  The option to execute the graph synchronously.
- [static var profiling: MLCExecutionOptions](mlcexecutionoptions/profiling.md)
  The option to return profiling information in the callback before returning from execution.
- [static var perLayerProfiling: MLCExecutionOptions](mlcexecutionoptions/perlayerprofiling.md)
  The option to enable additional per-layer profiling information using signposts.
- [static var forwardForInference: MLCExecutionOptions](mlcexecutionoptions/forwardforinference.md)
  The option to execute the forward pass for inference only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcexecutionoptions/skipwritinginputdatatodevice)*