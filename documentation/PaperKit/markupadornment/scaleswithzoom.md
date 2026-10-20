# scalesWithZoom

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the adornment scales with the zoom level or remains fixed in the base coordinate system.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var scalesWithZoom: Bool
```

#### Discussion

When this value is `true`, the adornment image adjusts to the zoom scale of the `PaperMarkupViewController`. When `false`, the adornment image remains fixed in the base coordinate system.

## See Also

### Controlling interactions
- [MarkupAdornment.DragRegion](./dragregion-swift.struct.md)
  The movement behavior and interaction constraints for a markup adornment.
- [var dragRegion: MarkupAdornment.DragRegion](./dragregion-swift.property.md)
  The constraints that define where a person can drag this adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/scaleswithzoom)*