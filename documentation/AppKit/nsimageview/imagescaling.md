# imageScaling

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scaling mode applied to make the cell’s image fit the frame of the image view.

**Availability**:
- macOS

## Declaration

```swift
var imageScaling: NSImageScaling { get set }
```

```objc
@property NSImageScaling imageScaling;
```

## Discussion

The default value of this property is [`NSImageScaling.scaleProportionallyDown`](../nsimagescaling/scaleproportionallydown.md).

## See Also

### Specifying the visual characteristics
- [var imageFrameStyle: NSImageView.FrameStyle](./imageframestyle.md)
  The style of frame that appears around the image.
- [var imageAlignment: NSImageAlignment](./imagealignment.md)
  The alignment of the cell’s image inside the image view.
- [var animates: Bool](./animates.md)
  A Boolean value indicating whether the image view automatically plays animated images.
- [var contentTintColor: NSColor?](./contenttintcolor.md)
  A tint color to be used when rendering template image content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/imagescaling)*