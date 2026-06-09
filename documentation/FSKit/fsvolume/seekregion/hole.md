# FSVolume.SeekRegion.hole

**Framework**: FSKit  
**Kind**: case

Seek the next hole region.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
case hole
```

#### Discussion

When there are no more hole regions past the supplied `offset`, the current file size (end-of-file offset) should be returned.

## See Also

- [FSVolume.SeekRegion.data](fsvolume/seekregion/data.md)
  Seek the next data region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/seekregion/hole)*