# sendsActionOnArrowKeys

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether pressing an arrow key causes an action message to be sent.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var sendsActionOnArrowKeys: Bool { get set }
```

#### Discussion

When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), pressing an arrow key scrolls the browser. When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), it also sends the action message specified by [`action`](nscontrol/action.md).

## See Also

- [var doubleAction: Selector?](nsbrowser/doubleaction.md)
  The browser’s double-click action method.
- [func sendAction() -> Bool](nsbrowser/sendaction.md)
  Sends the action message to the target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/sendsactiononarrowkeys)*