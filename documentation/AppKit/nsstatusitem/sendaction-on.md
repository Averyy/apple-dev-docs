# sendAction(on:)

**Framework**: AppKit  
**Kind**: method

Sets the conditions on which the status item sends action messages to its target.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func sendAction(on mask: NSEvent.EventTypeMask) -> Int
```

#### Return Value

A bit mask containing the previous settings. This bit mask uses the same values as specified in the `mask` parameter.

## Parameters

- `mask`: Takes one or more of the following bit masks described in `Getting Unicode Values` section of the `NSEvent` class reference: `NSLeftMouseUpMask`, `NSLeftMouseDownMask`, `NSLeftMouseDraggedMask`, and `NSPeriodicMask`. Bitwise-OR multiple bit masks.

## See Also

- [func popUpMenu(NSMenu)](nsstatusitem/popupmenu(_:).md)
  Displays a menu under a custom status bar item.
- [func drawStatusBarBackground(in: NSRect, withHighlight: Bool)](nsstatusitem/drawstatusbarbackground(in:withhighlight:).md)
  Draws the menu background pattern for a custom status-bar item in regular or highlight pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/sendaction(on:))*