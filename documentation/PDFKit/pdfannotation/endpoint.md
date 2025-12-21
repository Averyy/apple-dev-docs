# endPoint

**Framework**: PDFKit  
**Kind**: property

The point where a line ends, in annotation-space coordinates.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var endPoint: NSPoint { get set }
```

## See Also

- [var startPoint: CGPoint](pdfannotation/startpoint.md)
  The point where a line begins, in annotation-space coordinates.
- [var startLineStyle: PDFLineStyle](pdfannotation/startlinestyle.md)
  The style of the line annotation’s starting point, such as square or filled arrowhead.
- [var endLineStyle: PDFLineStyle](pdfannotation/endlinestyle.md)
  The style of the line annotation’s ending point, such as square or filled arrowhead.
- [class func lineStyle(fromName: String) -> PDFLineStyle](pdfannotation/linestyle(fromname:).md)
  Returns a line style that corresponds to the specified name.
- [class func name(for: PDFLineStyle) -> String](pdfannotation/name(for:).md)
  Returns the name of the line style, which matches the definition in the Adobe PDF Specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/endpoint)*