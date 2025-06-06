# presentationFrame

**Framework**: AppKit  
**Kind**: property

The frame rectangle that places the preview image directly over the matching text.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
var presentationFrame: NSRect { get }
```

#### Discussion

You specify this value at initialization time. The system uses it to position the preview image over the text in your view. Make sure the frame rectangle is in your view’s coordinate space.

## See Also

- [var previewImage: CGImage](nstextpreview/previewimage.md)
  The image that contains the requested text from your view.
- [var candidateRects: [NSValue]](nstextpreview/candidaterects.md)
  Rectangles that define the specific portions of text to highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextpreview/presentationframe)*