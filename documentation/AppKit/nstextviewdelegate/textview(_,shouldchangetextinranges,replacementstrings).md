# textView(_:shouldChangeTextInRanges:replacementStrings:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when a text view needs to determine if text in an array of specified ranges should be changed.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, shouldChangeTextInRanges affectedRanges: [NSValue], replacementStrings: [String]?) -> Bool
```

```objc
- (BOOL) textView:(NSTextView *) textView shouldChangeTextInRanges:(NSArray<NSValue *> *) affectedRanges replacementStrings:(NSArray<NSString *> *) replacementStrings;
```

## Return Value

[`true`](../../Swift/true.md) to allow the replacement, or [`false`](../../Swift/false.md) to reject the change.

## Parameters

- `textView`: The text view sending the message. This is the first text view in a series shared by a layout manager, not necessarily the text view displaying the selected text.
- `affectedRanges`: The array of ranges of characters to be replaced. This array must be a non-nil, non-empty array of objects responding to the NSValue `rangeValue` method, and in addition its elements must be sorted, non-overlapping, non-contiguous, and (except for the case of a single range) have non-zero-length.
- `replacementStrings`: The array of strings that will replace the characters in `affectedRanges`, one string for each range; `nil` if only text attributes are being changed.

## See Also

### Setting Text Attributes
- [func textView(NSTextView, shouldChangeTextIn: NSRange, replacementString: String?) -> Bool](./textview%28_,shouldchangetextin,replacementstring%29.md)
  Sent when a text view needs to determine if text in a specified range should be changed.
- [func textView(NSTextView, shouldChangeTypingAttributes: [String : Any], toAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]](./textview%28_,shouldchangetypingattributes,toattributes%29.md)
  Sent when the typing attributes are changed.
- [func textViewDidChangeTypingAttributes(Notification)](./textviewdidchangetypingattributes%28_%29.md)
  Sent when a text view’s typing attributes change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:shouldchangetextinranges:replacementstrings:))*