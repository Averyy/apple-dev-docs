# tileBuffers

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array that contains the buffer mutability options for a render pipeline’s tile function.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var tileBuffers: MTLPipelineBufferDescriptorArray { get }
```

```objc
@property (readonly) MTLPipelineBufferDescriptorArray * tileBuffers;
```

## Discussion

This property returns an array of [`MTLPipelineBufferDescriptor`](../mtlpipelinebufferdescriptor.md) objects, with each array index corresponding to the same index in the buffer argument table for the render pipeline’s tile shader.

## See Also

### Specifying graphics functions and associated data
- [var tileFunction: any MTLFunction](./tilefunction.md)
  The compute kernel or fragment function the pipeline calls.
- [var maxCallStackDepth: Int](./maxcallstackdepth.md)
  The maximum call stack depth for indirect function calls in tile shaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/tilebuffers)*