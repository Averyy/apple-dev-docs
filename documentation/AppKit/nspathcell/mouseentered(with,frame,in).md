# mouseEntered(with:frame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the cell component over which the mouse is hovering.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func mouseEntered(with event: NSEvent, frame: NSRect, in view: NSView)
```

```objc
- (void) mouseEntered:(NSEvent *) event withFrame:(NSRect) frame inView:(NSView *) view;
```

#### Discussion

The `NSPathCell` object dynamically animates to display the component that the mouse is hovering over using mouse-entered and mouse-exited events. The control should call these methods to correctly display the hovered component to the user. The control can acquire rectangles to track using [`rect(of:withFrame:in:)`](./rect%28of,withframe,in%29.md).

## Parameters

- `event`: The mouse-entered event.
- `frame`: The frame in which the cell is located.
- `view`: The view in which the cell is located.

## See Also

### Displaying Hidden Components
- [func mouseExited(with: NSEvent, frame: NSRect, in: NSView)](./mouseexited%28with,frame,in%29.md)
  Hides the cell component over which the mouse is hovering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/mouseentered(with:frame:in:))*