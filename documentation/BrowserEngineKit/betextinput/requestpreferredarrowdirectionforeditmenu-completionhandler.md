# requestPreferredArrowDirectionForEditMenu(completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Invoked by the system to gather context, including the client’s preference for how the edit menu should be positioned relative to the selected text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func requestPreferredArrowDirectionForEditMenu() async -> UIEditMenuArrowDirection
```

## See Also

- [func transposeCharactersAroundSelection()](betextinput/transposecharactersaroundselection.md)
  Transposes the characters on either side of the caret in response to the key command, ctrl + T
- [func replaceText(String, withText: String, options: BETextReplacementOptions, completionHandler: ([UITextSelectionRect]) -> Void)](betextinput/replacetext(_:withtext:options:completionhandler:).md)
  Replace the specified text preceding the current selection.
- [func requestTextContextForAutocorrection(completionHandler: (BETextDocumentContext) -> Void)](betextinput/requesttextcontextforautocorrection(completionhandler:).md)
  Invoked by the system to gather context around the current selection.  Clients should generally include the setence that contains the current selection and include the previous sentence if the current selection is at a boundary.
- [func requestTextRects(for: String, withCompletionHandler: ([UITextSelectionRect]) -> Void)](betextinput/requesttextrects(for:withcompletionhandler:).md)
  Invoked by the system to gather context for the presentation of various text related UI’s. Completion handler should be invoked with the `UITextSelectionRect`s for the substring nearest to the caret that matches the given `input`
- [var automaticallyPresentEditMenu: Bool](betextinput/automaticallypresenteditmenu.md)
  Controls whether the edit menu is allowed to be presented or should be suppressed.
- [func systemWillPresentEditMenu(withAnimator: any UIEditMenuInteractionAnimating)](betextinput/systemwillpresenteditmenu(withanimator:).md)
  Invoked by the system when it is about to present an edit menu with an animator.
- [func systemWillDismissEditMenu(withAnimator: any UIEditMenuInteractionAnimating)](betextinput/systemwilldismisseditmenu(withanimator:).md)
  Invoked by the system when it is about to dismiss an edit menu with an animator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/requestpreferredarrowdirectionforeditmenu(completionhandler:))*