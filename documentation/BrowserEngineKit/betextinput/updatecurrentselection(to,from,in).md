# updateCurrentSelection(to:from:in:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates the point where the text interaction gesture changes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func updateCurrentSelection(to point: CGPoint, from gestureType: BEGestureType, in state: UIGestureRecognizer.State)
```

```objc
- (void) updateCurrentSelectionTo:(CGPoint) point fromGesture:(BEGestureType) gestureType inState:(UIGestureRecognizerState) state;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

In your implementation of this method, notify the system that your app handles the change by calling [`selectionChangedWithGesture(at:gesture:state:flags:)`](../betextinteraction/selectionchangedwithgesture%28at,gesture,state,flags%29.md).

## Parameters

- `point`: The new location of the gesture.
- `gestureType`: The type of gesture the system tracks.
- `state`: The state of the gesture.

## See Also

### Managing selection
- [var selectedText: String?](./selectedtext.md)
  A string that represents the selected text.
- [var selectedTextRange: UITextRange?](./selectedtextrange.md)
  A range that represents the selected text.
- [var isSelectionAtDocumentStart: Bool](./isselectionatdocumentstart.md)
  A Boolean value that indicates if the current selection is at the beginning of the document.
- [func selectPosition(at: CGPoint, completionHandler: () -> Void)](./selectposition%28at,completionhandler%29.md)
  Sets the selection caret to the given point.
- [func selectPosition(at: CGPoint, for: BETextDocumentRequest, completionHandler: (BETextDocumentContext) -> Void)](./selectposition%28at,for,completionhandler%29.md)
  Sets the selection caret to the given point.
- [func adjustSelection(by: BEDirectionalTextRange, completionHandler: () -> Void)](./adjustselection%28by,completionhandler%29.md)
  Adjusts the selection using a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/updatecurrentselection(to:from:in:))*