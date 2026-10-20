# hasReplyButton

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the notification displays a reply button.

**Availability**:
- macOS 10.9+ - Deprecated in 11.0

## Declaration

```swift
var hasReplyButton: Bool { get set }
```

```objc
@property BOOL hasReplyButton;
```

#### Discussion

Set to [`true`](../../Swift/true.md) if the notification has a reply button. The default value is [`false`](../../Swift/false.md). If this property and [`hasActionButton`](./hasactionbutton.md) are both [`true`](../../Swift/true.md), the reply button is shown.

## See Also

### Displayed Notification Buttons
- [var hasActionButton: Bool](./hasactionbutton.md)
  A Boolean value that specifies whether the notification displays an action button.
- [var actionButtonTitle: String](./actionbuttontitle.md)
  Specifies the title of the action button displayed in the notification.
- [var otherButtonTitle: String](./otherbuttontitle.md)
  Specifies a custom title for the close button in an alert-style notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/hasreplybutton)*