# FSVolume.SeekRegion.data

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

Seek the next data region.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case data
```

```c
FSSeekRegionData
```

## Discussion

When there are no more data regions past the supplied `offset`, an error code `ENXIO` should be returned.

## See Also

### Seek region types
- [FSVolume.SeekRegion.hole](./hole.md)
  Seek the next hole region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/seekregion/data)*