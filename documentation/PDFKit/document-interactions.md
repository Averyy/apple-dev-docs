# Document Interactions

**Framework**: PDFKit  
**Role**: API Collection

Handle selections, work with annotation actions, convert page and view points, and work with mouse events in a document.

## Topics

### Handling Selections
- [var currentSelection: PDFSelection?](./pdfview/currentselection.md)
  The current selection.
- [func setCurrentSelection(PDFSelection?, animate: Bool)](./pdfview/setcurrentselection%28_,animate%29.md)
  Sets the current selection, in an animated way, if desired.
- [func selectAll(Any?)](./pdfview/selectall%28_%29.md)
  Selects all text in the document.
- [func clearSelection()](./pdfview/clearselection%28%29.md)
  Clears the selection.
- [func copy(Any?)](./pdfview/copy%28_%29.md)
  Copies the text in the selection, if any, to the Pasteboard.
- [func scrollSelectionToVisible(Any?)](./pdfview/scrollselectiontovisible%28_%29.md)
  Scrolls the view until the selection is visible.
- [var highlightedSelections: [PDFSelection]?](./pdfview/highlightedselections.md)
  Returns the array of selections that are highlighted using `setHighlightedSelections`.
### Working with Annotation Actions
- [func annotationsChanged(on: PDFPage)](./pdfview/annotationschanged%28on%29.md)
  Tells the PDF view that an annotation on the specified page has changed.
- [Link Annotations](./link-annotations.md)
  Validate and handle links in a PDF view.
### Converting Page and View Points
- [func page(for: CGPoint, nearest: Bool) -> PDFPage?](./pdfview/page%28for,nearest%29.md)
  Returns the page containing a point specified in view coordinates.
- [func convert(CGPoint, to: PDFPage) -> CGPoint](./pdfview/convert%28_,to%29-9twqk.md)
  Converts a point from view space to page space.
- [func convert(CGRect, to: PDFPage) -> CGRect](./pdfview/convert%28_,to%29-8cp0c.md)
  Converts a rectangle from view space to page space.
- [func convert(CGPoint, from: PDFPage) -> CGPoint](./pdfview/convert%28_,from%29-4evlx.md)
  Converts a point from page space to view space.
- [func convert(CGRect, from: PDFPage) -> CGRect](./pdfview/convert%28_,from%29-9xv1z.md)
  Converts a rectangle from page space to view space.
### Working with Mouse Position and Events
- [func areaOfInterest(forMouse: UIEvent) -> PDFAreaOfInterest](./pdfview/areaofinterest%28formouse%29.md)
  Returns the type of area the mouse cursor is over.
- [func areaOfInterest(for: CGPoint) -> PDFAreaOfInterest](./pdfview/areaofinterest%28for%29.md)
  Returns the type of area for a specific cursor location point.
- [struct PDFAreaOfInterest](./pdfareaofinterest.md)
  The mouse position over PDF view areas.
- [func setCursorFor(PDFAreaOfInterest)](./pdfview/setcursorfor%28_%29.md)
  Sets the type of mouse cursor according to the type of area the mouse cursor is over.
- [func perform(PDFAction)](./pdfview/perform%28_%29.md)
  Performs the specified action.
- [Drag Operations](./drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/document-interactions)*