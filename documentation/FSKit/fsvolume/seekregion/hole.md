# FSVolume.SeekRegion.hole

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

Seek the next hole region.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case hole
```

```c
FSSeekRegionHole
```

#### Discussion

When there are no more hole regions past the supplied `offset`, the current file size (end-of-file offset) should be returned.

## See Also

### Seek region types
- [FSVolume.SeekRegion.data](./data.md)
  Seek the next data region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/seekregion/hole)*