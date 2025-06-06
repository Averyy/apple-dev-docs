# threadgroupSizeMatchesTileSize

**Framework**: Metal  
**Kind**: property

A Boolean value that indicates whether all threadgroups for this pipeline completely cover tiles.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var threadgroupSizeMatchesTileSize: Bool { get set }
```

#### Discussion

Metal can optimize code generation when the threadgroup and tile sizes match.

## See Also

- [var rasterSampleCount: Int](mtltilerenderpipelinedescriptor/rastersamplecount.md)
  The number of samples in each fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/threadgroupsizematchestilesize)*