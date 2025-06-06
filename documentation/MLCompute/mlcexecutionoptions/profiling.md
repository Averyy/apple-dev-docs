# profiling

**Framework**: ML Compute  
**Kind**: property

The option to return profiling information in the callback before returning from execution.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
static var profiling: MLCExecutionOptions { get }
```

#### Discussion

Include this option to return profiling information in the graph execute completion handler callback, including device execution time.

## See Also

- [init(rawValue: UInt64)](mlcexecutionoptions/init(rawvalue:).md)
  Creates an execution option with the specified raw value.
- [static var skipWritingInputDataToDevice: MLCExecutionOptions](mlcexecutionoptions/skipwritinginputdatatodevice.md)
  The option to skip writing input data to device memory.
- [static var synchronous: MLCExecutionOptions](mlcexecutionoptions/synchronous.md)
  The option to execute the graph synchronously.
- [static var perLayerProfiling: MLCExecutionOptions](mlcexecutionoptions/perlayerprofiling.md)
  The option to enable additional per-layer profiling information using signposts.
- [static var forwardForInference: MLCExecutionOptions](mlcexecutionoptions/forwardforinference.md)
  The option to execute the forward pass for inference only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcexecutionoptions/profiling)*