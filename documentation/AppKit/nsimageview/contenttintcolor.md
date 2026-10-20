# contentTintColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A tint color to be used when rendering template image content.

**Availability**:
- macOS 10.14+

## Declaration

```swift
@NSCopying
var contentTintColor: NSColor? { get set }
```

```objc
@property (copy, nullable) NSColor * contentTintColor;
```

#### Discussion

This color may be combined with other effects to produce a theme-appropriate rendition of the template image. A `nil` value indicates the standard set of effects without color modification. The default value is `nil`.

## See Also

### Specifying the visual characteristics
- [var imageFrameStyle: NSImageView.FrameStyle](./imageframestyle.md)
  The style of frame that appears around the image.
- [var imageAlignment: NSImageAlignment](./imagealignment.md)
  The alignment of the cell’s image inside the image view.
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.
- [var animates: Bool](./animates.md)
  A Boolean value indicating whether the image view automatically plays animated images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/contenttintcolor)*