# textViewDidChangeSelection(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when the selection changes in the text view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func textViewDidChangeSelection(_ notification: Notification)
```

```objc
- (void) textViewDidChangeSelection:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`didChangeSelectionNotification`](../nstextview/didchangeselectionnotification.md).

## See Also

### Managing the Selection
- [func textView(NSTextView, willChangeSelectionFromCharacterRange: NSRange, toCharacterRange: NSRange) -> NSRange](./textview%28_,willchangeselectionfromcharacterrange,tocharacterrange%29.md)
  Returns the actual range to select.
- [func textView(NSTextView, willChangeSelectionFromCharacterRanges: [NSValue], toCharacterRanges: [NSValue]) -> [NSValue]](./textview%28_,willchangeselectionfromcharacterranges,tocharacterranges%29.md)
  Returns the actual character ranges to select.
- [func textView(NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](./textview%28_,candidates,forselectedrange%29.md)
  Returns an array of text objects to include in a text selection.
- [func textView(NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](./textview%28_,candidatesforselectedrange%29.md)
  Returns an array of objects that represent the elements of a selection.
- [func textView(NSTextView, shouldSelectCandidateAt: Int) -> Bool](./textview%28_,shouldselectcandidateat%29.md)
  Returns a Boolean value that indicates whether to select the text object at the index.
- [func textView(NSTextView, shouldUpdateTouchBarItemIdentifiers: [NSTouchBarItem.Identifier]) -> [NSTouchBarItem.Identifier]](./textview%28_,shouldupdatetouchbaritemidentifiers%29.md)
  Returns and array of touch bar elements for the framework to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textviewdidchangeselection(_:))*