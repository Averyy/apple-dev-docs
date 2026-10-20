# candidateRects

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Rectangles that define the specific portions of text to highlight.

**Availability**:
- macOS 15.2+

## Declaration

```swift
var candidateRects: [NSValue] { get }
```

```objc
@property (readonly) NSArray<NSValue *> * candidateRects;
```

#### Discussion

At initialization time, you set this property to an array of [`NSValue`](../../Foundation/nsvalue.md) objects, each of which contains an [`NSRect`](../../Foundation/nsrect.md) in the coordinate space of the target view. Each rectangle contains a bounding rectangle for text that is part of the preview. When applying visual effects, the system adds highlights only to the text in the specified rectangles.

## See Also

### Getting the preview details
- [var previewImage: CGImage](./previewimage.md)
  The image that contains the requested text from your view.
- [var presentationFrame: NSRect](./presentationframe.md)
  The frame rectangle that places the preview image directly over the matching text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextpreview/candidaterects)*