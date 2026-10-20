# sendsActionOnArrowKeys

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether pressing an arrow key causes an action message to be sent.

**Availability**:
- macOS

## Declaration

```swift
var sendsActionOnArrowKeys: Bool { get set }
```

```objc
@property BOOL sendsActionOnArrowKeys;
```

#### Discussion

When the value of this property is [`false`](../../Swift/false.md), pressing an arrow key scrolls the browser. When the value of this property is [`true`](../../Swift/true.md), it also sends the action message specified by [`action`](../nscontrol/action.md).

## See Also

### Managing Actions
- [var doubleAction: Selector?](./doubleaction.md)
  The browser’s double-click action method.
- [func sendAction() -> Bool](./sendaction%28%29.md)
  Sends the action message to the target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/sendsactiononarrowkeys)*