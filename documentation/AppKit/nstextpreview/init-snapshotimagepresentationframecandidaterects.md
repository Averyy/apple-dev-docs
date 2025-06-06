# init(snapshotImage:presentationFrame:candidateRects:)

**Framework**: AppKit  
**Kind**: init

Creates a text preview using the specified image and rectangles that indicate the portions of text to highlight.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
init(snapshotImage: CGImage, presentationFrame: NSRect, candidateRects: [NSValue])
```

## Parameters

- `snapshotImage`: An image that contains the requested text from your view.   Create the image using a transparent background and the current rendering   attributes for your text.
- `presentationFrame`: A rectangle in the coordinate space of your text view.   The system uses this rectangle to place your image precisely over your   view’s actual text. Set its size to the size of your snapshot image, and   set its origin to the point that allows the system to place your image   directly over the text.
- `candidateRects`: An array of    objects, each of which contains an    in the coordinate space of your text view. Each rectangle contains a   bounding rectangle for text that is part of the preview. When applying   visual effects, the system adds highlights only to the text in the specified rectangles.

## See Also

- [convenience init(snapshotImage: CGImage, presentationFrame: NSRect)](nstextpreview/init(snapshotimage:presentationframe:).md)
  Creates a text preview using the specified image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextpreview/init(snapshotimage:presentationframe:candidaterects:))*