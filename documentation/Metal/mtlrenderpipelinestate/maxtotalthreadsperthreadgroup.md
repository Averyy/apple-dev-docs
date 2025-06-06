# maxTotalThreadsPerThreadgroup

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The largest number of threads the pipeline state can have in a single tile shader threadgroup.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var maxTotalThreadsPerThreadgroup: Int { get }
```

## See Also

- [var threadgroupSizeMatchesTileSize: Bool](mtlrenderpipelinestate/threadgroupsizematchestilesize.md)
  A Boolean value that indicates whether the pipeline state needs a threadgroup’s size to equal a tile’s size.
- [var imageblockSampleLength: Int](mtlrenderpipelinestate/imageblocksamplelength.md)
  The memory size, in byes, of the render pipeline’s imageblock for a single sample.
- [func imageblockMemoryLength(forDimensions: MTLSize) -> Int](mtlrenderpipelinestate/imageblockmemorylength(fordimensions:).md)
  Returns the length of an imageblock’s memory for the specified imageblock dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/maxtotalthreadsperthreadgroup)*