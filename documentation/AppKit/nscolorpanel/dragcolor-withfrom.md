# dragColor(_:with:from:)

**Framework**: AppKit  
**Kind**: method

Drags a color into a destination view from the specified source view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class func dragColor(_ color: NSColor, with event: NSEvent, from sourceView: NSView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true)

#### Discussion

This method is usually invoked by the `mouseDown:` method of `sourceView`. The dragging mechanism handles all subsequent events.

Because it is a class method, [`dragColor(_:with:from:)`](nscolorpanel/dragcolor(_:with:from:).md) can be invoked whether or not the instance of `NSColorPanel` exists.

## Parameters

- `color`: The color to drag.
- `event`: The drag event.
- `sourceView`: The view from which the color was dragged.

## See Also

- [var color: NSColor](nscolorpanel/color.md)
  The color of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/dragcolor(_:with:from:))*