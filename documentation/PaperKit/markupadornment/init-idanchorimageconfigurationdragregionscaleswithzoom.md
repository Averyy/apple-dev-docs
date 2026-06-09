# init(id:anchor:imageConfiguration:dragRegion:scalesWithZoom:)

**Framework**: PaperKit  
**Kind**: init

Creates a new markup adornment with the specified configuration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(id: UUID = UUID(), anchor: MarkupAdornment.Anchor, imageConfiguration: MarkupAdornment.ImageConfiguration = .default, dragRegion: MarkupAdornment.DragRegion = .canvas, scalesWithZoom: Bool = false)
```

## Parameters

- `id`: A unique identifier for the adornment. Defaults to a new UUID.
- `anchor`: The positioning anchor that determines where the adornment appears.
- `imageConfiguration`: The visual configuration for the adornment image. Defaults to a pin icon.
- `dragRegion`: The movement constraints for the adornment. Defaults to draggable within the canvas.
- `scalesWithZoom`: A Boolean value that indicates whether the adornment scales with the zoom level. Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/init(id:anchor:imageconfiguration:dragregion:scaleswithzoom:))*