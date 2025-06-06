# removeFromParent()

**Framework**: PDFKit  
**Kind**: method

Removes the outline object from its parent (does nothing if outline object is the root outline object).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeFromParent()
```

## See Also

- [var parent: PDFOutline?](pdfoutline/parent.md)
  Returns the parent outline object of the outline (returns `NULL` if called on the root outline object).
- [func insertChild(PDFOutline, at: Int)](pdfoutline/insertchild(_:at:).md)
  Inserts the specified outline object at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/removefromparent())*