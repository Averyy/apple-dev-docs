# currentSelection

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

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
var currentSelection: PDFSelection? { get set }
```

```objc
@property (nonatomic, strong, nullable) PDFSelection * currentSelection;
```

#### Discussion

Returns `NULL` if no selection exists.

Note that this method returns the actual instance of the current `PDFSelection` object. Therefore, if you want to modify it, you should make a copy of the returned selection and modify that, instead.

## See Also

### Handling Selections
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
- [var highlightedSelections: [PDFSelection]?](./highlightedselections.md)
  Returns the array of selections that are highlighted using `setHighlightedSelections`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/currentselection)*