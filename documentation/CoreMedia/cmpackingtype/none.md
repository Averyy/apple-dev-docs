# CMPackingType.none

**Framework**: Core Media  
**Kind**: case

Each frame contains only a single image, and isn’t frame-packed.

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
case none
```

#### Discussion

This is the default frame-packing type for 3D video.

## See Also

- [CMPackingType.sideBySide](cmpackingtype/sidebyside.md)
  The video contains packed frames that have a left eye image on the left and right eye image on the right.
- [CMPackingType.overUnder](cmpackingtype/overunder.md)
  The video contains packed frames that have a left eye image on the top and right eye image on the bottom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmpackingtype/none)*