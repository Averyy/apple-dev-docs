# copy(_:)

**Framework**: PDFKit  
**Kind**: method

Copies the text in the selection, if any, to the Pasteboard.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@IBAction
@MainActor func copy(_ sender: Any?)
```

## See Also

- [var currentSelection: PDFSelection?](pdfview/currentselection.md)
  The current selection.
- [func setCurrentSelection(PDFSelection?, animate: Bool)](pdfview/setcurrentselection(_:animate:).md)
  Sets the current selection, in an animated way, if desired.
- [func selectAll(Any?)](pdfview/selectall(_:).md)
  Selects all text in the document.
- [func clearSelection()](pdfview/clearselection.md)
  Clears the selection.
- [func scrollSelectionToVisible(Any?)](pdfview/scrollselectiontovisible(_:).md)
  Scrolls the view until the selection is visible.
- [var highlightedSelections: [PDFSelection]?](pdfview/highlightedselections.md)
  Returns the array of selections that are highlighted using `setHighlightedSelections`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/copy(_:))*