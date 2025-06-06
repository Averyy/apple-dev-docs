# perLayerProfiling

**Framework**: ML Compute  
**Kind**: property

The option to enable additional per-layer profiling information using signposts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
static var perLayerProfiling: MLCExecutionOptions { get }
```

#### Discussion

Visualize the layer information using the Logging profiling template in Instruments. This information may not be available for all [`ML Compute`](MLCompute.md) devices.

## See Also

- [init(rawValue: UInt64)](mlcexecutionoptions/init(rawvalue:).md)
  Creates an execution option with the specified raw value.
- [static var skipWritingInputDataToDevice: MLCExecutionOptions](mlcexecutionoptions/skipwritinginputdatatodevice.md)
  The option to skip writing input data to device memory.
- [static var synchronous: MLCExecutionOptions](mlcexecutionoptions/synchronous.md)
  The option to execute the graph synchronously.
- [static var profiling: MLCExecutionOptions](mlcexecutionoptions/profiling.md)
  The option to return profiling information in the callback before returning from execution.
- [static var forwardForInference: MLCExecutionOptions](mlcexecutionoptions/forwardforinference.md)
  The option to execute the forward pass for inference only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcexecutionoptions/perlayerprofiling)*