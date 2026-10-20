# scrollSelectionToVisible(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the view until the selection is visible.

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
func scrollSelectionToVisible(_ sender: Any?)
```

```objc
- (void) scrollSelectionToVisible:(id) sender;
```

## See Also

### Handling Selections
- [var currentSelection: PDFSelection?](./currentselection.md)
  The current selection.
- [func setCurrentSelection(PDFSelection?, animate: Bool)](./setcurrentselection%28_,animate%29.md)
  Sets the current selection, in an animated way, if desired.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects all text in the document.
- [func clearSelection()](./clearselection%28%29.md)
  Clears the selection.
- [func copy(Any?)](./copy%28_%29.md)
  Copies the text in the selection, if any, to the Pasteboard.
- [var highlightedSelections: [PDFSelection]?](./highlightedselections.md)
  Returns the array of selections that are highlighted using `setHighlightedSelections`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/scrollselectiontovisible(_:))*