# perLayerProfiling

**Framework**: ML Compute  
**Kind**: property  
**Role**: Type Property

The option to enable additional per-layer profiling information using signposts.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
static var perLayerProfiling: MLCExecutionOptions { get }
```

```c
MLCExecutionOptionsPerLayerProfiling
```

#### Discussion

Visualize the layer information using the Logging profiling template in Instruments. This information may not be available for all [ML Compute](../MLCompute.md) devices.

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
- [static var forwardForInference: MLCExecutionOptions](./forwardforinference.md)
  The option to execute the forward pass for inference only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcexecutionoptions/perlayerprofiling)*