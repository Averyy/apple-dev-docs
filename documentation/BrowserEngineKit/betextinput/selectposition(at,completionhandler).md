# selectPosition(at:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the selection caret to the given point.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func selectPosition(at point: CGPoint, completionHandler: @escaping @Sendable () -> Void)
```

```swift
func selectPosition(at point: CGPoint) async
```

```objc
- (void) selectPositionAtPoint:(CGPoint) point completionHandler:(void (^)()) completionHandler;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

## Parameters

- `point`: The caret’s new location in the text view.
- `completionHandler`: A closure that you call when the text view handles the gesture.

## See Also

### Managing selection
- [var selectedText: String?](./selectedtext.md)
  A string that represents the selected text.
- [var selectedTextRange: UITextRange?](./selectedtextrange.md)
  A range that represents the selected text.
- [var isSelectionAtDocumentStart: Bool](./isselectionatdocumentstart.md)
  A Boolean value that indicates if the current selection is at the beginning of the document.
- [func selectPosition(at: CGPoint, for: BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](./selectposition%28at,for,completionhandler%29.md)
  Sets the selection caret to the given point.
- [func adjustSelection(by: BEDirectionalTextRange, completionHandler: () -> Void)](./adjustselection%28by,completionhandler%29.md)
  Adjusts the selection using a range.
- [func updateCurrentSelection(to: CGPoint, from: BEGestureType, in: UIGestureRecognizer.State)](./updatecurrentselection%28to,from,in%29.md)
  Indicates the point where the text interaction gesture changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/selectposition(at:completionhandler:))*