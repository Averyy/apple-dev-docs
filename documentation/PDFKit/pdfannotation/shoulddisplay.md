# shouldDisplay

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether the annotation should be displayed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var shouldDisplay: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldDisplay;
```

#### Return Value

[`true`](../../Swift/true.md) if the annotation should be displayed; otherwise [`false`](../../Swift/false.md).

#### Discussion

`PDFPage` respects this flag when drawing.

## See Also

### Managing Annotation Drawing and Output
- [func draw(with: PDFDisplayBox, in: CGContext)](./draw%28with,in%29.md)
  Draws the annotation in a graphics context using page-space coordinates relative to the origin of the specified box.
- [var shouldPrint: Bool](./shouldprint.md)
  Returns a Boolean value indicating whether the annotation should appear when the document is printed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/shoulddisplay)*