# clearSelection()

**Framework**: PDFKit  
**Kind**: method

Clears the selection.

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
func clearSelection()
```

#### Discussion

The view redraws as necessary but does not scroll. This call is equivalent to calling `[PDFView setCurrentSelection:NULL].`

## See Also

- [var currentSelection: PDFSelection?](pdfview/currentselection.md)
  The current selection.
- [func setCurrentSelection(PDFSelection?, animate: Bool)](pdfview/setcurrentselection(_:animate:).md)
  Sets the current selection, in an animated way, if desired.
- [func selectAll(Any?)](pdfview/selectall(_:).md)
  Selects all text in the document.
- [func copy(Any?)](pdfview/copy(_:).md)
  Copies the text in the selection, if any, to the Pasteboard.
- [func scrollSelectionToVisible(Any?)](pdfview/scrollselectiontovisible(_:).md)
  Scrolls the view until the selection is visible.
- [var highlightedSelections: [PDFSelection]?](pdfview/highlightedselections.md)
  Returns the array of selections that are highlighted using `setHighlightedSelections`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/clearselection())*