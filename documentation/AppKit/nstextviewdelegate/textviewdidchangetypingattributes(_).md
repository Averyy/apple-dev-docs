# textViewDidChangeTypingAttributes(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when a text view’s typing attributes change.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func textViewDidChangeTypingAttributes(_ notification: Notification)
```

```objc
- (void) textViewDidChangeTypingAttributes:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`didChangeTypingAttributesNotification`](../nstextview/didchangetypingattributesnotification.md).

## See Also

### Setting Text Attributes
- [func textView(NSTextView, shouldChangeTextIn: NSRange, replacementString: String?) -> Bool](./textview%28_,shouldchangetextin,replacementstring%29.md)
  Sent when a text view needs to determine if text in a specified range should be changed.
- [func textView(NSTextView, shouldChangeTextInRanges: [NSValue], replacementStrings: [String]?) -> Bool](./textview%28_,shouldchangetextinranges,replacementstrings%29.md)
  Sent when a text view needs to determine if text in an array of specified ranges should be changed.
- [func textView(NSTextView, shouldChangeTypingAttributes: [String : Any], toAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]](./textview%28_,shouldchangetypingattributes,toattributes%29.md)
  Sent when the typing attributes are changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textviewdidchangetypingattributes(_:))*