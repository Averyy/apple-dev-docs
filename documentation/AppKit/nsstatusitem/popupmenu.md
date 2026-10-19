# popUpMenu(_:)

**Framework**: AppKit  
**Kind**: method

Displays a menu under a custom status bar item.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func popUpMenu(_ menu: NSMenu)
```

#### Discussion

You can use this method to cause a popup menu to appear under a custom status bar item when the user clicks the item. Note that the view of the status item must exist (that is, it must not be `nil`).

## Parameters

- `menu`: The `NSMenu` object to display.

## See Also

- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nsstatusitem/sendaction(on:).md)
  Sets the conditions on which the status item sends action messages to its target.
- [func drawStatusBarBackground(in: NSRect, withHighlight: Bool)](nsstatusitem/drawstatusbarbackground(in:withhighlight:).md)
  Draws the menu background pattern for a custom status-bar item in regular or highlight pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/popupmenu(_:))*