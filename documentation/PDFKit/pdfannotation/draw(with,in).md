# draw(with:in:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Draws the annotation in a graphics context using page-space coordinates relative to the origin of the specified box.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func draw(with box: PDFDisplayBox, in context: CGContext)
```

```objc
- (void) drawWithBox:(PDFDisplayBox) box inContext:(CGContextRef) context;
```

## Discussion

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## Parameters

- `box`: The display box that represents the rectangle to draw the annotation in, in page-space coordinates.
- `context`: The graphics context to draw the annotation in.

## See Also

### Managing Annotation Drawing and Output
- [var shouldDisplay: Bool](./shoulddisplay.md)
  Returns a Boolean value indicating whether the annotation should be displayed.
- [var shouldPrint: Bool](./shouldprint.md)
  Returns a Boolean value indicating whether the annotation should appear when the document is printed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/draw(with:in:))*