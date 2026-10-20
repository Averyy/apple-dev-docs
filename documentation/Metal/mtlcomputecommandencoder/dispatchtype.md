# dispatchType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The dispatch type to use when submitting compute work to the GPU.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var dispatchType: MTLDispatchType { get }
```

```objc
@property (readonly) MTLDispatchType dispatchType;
```

#### Discussion

You set this property when you create the command encoder, and it doesn’t change for the remainder of the encoding.

See [`makeComputeCommandEncoder(dispatchType:)`](../mtlcommandbuffer/makecomputecommandencoder%28dispatchtype%29.md) for more information.

## See Also

### Configuring the pipeline state
- [func setComputePipelineState(any MTLComputePipelineState)](./setcomputepipelinestate%28_%29.md)
  Configures the compute encoder with a pipeline state for subsequent kernel calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/dispatchtype)*