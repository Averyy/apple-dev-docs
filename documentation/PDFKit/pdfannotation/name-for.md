# name(for:)

**Framework**: PDFKit  
**Kind**: method

Returns the name of the line style, which matches the definition in the Adobe PDF Specification.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class func name(for style: PDFLineStyle) -> String
```

## Parameters

- `style`: A line style to get a name for.

## See Also

- [var startPoint: CGPoint](pdfannotation/startpoint.md)
  The point where a line begins, in annotation-space coordinates.
- [var endPoint: CGPoint](pdfannotation/endpoint.md)
  The point where a line ends, in annotation-space coordinates.
- [var startLineStyle: PDFLineStyle](pdfannotation/startlinestyle.md)
  The style of the line annotation’s starting point, such as square or filled arrowhead.
- [var endLineStyle: PDFLineStyle](pdfannotation/endlinestyle.md)
  The style of the line annotation’s ending point, such as square or filled arrowhead.
- [class func lineStyle(fromName: String) -> PDFLineStyle](pdfannotation/linestyle(fromname:).md)
  Returns a line style that corresponds to the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/name(for:))*