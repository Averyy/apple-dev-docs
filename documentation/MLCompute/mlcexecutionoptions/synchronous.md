# synchronous

**Framework**: ML Compute  
**Kind**: property

The option to execute the graph synchronously.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
static var synchronous: MLCExecutionOptions { get }
```

#### Discussion

Include this option to wait until execution of the graph on specified device finishes before returning from the execute method.

## See Also

- [init(rawValue: UInt64)](mlcexecutionoptions/init(rawvalue:).md)
  Creates an execution option with the specified raw value.
- [static var skipWritingInputDataToDevice: MLCExecutionOptions](mlcexecutionoptions/skipwritinginputdatatodevice.md)
  The option to skip writing input data to device memory.
- [static var profiling: MLCExecutionOptions](mlcexecutionoptions/profiling.md)
  The option to return profiling information in the callback before returning from execution.
- [static var perLayerProfiling: MLCExecutionOptions](mlcexecutionoptions/perlayerprofiling.md)
  The option to enable additional per-layer profiling information using signposts.
- [static var forwardForInference: MLCExecutionOptions](mlcexecutionoptions/forwardforinference.md)
  The option to execute the forward pass for inference only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcexecutionoptions/synchronous)*