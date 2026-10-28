# popUpMenu(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays a menu under a custom status bar item.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use the [`menu`](./menu.md) property instead.

## Declaration

```swift
func popUpMenu(_ menu: NSMenu)
```

```objc
- (void) popUpStatusItemMenu:(NSMenu *) menu;
```

## Discussion

You can use this method to cause a popup menu to appear under a custom status bar item when the user clicks the item. Note that the view of the status item must exist (that is, it must not be `nil`).

## Parameters

- `menu`: The `NSMenu` object to display.

## See Also

### Deprecated methods
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](./sendaction%28on%29.md)
  Sets the conditions on which the status item sends action messages to its target.
- [func drawStatusBarBackground(in: NSRect, withHighlight: Bool)](./drawstatusbarbackground%28in,withhighlight%29.md)
  Draws the menu background pattern for a custom status-bar item in regular or highlight pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/popupmenu(_:))*