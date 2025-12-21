# setCurrentSelection(_:animate:)

**Framework**: PDFKit  
**Kind**: method

Sets the current selection, in an animated way, if desired.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setCurrentSelection(_ selection: PDFSelection?, animate: Bool)
```

#### Discussion

This method behaves as `setCurrentSelection(_:)`, but with the addition of animation, if `animate` is [`true`](https://developer.apple.com/documentation/Swift/true). The animation serves to draw the user’s attention to the new selection, which can be useful when implementing search.

## See Also

- [var currentSelection: PDFSelection?](pdfview/currentselection.md)
  The current selection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/setcurrentselection(_:animate:))*