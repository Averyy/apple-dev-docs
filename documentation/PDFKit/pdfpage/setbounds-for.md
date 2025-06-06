# setBounds(_:for:)

**Framework**: PDFKit  
**Kind**: method

Sets the bounds for the specified box.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setBounds(_ bounds: NSRect, for box: PDFDisplayBox)
```

#### Discussion

If the box does not exist, this method creates it for you.

To remove a box, pass `NSZeroRect` for the bounds (note that you cannot remove the media box). If the box bounds are not in range, this method throws a range exception.

## See Also

- [var document: PDFDocument?](pdfpage/document.md)
  Returns the `PDFDocument` object with which the page is associated.
- [var label: String?](pdfpage/label.md)
  Returns the label for the page.
- [func bounds(for: PDFDisplayBox) -> CGRect](pdfpage/bounds(for:).md)
  Returns the bounds for the specified PDF display box.
- [var rotation: Int](pdfpage/rotation.md)
  Sets the rotation angle for the page in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/setbounds(_:for:))*