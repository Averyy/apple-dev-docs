# areaOfInterest(for:)

**Framework**: PDFKit  
**Kind**: method

Returns the type of area for a specific cursor location point.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func areaOfInterest(for cursorLocation: CGPoint) -> PDFAreaOfInterest
```

## See Also

- [func areaOfInterest(forMouse: UIEvent) -> PDFAreaOfInterest](pdfview/areaofinterest(formouse:).md)
  Returns the type of area the mouse cursor is over.
- [struct PDFAreaOfInterest](pdfareaofinterest.md)
  The mouse position over PDF view areas.
- [func setCursorFor(PDFAreaOfInterest)](pdfview/setcursorfor(_:).md)
  Sets the type of mouse cursor according to the type of area the mouse cursor is over.
- [func perform(PDFAction)](pdfview/perform(_:).md)
  Performs the specified action.
- [Drag Operations](drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/areaofinterest(for:))*