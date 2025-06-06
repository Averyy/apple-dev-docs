# maxCallStackDepth

**Framework**: Metal  
**Kind**: property

The maximum function call depth from the top-most shader function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var maxCallStackDepth: Int { get set }
```

#### Discussion

The default value is 1.

## See Also

- [var tileFunction: any MTLFunction](mtltilerenderpipelinedescriptor/tilefunction.md)
  The compute kernel or fragment function the pipeline calls.
- [var tileBuffers: MTLPipelineBufferDescriptorArray](mtltilerenderpipelinedescriptor/tilebuffers.md)
  An array that contains the buffer mutability options for a render pipeline’s tile function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/maxcallstackdepth)*