# isSelectionAtDocumentStart

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates if the current selection is at the beginning of the document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var isSelectionAtDocumentStart: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSelectionAtDocumentStart) BOOL selectionAtDocumentStart;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

## See Also

### Managing selection
- [var selectedText: String?](./selectedtext.md)
  A string that represents the selected text.
- [var selectedTextRange: UITextRange?](./selectedtextrange.md)
  A range that represents the selected text.
- [func selectPosition(at: CGPoint, completionHandler: () -> Void)](./selectposition%28at,completionhandler%29.md)
  Sets the selection caret to the given point.
- [func selectPosition(at: CGPoint, for: BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](./selectposition%28at,for,completionhandler%29.md)
  Sets the selection caret to the given point.
- [func adjustSelection(by: BEDirectionalTextRange, completionHandler: () -> Void)](./adjustselection%28by,completionhandler%29.md)
  Adjusts the selection using a range.
- [func updateCurrentSelection(to: CGPoint, from: BEGestureType, in: UIGestureRecognizer.State)](./updatecurrentselection%28to,from,in%29.md)
  Indicates the point where the text interaction gesture changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/isselectionatdocumentstart)*