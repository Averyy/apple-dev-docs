# buildScratchBufferSize

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The amount of scratch memory, in bytes, the GPU devices needs to build the acceleration structure.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var buildScratchBufferSize: Int
```

```c
NSUInteger buildScratchBufferSize;
```

## See Also

### Retrieving the sizes
- [var accelerationStructureSize: Int](./accelerationstructuresize.md)
  The size of the acceleration structure, in bytes.
- [var refitScratchBufferSize: Int](./refitscratchbuffersize.md)
  The amount of scratch memory, in bytes, the GPU device needs to refit the acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuresizes/buildscratchbuffersize)*