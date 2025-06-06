# document

**Framework**: PDFKit  
**Kind**: property

Returns the `PDFDocument` object with which the page is associated.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
weak var document: PDFDocument? { get }
```

## See Also

- [var label: String?](pdfpage/label.md)
  Returns the label for the page.
- [func bounds(for: PDFDisplayBox) -> CGRect](pdfpage/bounds(for:).md)
  Returns the bounds for the specified PDF display box.
- [func setBounds(CGRect, for: PDFDisplayBox)](pdfpage/setbounds(_:for:).md)
  Sets the bounds for the specified box.
- [var rotation: Int](pdfpage/rotation.md)
  Sets the rotation angle for the page in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/document)*