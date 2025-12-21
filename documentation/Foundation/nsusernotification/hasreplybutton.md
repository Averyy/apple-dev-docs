# hasReplyButton

**Framework**: Foundation  
**Kind**: property

A Boolean value that specifies whether the notification displays a reply button.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var hasReplyButton: Bool { get set }
```

#### Discussion

Set to [`true`](https://developer.apple.com/documentation/Swift/true) if the notification has a reply button. The default value is [`false`](https://developer.apple.com/documentation/Swift/false). If this property and [`hasActionButton`](nsusernotification/hasactionbutton.md) are both [`true`](https://developer.apple.com/documentation/Swift/true), the reply button is shown.

## See Also

- [var hasActionButton: Bool](nsusernotification/hasactionbutton.md)
  A Boolean value that specifies whether the notification displays an action button.
- [var actionButtonTitle: String](nsusernotification/actionbuttontitle.md)
  Specifies the title of the action button displayed in the notification.
- [var otherButtonTitle: String](nsusernotification/otherbuttontitle.md)
  Specifies a custom title for the close button in an alert-style notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/hasreplybutton)*