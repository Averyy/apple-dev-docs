# setComputePipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the compute encoder with a pipeline state for subsequent kernel calls.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setComputePipelineState(_ state: any MTLComputePipelineState)
```

#### Discussion

> ❗ **Important**:  Set a compute encoder’s pipeline state before encoding any commands. Encoding commands without an available pipeline state causes an error.

Create your pipeline state through one of the [`MTLDevice`](mtldevice.md) methods in Creating Compute Pipeline States.

A compute pipeline state provides information Metal uses to compile and run encoded commands. You can change the pipeline state at any time, allowing you to encode multiple kernel calls in a single command buffer. Changing the pipeline state doesn’t affect any previously encoded commands.

## Parameters

- `state`: An   instance.

## See Also

- [var dispatchType: MTLDispatchType](mtlcomputecommandencoder/dispatchtype.md)
  The dispatch type to use when submitting compute work to the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setcomputepipelinestate(_:))*