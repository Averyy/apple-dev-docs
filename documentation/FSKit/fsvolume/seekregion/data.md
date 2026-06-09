# FSVolume.SeekRegion.data

**Framework**: FSKit  
**Kind**: case

Seek the next data region.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
case data
```

#### Discussion

When there are no more data regions past the supplied `offset`, an error code `ENXIO` should be returned.

## See Also

- [FSVolume.SeekRegion.hole](fsvolume/seekregion/hole.md)
  Seek the next hole region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/seekregion/data)*