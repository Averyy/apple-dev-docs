# tileBuffers

**Framework**: Metal  
**Kind**: property

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

#### Discussion

This property returns an array of [`MTLPipelineBufferDescriptor`](mtlpipelinebufferdescriptor.md) objects, with each array index corresponding to the same index in the buffer argument table for the render pipeline’s tile shader.

## See Also

- [var tileFunction: any MTLFunction](mtltilerenderpipelinedescriptor/tilefunction.md)
  The compute kernel or fragment function the pipeline calls.
- [var maxCallStackDepth: Int](mtltilerenderpipelinedescriptor/maxcallstackdepth.md)
  The maximum function call depth from the top-most shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/tilebuffers)*