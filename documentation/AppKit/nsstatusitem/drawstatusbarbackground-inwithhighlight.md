# drawStatusBarBackground(in:withHighlight:)

**Framework**: AppKit  
**Kind**: method

Draws the menu background pattern for a custom status-bar item in regular or highlight pattern.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func drawStatusBarBackground(in rect: NSRect, withHighlight highlight: Bool)
```

#### Discussion

You can use this method to help a custom status-bar item emulate the behavior of a standard item.

## Parameters

- `rect`: A rectangle defining the area of a custom status-bar item.
- `highlight`: [`true`](https://developer.apple.com/documentation/swift/true) to draw the background pattern in the standard highlight pattern, [`false`](https://developer.apple.com/documentation/swift/false) to not highlight the pattern.

## See Also

- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nsstatusitem/sendaction(on:).md)
  Sets the conditions on which the status item sends action messages to its target.
- [func popUpMenu(NSMenu)](nsstatusitem/popupmenu(_:).md)
  Displays a menu under a custom status bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/drawstatusbarbackground(in:withhighlight:))*