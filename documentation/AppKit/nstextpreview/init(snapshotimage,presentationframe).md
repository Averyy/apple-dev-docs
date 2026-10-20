# init(snapshotImage:presentationFrame:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a text preview using the specified image.

**Availability**:
- macOS 15.2+

## Declaration

```swift
convenience init(snapshotImage: CGImage, presentationFrame: NSRect)
```

```objc
- (instancetype) initWithSnapshotImage:(CGImageRef) snapshotImage presentationFrame:(NSRect) presentationFrame;
```

## Parameters

- `snapshotImage`: An image that contains the requested text from your view. Create the image using a transparent background and the current rendering attributes for your text.
- `presentationFrame`: A rectangle in your frame’s coordinate space. The system uses this rectangle to place your image precisely over your view’s actual text. Set its size to the size of your snapshot image, and set its origin to the point that allows the system to place your image directly over the text.

## See Also

### Creating a text preview
- [init(snapshotImage: CGImage, presentationFrame: NSRect, candidateRects: [NSValue])](./init%28snapshotimage,presentationframe,candidaterects%29.md)
  Creates a text preview using the specified image and rectangles that indicate the portions of text to highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextpreview/init(snapshotimage:presentationframe:))*