# textView(_:willChangeSelectionFromCharacterRanges:toCharacterRanges:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the actual character ranges to select.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, willChangeSelectionFromCharacterRanges oldSelectedCharRanges: [NSValue], toCharacterRanges newSelectedCharRanges: [NSValue]) -> [NSValue]
```

```objc
- (NSArray<NSValue *> *) textView:(NSTextView *) textView willChangeSelectionFromCharacterRanges:(NSArray<NSValue *> *) oldSelectedCharRanges toCharacterRanges:(NSArray<NSValue *> *) newSelectedCharRanges;
```

#### Return Value

An array containing the actual character ranges for the new selection.

#### Discussion

Invoked before an `NSTextView` object finishes changing the selection—that is, when the last argument to a [`setSelectedRange(_:affinity:stillSelecting:)`](../nstextview/setselectedrange%28_,affinity,stillselecting%29.md) or [`setSelectedRanges(_:affinity:stillSelecting:)`](../nstextview/setselectedranges%28_,affinity,stillselecting%29.md) message is [`false`](../../Swift/false.md).

Non-selectable text views do not process any mouse events. If for some reason it is necessary to disallow user selection change in a text view that handles mouse events, this can be achieved by making the text view selectable but implementing this delegate method to disallow selection changes.

If a delegate implements both this method and [`textView(_:willChangeSelectionFromCharacterRange:toCharacterRange:)`](./textview%28_,willchangeselectionfromcharacterrange,tocharacterrange%29.md), then the latter is ignored.

## Parameters

- `textView`: The text view sending the message. This is the first text view in a series shared by a layout manager, not necessarily the text view displaying the selected text.
- `oldSelectedCharRanges`: An array containing the original ranges of the selection. This must be a non-`nil`, non-empty array of objects responding to the `NSValue` method `rangeValue`, and in addition its elements must be sorted, non-overlapping, non-contiguous, and (except for the case of a single range) have non-zero-length.
- `newSelectedCharRanges`: An array containing the proposed character ranges for the new selection. This must be a non-`nil`, non-empty array of objects responding to the `NSValue` method `rangeValue`, and in addition its elements must be sorted, non-overlapping, non-contiguous, and (except for the case of a single range) have non-zero-length.

## See Also

### Managing the Selection
- [func textView(NSTextView, willChangeSelectionFromCharacterRange: NSRange, toCharacterRange: NSRange) -> NSRange](./textview%28_,willchangeselectionfromcharacterrange,tocharacterrange%29.md)
  Returns the actual range to select.
- [func textViewDidChangeSelection(Notification)](./textviewdidchangeselection%28_%29.md)
  Sent when the selection changes in the text view.
- [func textView(NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](./textview%28_,candidates,forselectedrange%29.md)
  Returns an array of text objects to include in a text selection.
- [func textView(NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](./textview%28_,candidatesforselectedrange%29.md)
  Returns an array of objects that represent the elements of a selection.
- [func textView(NSTextView, shouldSelectCandidateAt: Int) -> Bool](./textview%28_,shouldselectcandidateat%29.md)
  Returns a Boolean value that indicates whether to select the text object at the index.
- [func textView(NSTextView, shouldUpdateTouchBarItemIdentifiers: [NSTouchBarItem.Identifier]) -> [NSTouchBarItem.Identifier]](./textview%28_,shouldupdatetouchbaritemidentifiers%29.md)
  Returns and array of touch bar elements for the framework to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:willchangeselectionfromcharacterranges:tocharacterranges:))*