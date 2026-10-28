# textView(_:shouldChangeTextIn:replacementString:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when a text view needs to determine if text in a specified range should be changed.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, shouldChangeTextIn affectedCharRange: NSRange, replacementString: String?) -> Bool
```

```objc
- (BOOL) textView:(NSTextView *) textView shouldChangeTextInRange:(NSRange) affectedCharRange replacementString:(NSString *) replacementString;
```

## Return Value

[`true`](../../Swift/true.md) to allow the replacement, or [`false`](../../Swift/false.md) to reject the change.

## Discussion

If a delegate implements this method and not its multiple-selection replacement, [`textView(_:shouldChangeTextInRanges:replacementStrings:)`](./textview%28_,shouldchangetextinranges,replacementstrings%29.md), it is called with an appropriate range and string. If a delegate implements the new method, then this one is ignored.

## Parameters

- `textView`: The text view sending the message. This is the first text view in a series shared by a layout manager, not necessarily the text view displaying the selected text.
- `affectedCharRange`: The range of characters to be replaced.
- `replacementString`: The characters that will replace the characters in `affectedCharRange`; `nil` if only text attributes are being changed.

## See Also

### Setting Text Attributes
- [func textView(NSTextView, shouldChangeTextInRanges: [NSValue], replacementStrings: [String]?) -> Bool](./textview%28_,shouldchangetextinranges,replacementstrings%29.md)
  Sent when a text view needs to determine if text in an array of specified ranges should be changed.
- [func textView(NSTextView, shouldChangeTypingAttributes: [String : Any], toAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]](./textview%28_,shouldchangetypingattributes,toattributes%29.md)
  Sent when the typing attributes are changed.
- [func textViewDidChangeTypingAttributes(Notification)](./textviewdidchangetypingattributes%28_%29.md)
  Sent when a text view’s typing attributes change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:shouldchangetextin:replacementstring:))*