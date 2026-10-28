# imageAlignment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The alignment of the cell’s image inside the image view.

**Availability**:
- macOS

## Declaration

```swift
var imageAlignment: NSImageAlignment { get set }
```

```objc
@property NSImageAlignment imageAlignment;
```

## Discussion

The default value of this property is [`NSImageAlignment.alignCenter`](../nsimagealignment/aligncenter.md).

## See Also

### Specifying the visual characteristics
- [var imageFrameStyle: NSImageView.FrameStyle](./imageframestyle.md)
  The style of frame that appears around the image.
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.
- [var animates: Bool](./animates.md)
  A Boolean value indicating whether the image view automatically plays animated images.
- [var contentTintColor: NSColor?](./contenttintcolor.md)
  A tint color to be used when rendering template image content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/imagealignment)*