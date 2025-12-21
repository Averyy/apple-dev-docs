# textView(_:shouldChangeTextInRanges:replacementStrings:)

**Framework**: AppKit  
**Kind**: method

Sent when a text view needs to determine if text in an array of specified ranges should be changed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, shouldChangeTextInRanges affectedRanges: [NSValue], replacementStrings: [String]?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow the replacement, or [`false`](https://developer.apple.com/documentation/Swift/false) to reject the change.

## Parameters

- `textView`: The text view sending the message. This is the first text view in a series shared by a layout manager, not necessarily the text view displaying the selected text.
- `affectedRanges`: The array of ranges of characters to be replaced. This array must be a non-nil, non-empty array of objects responding to the NSValue   method, and in addition its elements must be sorted, non-overlapping, non-contiguous, and (except for the case of a single range) have non-zero-length.
- `replacementStrings`: The array of strings that will replace the characters in  , one string for each range;   if only text attributes are being changed.

## See Also

- [func textView(NSTextView, shouldChangeTextIn: NSRange, replacementString: String?) -> Bool](nstextviewdelegate/textview(_:shouldchangetextin:replacementstring:).md)
  Sent when a text view needs to determine if text in a specified range should be changed.
- [func textView(NSTextView, shouldChangeTypingAttributes: [String : Any], toAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]](nstextviewdelegate/textview(_:shouldchangetypingattributes:toattributes:).md)
  Sent when the typing attributes are changed.
- [func textViewDidChangeTypingAttributes(Notification)](nstextviewdelegate/textviewdidchangetypingattributes(_:).md)
  Sent when a text view’s typing attributes change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:shouldchangetextinranges:replacementstrings:))*