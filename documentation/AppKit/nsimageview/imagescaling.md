# imageScaling

**Framework**: AppKit  
**Kind**: property

The scaling mode applied to make the cell’s image fit the frame of the image view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var imageScaling: NSImageScaling { get set }
```

#### Discussion

The default value of this property is [`NSImageScaling.scaleProportionallyDown`](nsimagescaling/scaleproportionallydown.md).

## See Also

- [var imageFrameStyle: NSImageView.FrameStyle](nsimageview/imageframestyle.md)
  The style of frame that appears around the image.
- [var imageAlignment: NSImageAlignment](nsimageview/imagealignment.md)
  The alignment of the cell’s image inside the image view.
- [var animates: Bool](nsimageview/animates.md)
  A Boolean value indicating whether the image view automatically plays animated images.
- [var contentTintColor: NSColor?](nsimageview/contenttintcolor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/imagescaling)*