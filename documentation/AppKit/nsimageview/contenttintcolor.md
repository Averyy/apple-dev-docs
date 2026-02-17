# contentTintColor

**Framework**: AppKit  
**Kind**: property

A tint color to be used when rendering template image content.

**Availability**:
- macOS 10.14+

## Declaration

```swift
@NSCopying
var contentTintColor: NSColor? { get set }
```

#### Discussion

This color may be combined with other effects to produce a theme-appropriate rendition of the template image. A `nil` value indicates the standard set of effects without color modification. The default value is `nil`.

## See Also

- [var imageFrameStyle: NSImageView.FrameStyle](nsimageview/imageframestyle.md)
  The style of frame that appears around the image.
- [var imageAlignment: NSImageAlignment](nsimageview/imagealignment.md)
  The alignment of the cell’s image inside the image view.
- [var imageScaling: NSImageScaling](nsimageview/imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.
- [var animates: Bool](nsimageview/animates.md)
  A Boolean value indicating whether the image view automatically plays animated images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/contenttintcolor)*