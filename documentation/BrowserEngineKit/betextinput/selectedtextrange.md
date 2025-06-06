# selectedTextRange

**Framework**: BrowserEngineKit  
**Kind**: property  
**Required**: Yes

Range representing the selected text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@NSCopying
var selectedTextRange: UITextRange? { get set }
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

Text may have a selection, either zero-length (a caret) or ranged. Editing operations are always performed on the text from this selection.  nil corresponds to no selection.

The range of text in the text view’s selection.

#### Overview

If the text caret is in the view but no text is selected, return a range with `0` as its length. If there’s no selection in the view, return `nil`.

## See Also

- [var selectedText: String?](betextinput/selectedtext.md)
  String representing the selected text.
- [var isSelectionAtDocumentStart: Bool](betextinput/isselectionatdocumentstart.md)
  Represents whether the current selection is at the beginning of the document
- [func caretRect(for: UITextPosition) -> CGRect](betextinput/caretrect(for:).md)
  Returns a rectangle to draw the caret at a specified insertion point.
- [func selectionRects(for: UITextRange) -> [UITextSelectionRect]](betextinput/selectionrects(for:).md)
  Returns an array of selection rects corresponding to the range of text.
- [func selectWordForReplacement()](betextinput/selectwordforreplacement.md)
  Selects a word with autocorrect replacement suggestions when it is tapped
- [func updateSelection(extent: CGPoint, boundary: UITextGranularity, completionHandler: (Bool) -> Void)](betextinput/updateselection(extent:boundary:completionhandler:).md)
  Includes the text up to the given point in the current text selection.
- [func selectText(in: UITextGranularity, at: CGPoint, completionHandler: () -> Void)](betextinput/selecttext(in:at:completionhandler:).md)
  Selects the text within the given granularity at the given point in the text view.
- [func selectPosition(at: CGPoint, completionHandler: () -> Void)](betextinput/selectposition(at:completionhandler:).md)
  Sets the selection caret to the given point
- [func selectPosition(at: CGPoint, for: BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](betextinput/selectposition(at:for:completionhandler:).md)
  Sets the selection caret to the given point.  Also includes a convenience document context request.
- [func adjustSelection(by: BEDirectionalTextRange, completionHandler: () -> Void)](betextinput/adjustselection(by:completionhandler:).md)
  Adjusts the selection by the moving the selected range by the given `range`, in character granularity units.
- [func move(byOffset: Int)](betextinput/move(byoffset:).md)
  Adjusts the current selection by `offset` in character granularity units
- [func moveSelection(atBoundary: UITextGranularity, in: UITextStorageDirection, completionHandler: () -> Void)](betextinput/moveselection(atboundary:in:completionhandler:).md)
  Moves the caret to relative to the current position in the `direction` to the given `granularity`. The `direction` is “forward” or “backward” in accordance with the directionality of the language.
- [func selectTextForEditMenuWithLocation(inView: CGPoint, completionHandler: (Bool, String?, NSRange) -> Void)](betextinput/selecttextforeditmenuwithlocation(inview:completionhandler:).md)
  Indicates the edit menu is being shown at the given location in the text input view’s coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/selectedtextrange)*