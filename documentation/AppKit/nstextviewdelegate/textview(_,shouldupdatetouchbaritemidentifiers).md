# textView(_:shouldUpdateTouchBarItemIdentifiers:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns and array of touch bar elements for the framework to update.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, shouldUpdateTouchBarItemIdentifiers identifiers: [NSTouchBarItem.Identifier]) -> [NSTouchBarItem.Identifier]
```

```objc
- (NSArray<NSString *> *) textView:(NSTextView *) textView shouldUpdateTouchBarItemIdentifiers:(NSArray<NSString *> *) identifiers;
```

#### Return Value

Returns an array of [`NSTouchBarItem.Identifier`](../nstouchbaritem/identifier-swift.struct.md) elements for framework to update.

## Parameters

- `textView`: The text view that sent the message.
- `identifiers`: An array of touch bar identifiers to evaluate.

## See Also

### Managing the Selection
- [func textView(NSTextView, willChangeSelectionFromCharacterRange: NSRange, toCharacterRange: NSRange) -> NSRange](./textview%28_,willchangeselectionfromcharacterrange,tocharacterrange%29.md)
  Returns the actual range to select.
- [func textView(NSTextView, willChangeSelectionFromCharacterRanges: [NSValue], toCharacterRanges: [NSValue]) -> [NSValue]](./textview%28_,willchangeselectionfromcharacterranges,tocharacterranges%29.md)
  Returns the actual character ranges to select.
- [func textViewDidChangeSelection(Notification)](./textviewdidchangeselection%28_%29.md)
  Sent when the selection changes in the text view.
- [func textView(NSTextView, candidates: [NSTextCheckingResult], forSelectedRange: NSRange) -> [NSTextCheckingResult]](./textview%28_,candidates,forselectedrange%29.md)
  Returns an array of text objects to include in a text selection.
- [func textView(NSTextView, candidatesForSelectedRange: NSRange) -> [Any]?](./textview%28_,candidatesforselectedrange%29.md)
  Returns an array of objects that represent the elements of a selection.
- [func textView(NSTextView, shouldSelectCandidateAt: Int) -> Bool](./textview%28_,shouldselectcandidateat%29.md)
  Returns a Boolean value that indicates whether to select the text object at the index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:shouldupdatetouchbaritemidentifiers:))*