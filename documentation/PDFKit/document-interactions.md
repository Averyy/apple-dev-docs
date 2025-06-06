# Document Interactions

**Framework**: PDFKit

Handle selections, work with annotation actions, convert page and view points, and work with mouse events in a document.

## Topics

### Handling Selections
- [var currentSelection: PDFSelection?](pdfview/currentselection.md)
  The current selection.
- [func setCurrentSelection(PDFSelection?, animate: Bool)](pdfview/setcurrentselection(_:animate:).md)
  Sets the current selection, in an animated way, if desired.
- [func selectAll(Any?)](pdfview/selectall(_:).md)
  Selects all text in the document.
- [func clearSelection()](pdfview/clearselection.md)
  Clears the selection.
- [func copy(Any?)](pdfview/copy(_:).md)
  Copies the text in the selection, if any, to the Pasteboard.
- [func scrollSelectionToVisible(Any?)](pdfview/scrollselectiontovisible(_:).md)
  Scrolls the view until the selection is visible.
- [var highlightedSelections: [PDFSelection]?](pdfview/highlightedselections.md)
  Returns the array of selections that are highlighted using `setHighlightedSelections`.
### Working with Annotation Actions
- [func annotationsChanged(on: PDFPage)](pdfview/annotationschanged(on:).md)
  Tells the PDF view that an annotation on the specified page has changed.
- [Link Annotations](link-annotations.md)
  Validate and handle links in a PDF view.
### Converting Page and View Points
- [func page(for: CGPoint, nearest: Bool) -> PDFPage?](pdfview/page(for:nearest:).md)
  Returns the page containing a point specified in view coordinates.
- [func convert(CGPoint, to: PDFPage) -> CGPoint](pdfview/convert(_:to:)-9twqk.md)
  Converts a point from view space to page space.
- [func convert(CGRect, to: PDFPage) -> CGRect](pdfview/convert(_:to:)-8cp0c.md)
  Converts a rectangle from view space to page space.
- [func convert(CGPoint, from: PDFPage) -> CGPoint](pdfview/convert(_:from:)-4evlx.md)
  Converts a point from page space to view space.
- [func convert(CGRect, from: PDFPage) -> CGRect](pdfview/convert(_:from:)-9xv1z.md)
  Converts a rectangle from page space to view space.
### Working with Mouse Position and Events
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
- [Drag Operations](drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/document-interactions)*