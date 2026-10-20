# CMPackingType.sideBySide

**Framework**: Core Media  
**Kind**: case  
**Role**: Case

The video contains packed frames that have a left eye image on the left and right eye image on the right.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case sideBySide
```

```c
kCMPackingType_SideBySide
```

#### Discussion

For side-by-side packed frames, the width of a frame in video data is twice as wide as the video displayed.

## See Also

### Frame Arrangement
- [CMPackingType.none](./none.md)
  Each frame contains only a single image, and isn’t frame-packed.
- [CMPackingType.overUnder](./overunder.md)
  The video contains packed frames that have a left eye image on the top and right eye image on the bottom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmpackingtype/sidebyside)*