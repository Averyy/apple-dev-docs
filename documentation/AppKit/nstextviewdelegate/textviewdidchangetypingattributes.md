# textViewDidChangeTypingAttributes(_:)

**Framework**: AppKit  
**Kind**: method

Sent when a text view’s typing attributes change.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func textViewDidChangeTypingAttributes(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  .

## See Also

- [func textView(NSTextView, shouldChangeTextIn: NSRange, replacementString: String?) -> Bool](nstextviewdelegate/textview(_:shouldchangetextin:replacementstring:).md)
  Sent when a text view needs to determine if text in a specified range should be changed.
- [func textView(NSTextView, shouldChangeTextInRanges: [NSValue], replacementStrings: [String]?) -> Bool](nstextviewdelegate/textview(_:shouldchangetextinranges:replacementstrings:).md)
  Sent when a text view needs to determine if text in an array of specified ranges should be changed.
- [func textView(NSTextView, shouldChangeTypingAttributes: [String : Any], toAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]](nstextviewdelegate/textview(_:shouldchangetypingattributes:toattributes:).md)
  Sent when the typing attributes are changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textviewdidchangetypingattributes(_:))*