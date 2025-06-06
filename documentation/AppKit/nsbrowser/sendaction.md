# sendAction()

**Framework**: AppKit  
**Kind**: method

Sends the action message to the target.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sendAction() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; [`false`](https://developer.apple.com/documentation/swift/false) if no target for the message could be found.

## See Also

- [func doDoubleClick(Any?)](nsbrowser/dodoubleclick(_:).md)
  Responds to double clicks in a column of the browser.
- [func doClick(Any?)](nsbrowser/doclick(_:).md)
  Responds to (single) mouse clicks in a column of the browser.
- [var doubleAction: Selector?](nsbrowser/doubleaction.md)
  The browser’s double-click action method.
- [var sendsActionOnArrowKeys: Bool](nsbrowser/sendsactiononarrowkeys.md)
  A Boolean that indicates whether pressing an arrow key causes an action message to be sent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/sendaction())*