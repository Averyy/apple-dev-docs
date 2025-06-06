# candidateRects

**Framework**: AppKit  
**Kind**: property

Rectangles that define the specific portions of text to highlight.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
var candidateRects: [NSValue] { get }
```

#### Discussion

At initialization time, you set this property to an array of [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) objects, each of which contains an [`NSRect`](https://developer.apple.com/documentation/Foundation/NSRect) in the coordinate space of the target view. Each rectangle contains a bounding rectangle for text that is part of the preview. When applying visual effects, the system adds highlights only to the text in the specified rectangles.

## See Also

- [var previewImage: CGImage](nstextpreview/previewimage.md)
  The image that contains the requested text from your view.
- [var presentationFrame: NSRect](nstextpreview/presentationframe.md)
  The frame rectangle that places the preview image directly over the matching text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextpreview/candidaterects)*