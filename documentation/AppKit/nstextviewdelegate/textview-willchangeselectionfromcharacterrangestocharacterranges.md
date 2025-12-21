# textView(_:willChangeSelectionFromCharacterRanges:toCharacterRanges:)

**Framework**: AppKit  
**Kind**: method

Returns the actual character ranges to select.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, willChangeSelectionFromCharacterRanges oldSelectedCharRanges: [NSValue], toCharacterRanges newSelectedCharRanges: [NSValue]) -> [NSValue]
```

#### Return Value

An array containing the actual character ranges for the new selection.

#### Discussion

Invoked before an `NSTextView` object finishes changing the selection—that is, when the last argument to a [`setSelectedRange(_:affinity:stillSelecting:)`](nstextview/setselectedrange(_:affinity:stillselecting:).md) or [`setSelectedRanges(_:affinity:stillSelecting:)`](nstextview/setselectedranges(_:affinity:stillselecting:).md) message is [`false`](https://developer.apple.com/documentation/Swift/false).

Non-selectable text views do not process any mouse events. If for some reason it is necessary to disallow user selection change in a text view that handles mouse events, this can be achieved by making the text view selectable but implementing this delegate method to disallow selection changes.

If a delegate implements both this method and [`textView(_:willChangeSelectionFromCharacterRange:toCharacterRange:)`](nstextviewdelegate/textview(_:willchangeselectionfromcharacterrange:tocharacterrange:).md), then the latter is ignored.

## Parameters

- `textView`: The text view sending the message. This is the first text view in a series shared by a layout manager, not necessarily the text view displaying the selected text.
- `oldSelectedCharRanges`: An array containing the original ranges of the selection. This must be a non- , non-empty array of objects responding to the   method  , and in addition its elements must be sorted, non-overlapping, non-contiguous, and (except for the case of a single range) have non-zero-length.
- `newSelectedCharRanges`: An array containing the proposed character ranges for the new selection. This must be a non- , non-empty array of objects responding to the   method  , and in addition its elements must be sorted, non-overlapping, non-contiguous, and (except for the case of a single range) have non-zero-length.

## See Also

- [func textView(NSTextView, willChangeSelectionFromCharacterRange: NSRange, toCharacterRange: NSRange) -> NSRange](nstextviewdelegate/textview(_:willchangeselectionfromcharacterrange:tocharacterrange:).md)
  Returns the actual range to select.
- [func textViewDidChangeSelection(Notification)](nstextviewdelegate/textviewdidchangeselection(_:).md)
  Sent when the selection changes in the text view.
- [func textView(NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](nstextviewdelegate/textview(_:candidates:forselectedrange:).md)
  Returns an array of text objects to include in a text selection.
- [func textView(NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](nstextviewdelegate/textview(_:candidatesforselectedrange:).md)
  Returns an array of objects that represent the elements of a selection.
- [func textView(NSTextView, shouldSelectCandidateAt: Int) -> Bool](nstextviewdelegate/textview(_:shouldselectcandidateat:).md)
  Returns a Boolean value that indicates whether to select the text object at the index.
- [func textView(NSTextView, shouldUpdateTouchBarItemIdentifiers: [NSTouchBarItem.Identifier]) -> [NSTouchBarItem.Identifier]](nstextviewdelegate/textview(_:shouldupdatetouchbaritemidentifiers:).md)
  Returns and array of touch bar elements for the framework to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:willchangeselectionfromcharacterranges:tocharacterranges:))*