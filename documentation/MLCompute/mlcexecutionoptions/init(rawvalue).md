# init(rawValue:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an execution option with the specified raw value.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
init(rawValue: UInt64)
```

## Parameters

- `rawValue`: The bitmask raw value.

## See Also

### Execution Options
- [static var skipWritingInputDataToDevice: MLCExecutionOptions](./skipwritinginputdatatodevice.md)
  The option to skip writing input data to device memory.
- [static var synchronous: MLCExecutionOptions](./synchronous.md)
  The option to execute the graph synchronously.
- [static var profiling: MLCExecutionOptions](./profiling.md)
  The option to return profiling information in the callback before returning from execution.
- [static var perLayerProfiling: MLCExecutionOptions](./perlayerprofiling.md)
  The option to enable additional per-layer profiling information using signposts.
- [static var forwardForInference: MLCExecutionOptions](./forwardforinference.md)
  The option to execute the forward pass for inference only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcexecutionoptions/init(rawvalue:))*