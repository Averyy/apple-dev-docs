# Drag Operations

**Framework**: PDFKit

Define drag operations allowed for a view.

## Topics

### Dragging in a View
- [var allowsDragging: Bool](pdfview/allowsdragging.md)
  A Boolean value indicating whether the view can accept new PDF documents dragged into it by the user.
- [var acceptsDraggedFiles: Bool](pdfview/acceptsdraggedfiles.md)
  A Boolean value indicating whether you can drag a file into the view.

## See Also

- [func areaOfInterest(forMouse: UIEvent) -> PDFAreaOfInterest](pdfview/areaofinterest(formouse:).md)
  Returns the type of area the mouse cursor is over.
- [func areaOfInterest(for: CGPoint) -> PDFAreaOfInterest](pdfview/areaofinterest(for:).md)
  Returns the type of area for a specific cursor location point.
- [struct PDFAreaOfInterest](pdfareaofinterest.md)
  The mouse position over PDF view areas.
- [func setCursorFor(PDFAreaOfInterest)](pdfview/setcursorfor(_:).md)
  Sets the type of mouse cursor according to the type of area the mouse cursor is over.
- [func perform(PDFAction)](pdfview/perform(_:).md)
  Performs the specified action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/drag-operations)*