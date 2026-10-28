# drawStatusBarBackground(in:withHighlight:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the menu background pattern for a custom status-bar item in regular or highlight pattern.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: The standard [`button`](./button.md) handles highlight drawing automatically, so this method is no longer necessary.

## Declaration

```swift
func drawStatusBarBackground(in rect: NSRect, withHighlight highlight: Bool)
```

```objc
- (void) drawStatusBarBackgroundInRect:(NSRect) rect withHighlight:(BOOL) highlight;
```

## Discussion

You can use this method to help a custom status-bar item emulate the behavior of a standard item.

## Parameters

- `rect`: A rectangle defining the area of a custom status-bar item.
- `highlight`: [`true`](../../Swift/true.md) to draw the background pattern in the standard highlight pattern, [`false`](../../Swift/false.md) to not highlight the pattern.

## See Also

### Deprecated methods
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](./sendaction%28on%29.md)
  Sets the conditions on which the status item sends action messages to its target.
- [func popUpMenu(NSMenu)](./popupmenu%28_%29.md)
  Displays a menu under a custom status bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/drawstatusbarbackground(in:withhighlight:))*