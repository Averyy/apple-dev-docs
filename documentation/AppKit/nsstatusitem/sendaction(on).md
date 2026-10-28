# sendAction(on:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the conditions on which the status item sends action messages to its target.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use the [`button`](./button.md) property.

## Declaration

```swift
func sendAction(on mask: NSEvent.EventTypeMask) -> Int
```

```objc
- (NSInteger) sendActionOn:(NSEventMask) mask;
```

## Return Value

A bit mask containing the previous settings. This bit mask uses the same values as specified in the `mask` parameter.

## Parameters

- `mask`: Takes one or more of the following bit masks described in `Getting Unicode Values` section of the `NSEvent` class reference: `NSLeftMouseUpMask`, `NSLeftMouseDownMask`, `NSLeftMouseDraggedMask`, and `NSPeriodicMask`. Bitwise-OR multiple bit masks.

## See Also

### Deprecated methods
- [func popUpMenu(NSMenu)](./popupmenu%28_%29.md)
  Displays a menu under a custom status bar item.
- [func drawStatusBarBackground(in: NSRect, withHighlight: Bool)](./drawstatusbarbackground%28in,withhighlight%29.md)
  Draws the menu background pattern for a custom status-bar item in regular or highlight pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/sendaction(on:))*