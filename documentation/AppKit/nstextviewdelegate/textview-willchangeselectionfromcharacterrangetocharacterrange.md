# textView(_:willChangeSelectionFromCharacterRange:toCharacterRange:)

**Framework**: AppKit  
**Kind**: method

Returns the actual range to select.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, willChangeSelectionFromCharacterRange oldSelectedCharRange: NSRange, toCharacterRange newSelectedCharRange: NSRange) -> NSRange
```

#### Return Value

The actual character range for the new selection.

#### Discussion

This method is invoked before a text view finishes changing the selection—that is, when the last argument to a [`setSelectedRange(_:affinity:stillSelecting:)`](nstextview/setselectedrange(_:affinity:stillselecting:).md) message is [`false`](https://developer.apple.com/documentation/swift/false).

Non-selectable text views do not process any mouse events. If for some reason it is necessary to disallow user selection change in a text view that handles mouse events, this can be achieved by making the text view selectable but implementing this delegate method to disallow selection changes.

##### Special Considerations

In macOS 10.4 and later, if a delegate implements this delegate method and not its multiple-selection replacement, [`textView(_:willChangeSelectionFromCharacterRanges:toCharacterRanges:)`](nstextviewdelegate/textview(_:willchangeselectionfromcharacterranges:tocharacterranges:).md), then multiple selection is effectively disallowed; attempts to set the selected ranges call the old delegate method with the first subrange, and afterwards only a single selected range is set.

## Parameters

- `textView`: The text view sending the message. This is the first text view in a series shared by a layout manager, not necessarily the text view displaying the selected text.
- `oldSelectedCharRange`: The original range of the selection.
- `newSelectedCharRange`: The proposed character range for the new selection.

## See Also

- [func textView(NSTextView, willChangeSelectionFromCharacterRanges: [NSValue], toCharacterRanges: [NSValue]) -> [NSValue]](nstextviewdelegate/textview(_:willchangeselectionfromcharacterranges:tocharacterranges:).md)
  Returns the actual character ranges to select.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:willchangeselectionfromcharacterrange:tocharacterrange:))*