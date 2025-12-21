# animates

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the image view automatically plays animated images.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var animates: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the image view plays animated images automatically using the timing and looping characteristics stored in the image data. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

Decoding an animated GIF file is the only way to create an animated [`NSImage`](nsimage.md) object. If the image view has been assigned an image that was created from animated GIF data, setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) enables automatic playback of the animation. If this property is set to [`false`](https://developer.apple.com/documentation/Swift/false), only the first frame of an animated image is displayed.

Loading an animated GIF file using an [`NSImage`](nsimage.md) object produces an image that uses an [`NSBitmapImageRep`](nsbitmapimagerep.md) object. The [`currentFrame`](nsbitmapimagerep/propertykey/currentframe.md), [`currentFrameDuration`](nsbitmapimagerep/propertykey/currentframeduration.md), and [`frameCount`](nsbitmapimagerep/propertykey/framecount.md) properties of the bitmap image representation determine the timing and looping characteristics of the animation. For more information, see [`NSBitmapImageRep`](nsbitmapimagerep.md).

## See Also

- [var imageFrameStyle: NSImageView.FrameStyle](nsimageview/imageframestyle.md)
  The style of frame that appears around the image.
- [var imageAlignment: NSImageAlignment](nsimageview/imagealignment.md)
  The alignment of the cell’s image inside the image view.
- [var imageScaling: NSImageScaling](nsimageview/imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.
- [var contentTintColor: NSColor?](nsimageview/contenttintcolor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/animates)*