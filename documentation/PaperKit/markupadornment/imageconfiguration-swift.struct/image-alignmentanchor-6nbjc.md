# image(_:alignmentAnchor:)

**Framework**: PaperKit  
**Kind**: method

Creates an image configuration using a custom image.

## Declaration

```swift
static func image(_ image: NSImage, alignmentAnchor: CGPoint = .zero) -> MarkupAdornment.ImageConfiguration
```

#### Return Value

An `ImageConfiguration` for the custom image.

## Parameters

- `image`: The `NSImage` to display.
- `alignmentAnchor`: The offset from the image center for positioning. Defaults to zero.

## See Also

- [static let `default`: MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/default.md)
  The default image configuration using a pin-shaped system image.
- [static func systemImage(String, tint: UIColor, size: CGSize?, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/systemimage(_:tint:size:alignmentanchor:)-24032.md)
  Creates an image configuration using a system image.
- [static func systemImage(String, tint: NSColor, size: CGSize?, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/systemimage(_:tint:size:alignmentanchor:)-4itb9.md)
  Creates an image configuration using a system image.
- [static func image(UIImage, alignmentAnchor: CGPoint) -> MarkupAdornment.ImageConfiguration](markupadornment/imageconfiguration-swift.struct/image(_:alignmentanchor:)-6ds45.md)
  Creates an image configuration using a custom image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupadornment/imageconfiguration-swift.struct/image(_:alignmentanchor:)-6nbjc)*