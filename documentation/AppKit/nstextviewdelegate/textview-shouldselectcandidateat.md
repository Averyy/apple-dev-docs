# textView(_:shouldSelectCandidateAt:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether to select the text object at the index.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, shouldSelectCandidateAt index: Int) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the framework selects the text.

## Parameters

- `textView`: The text view that sent the message.
- `index`: The index that represents the start of the candidate text to evaluate.

## See Also

- [func textView(NSTextView, willChangeSelectionFromCharacterRange: NSRange, toCharacterRange: NSRange) -> NSRange](nstextviewdelegate/textview(_:willchangeselectionfromcharacterrange:tocharacterrange:).md)
  Returns the actual range to select.
- [func textView(NSTextView, willChangeSelectionFromCharacterRanges: [NSValue], toCharacterRanges: [NSValue]) -> [NSValue]](nstextviewdelegate/textview(_:willchangeselectionfromcharacterranges:tocharacterranges:).md)
  Returns the actual character ranges to select.
- [func textViewDidChangeSelection(Notification)](nstextviewdelegate/textviewdidchangeselection(_:).md)
  Sent when the selection changes in the text view.
- [func textView(NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](nstextviewdelegate/textview(_:candidates:forselectedrange:).md)
  Returns an array of text objects to include in a text selection.
- [func textView(NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](nstextviewdelegate/textview(_:candidatesforselectedrange:).md)
  Returns an array of objects that represent the elements of a selection.
- [func textView(NSTextView, shouldUpdateTouchBarItemIdentifiers: [NSTouchBarItem.Identifier]) -> [NSTouchBarItem.Identifier]](nstextviewdelegate/textview(_:shouldupdatetouchbaritemidentifiers:).md)
  Returns and array of touch bar elements for the framework to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:shouldselectcandidateat:))*