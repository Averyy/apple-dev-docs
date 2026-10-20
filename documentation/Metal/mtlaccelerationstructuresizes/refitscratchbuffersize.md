# refitScratchBufferSize

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The amount of scratch memory, in bytes, the GPU device needs to refit the acceleration structure.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var refitScratchBufferSize: Int
```

```c
NSUInteger refitScratchBufferSize;
```

#### Discussion

This value can be zero, which indicates that refitting the acceleration structure doesn’t require a scratch buffer.

## See Also

### Retrieving the sizes
- [var accelerationStructureSize: Int](./accelerationstructuresize.md)
  The size of the acceleration structure, in bytes.
- [var buildScratchBufferSize: Int](./buildscratchbuffersize.md)
  The amount of scratch memory, in bytes, the GPU devices needs to build the acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuresizes/refitscratchbuffersize)*