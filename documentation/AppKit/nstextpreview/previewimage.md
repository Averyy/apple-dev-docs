# previewImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image that contains the requested text from your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var previewImage: CGImage { get }
```

```objc
@property (readonly) CGImageRef previewImage;
```

#### Discussion

You specify this image at initialization time. The system uses it to implement any visual effects involving your view’s text. Create the image with your text on a transparent background.

## See Also

### Getting the preview details
- [var presentationFrame: NSRect](./presentationframe.md)
  The frame rectangle that places the preview image directly over the matching text.
- [var candidateRects: [NSValue]](./candidaterects.md)
  Rectangles that define the specific portions of text to highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextpreview/previewimage)*