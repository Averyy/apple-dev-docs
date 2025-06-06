# currentSelection

**Framework**: PDFKit  
**Kind**: property

The current selection.

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
var currentSelection: PDFSelection? { get set }
```

#### Discussion

Returns `NULL` if no selection exists.

Note that this method returns the actual instance of the current `PDFSelection` object. Therefore, if you want to modify it, you should make a copy of the returned selection and modify that, instead.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/currentselection)*