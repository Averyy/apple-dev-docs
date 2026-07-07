# scalesWithZoom

**Framework**: PaperKit  
**Kind**: property

A Boolean value that indicates whether the adornment scales with the zoom level or remains fixed in the base coordinate system.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var scalesWithZoom: Bool
```

#### Discussion

When this value is `true`, the adornment image adjusts to the zoom scale of the `PaperMarkupViewController`. When `false`, the adornment image remains fixed in the base coordinate system.

## See Also

- [MarkupAdornment.DragRegion](markupadornment/dragregion-swift.struct.md)
  The movement behavior and interaction constraints for a markup adornment.
- [var dragRegion: MarkupAdornment.DragRegion](markupadornment/dragregion-swift.property.md)
  The constraints that define where a person can drag this adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/scaleswithzoom)*