# sendAction()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sends the action message to the target.

**Availability**:
- macOS

## Declaration

```swift
func sendAction() -> Bool
```

```objc
- (BOOL) sendAction;
```

## Return Value

[`true`](../../Swift/true.md) if successful; [`false`](../../Swift/false.md) if no target for the message could be found.

## See Also

### Related Documentation
- [func doDoubleClick(Any?)](./dodoubleclick%28_%29.md)
  Responds to double clicks in a column of the browser.
- [func doClick(Any?)](./doclick%28_%29.md)
  Responds to (single) mouse clicks in a column of the browser.
### Managing Actions
- [var doubleAction: Selector?](./doubleaction.md)
  The browser’s double-click action method.
- [var sendsActionOnArrowKeys: Bool](./sendsactiononarrowkeys.md)
  A Boolean that indicates whether pressing an arrow key causes an action message to be sent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/sendaction())*