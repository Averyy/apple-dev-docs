# previewImage

**Framework**: AppKit  
**Kind**: property

The image that contains the requested text from your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
var previewImage: CGImage { get }
```

#### Discussion

You specify this image at initialization time. The system uses it to implement any visual effects involving your view’s text. Create the image with your text on a transparent background.

## See Also

- [var presentationFrame: NSRect](nstextpreview/presentationframe.md)
  The frame rectangle that places the preview image directly over the matching text.
- [var candidateRects: [NSValue]](nstextpreview/candidaterects.md)
  Rectangles that define the specific portions of text to highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextpreview/previewimage)*