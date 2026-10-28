# setCurrentSelection(_:animate:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

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
func setCurrentSelection(_ selection: PDFSelection?, animate: Bool)
```

```objc
- (void) setCurrentSelection:(PDFSelection *) selection animate:(BOOL) animate;
```

## Discussion

This method behaves as `setCurrentSelection(_:)`, but with the addition of animation, if `animate` is [`true`](../../Swift/true.md). The animation serves to draw the user’s attention to the new selection, which can be useful when implementing search.

## See Also

### Handling Selections
- [var currentSelection: PDFSelection?](./currentselection.md)
  The current selection.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects all text in the document.
- [func clearSelection()](./clearselection%28%29.md)
  Clears the selection.
- [func copy(Any?)](./copy%28_%29.md)
  Copies the text in the selection, if any, to the Pasteboard.
- [func scrollSelectionToVisible(Any?)](./scrollselectiontovisible%28_%29.md)
  Scrolls the view until the selection is visible.
- [var highlightedSelections: [PDFSelection]?](./highlightedselections.md)
  Returns the array of selections that are highlighted using `setHighlightedSelections`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/setcurrentselection(_:animate:))*