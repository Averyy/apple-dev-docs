# imageFrameStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The style of frame that appears around the image.

**Availability**:
- macOS

## Declaration

```swift
var imageFrameStyle: NSImageView.FrameStyle { get set }
```

```objc
@property NSImageFrameStyle imageFrameStyle;
```

## Discussion

The default value of this property is [`NSImageView.FrameStyle.none`](./framestyle/none.md).

## See Also

### Specifying the visual characteristics
- [var imageAlignment: NSImageAlignment](./imagealignment.md)
  The alignment of the cell’s image inside the image view.
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.
- [var animates: Bool](./animates.md)
  A Boolean value indicating whether the image view automatically plays animated images.
- [var contentTintColor: NSColor?](./contenttintcolor.md)
  A tint color to be used when rendering template image content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/imageframestyle)*