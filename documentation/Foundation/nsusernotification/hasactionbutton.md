# hasActionButton

**Framework**: Foundation  
**Kind**: property

A Boolean value that specifies whether the notification displays an action button.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var hasActionButton: Bool { get set }
```

#### Discussion

Set to [`false`](https://developer.apple.com/documentation/swift/false) if the notification has no action button. This is the case for notifications that are purely for information and have no user action. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var actionButtonTitle: String](nsusernotification/actionbuttontitle.md)
  Specifies the title of the action button displayed in the notification.
- [var otherButtonTitle: String](nsusernotification/otherbuttontitle.md)
  Specifies a custom title for the close button in an alert-style notification.
- [var hasReplyButton: Bool](nsusernotification/hasreplybutton.md)
  A Boolean value that specifies whether the notification displays a reply button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/hasactionbutton)*