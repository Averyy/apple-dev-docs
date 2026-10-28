# dragColor(_:with:from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Drags a color into a destination view from the specified source view.

**Availability**:
- macOS

## Declaration

```swift
class func dragColor(_ color: NSColor, with event: NSEvent, from sourceView: NSView) -> Bool
```

```objc
+ (BOOL) dragColor:(NSColor *) color withEvent:(NSEvent *) event fromView:(NSView *) sourceView;
```

## Return Value

[`true`](../../Swift/true.md)

## Discussion

This method is usually invoked by the `mouseDown:` method of `sourceView`. The dragging mechanism handles all subsequent events.

Because it is a class method, [`dragColor(_:with:from:)`](./dragcolor%28_,with,from%29.md) can be invoked whether or not the instance of `NSColorPanel` exists.

## Parameters

- `color`: The color to drag.
- `event`: The drag event.
- `sourceView`: The view from which the color was dragged.

## See Also

### Setting color
- [var color: NSColor](./color.md)
  The color of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/dragcolor(_:with:from:))*