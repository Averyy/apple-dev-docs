# textView(_:shouldChangeTypingAttributes:toAttributes:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when the typing attributes are changed.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, shouldChangeTypingAttributes oldTypingAttributes: [String : Any] = [:], toAttributes newTypingAttributes: [NSAttributedString.Key : Any] = [:]) -> [NSAttributedString.Key : Any]
```

```objc
- (NSDictionary<NSString *,id> *) textView:(NSTextView *) textView shouldChangeTypingAttributes:(NSDictionary<NSString *,id> *) oldTypingAttributes toAttributes:(NSDictionary<NSString *,id> *) newTypingAttributes;
```

#### Return Value

The actual new typing attributes.

## Parameters

- `textView`: The text view sending the message.
- `oldTypingAttributes`: The old typing attributes.
- `newTypingAttributes`: The proposed typing attributes.

## See Also

### Setting Text Attributes
- [func textView(NSTextView, shouldChangeTextIn: NSRange, replacementString: String?) -> Bool](./textview%28_,shouldchangetextin,replacementstring%29.md)
  Sent when a text view needs to determine if text in a specified range should be changed.
- [func textView(NSTextView, shouldChangeTextInRanges: [NSValue], replacementStrings: [String]?) -> Bool](./textview%28_,shouldchangetextinranges,replacementstrings%29.md)
  Sent when a text view needs to determine if text in an array of specified ranges should be changed.
- [func textViewDidChangeTypingAttributes(Notification)](./textviewdidchangetypingattributes%28_%29.md)
  Sent when a text view’s typing attributes change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:shouldchangetypingattributes:toattributes:))*