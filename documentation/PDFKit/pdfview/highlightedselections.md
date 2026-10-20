# highlightedSelections

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the array of selections that are highlighted using `setHighlightedSelections`.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var highlightedSelections: [PDFSelection]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<PDFSelection *> * highlightedSelections;
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
- [func scrollSelectionToVisible(Any?)](./scrollselectiontovisible%28_%29.md)
  Scrolls the view until the selection is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/highlightedselections)*