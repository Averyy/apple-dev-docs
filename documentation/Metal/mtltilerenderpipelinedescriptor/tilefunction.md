# tileFunction

**Framework**: Metal  
**Kind**: property

The compute kernel or fragment function the pipeline calls.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var tileFunction: any MTLFunction { get set }
```

#### Discussion

Kernel-based and fragment-based tile pipeline dispatches act as a barrier against previous draw commands and other dispatches. Kernel-based pipelines wait until all prior access to the tile completes. Fragment-based pipelines wait only until all prior access to the fragment’s location completes.

## See Also

- [var tileBuffers: MTLPipelineBufferDescriptorArray](mtltilerenderpipelinedescriptor/tilebuffers.md)
  An array that contains the buffer mutability options for a render pipeline’s tile function.
- [var maxCallStackDepth: Int](mtltilerenderpipelinedescriptor/maxcallstackdepth.md)
  The maximum function call depth from the top-most shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/tilefunction)*