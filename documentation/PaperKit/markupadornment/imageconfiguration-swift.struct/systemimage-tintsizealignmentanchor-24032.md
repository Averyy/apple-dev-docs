# systemImage(_:tint:size:alignmentAnchor:)

**Framework**: PaperKit  
**Kind**: method

Creates an image configuration using a system image.

## Declaration

```swift
static func systemImage(_ name: String, tint: UIColor = .tintColor, size: CGSize? = nil, alignmentAnchor: CGPoint = .zero) -> MarkupAdornment.ImageConfiguration
```

#### Return Value

An `ImageConfiguration` for the system image.

## Parameters

- `name`: The SF Symbol name for the system image.
- `tint`: The color to apply to the image. Defaults to the system tint color.
- `size`: The size of the rendered image in points. Defaults to 48x48.
- `alignmentAnchor`: The offset from the image center for positioning. Defaults to zero.

## See Also

- [static let `default`: MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/default.md)
  The default image configuration using a pin-shaped system image.
- [static func systemImage(String, tint: NSColor, size: CGSize?, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/systemimage(_:tint:size:alignmentanchor:)-4itb9.md)
  Creates an image configuration using a system image.
- [static func image(UIImage, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/image(_:alignmentanchor:)-6ds45.md)
  Creates an image configuration using a custom image.
- [static func image(NSImage, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/image(_:alignmentanchor:)-6nbjc.md)
  Creates an image configuration using a custom image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/imageconfiguration-swift.struct/systemimage(_:tint:size:alignmentanchor:)-24032)*