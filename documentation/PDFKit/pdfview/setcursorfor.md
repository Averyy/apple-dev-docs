# setCursorFor(_:)

**Framework**: PDFKit  
**Kind**: method

Sets the type of mouse cursor according to the type of area the mouse cursor is over.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setCursorFor(_ area: PDFAreaOfInterest)
```

#### Discussion

This method is especially useful for custom subclasses of the `PDFView` class.

## See Also

- [func areaOfInterest(forMouse: UIEvent) -> PDFAreaOfInterest](pdfview/areaofinterest(formouse:).md)
  Returns the type of area the mouse cursor is over.
- [func areaOfInterest(for: CGPoint) -> PDFAreaOfInterest](pdfview/areaofinterest(for:).md)
  Returns the type of area for a specific cursor location point.
- [struct PDFAreaOfInterest](pdfareaofinterest.md)
  The mouse position over PDF view areas.
- [func perform(PDFAction)](pdfview/perform(_:).md)
  Performs the specified action.
- [Drag Operations](drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/setcursorfor(_:))*