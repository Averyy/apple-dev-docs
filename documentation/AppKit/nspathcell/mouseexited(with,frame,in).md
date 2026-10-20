# mouseExited(with:frame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Hides the cell component over which the mouse is hovering.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func mouseExited(with event: NSEvent, frame: NSRect, in view: NSView)
```

```objc
- (void) mouseExited:(NSEvent *) event withFrame:(NSRect) frame inView:(NSView *) view;
```

## Parameters

- `event`: The mouse-exited event.
- `frame`: The frame in which the cell is located.
- `view`: The view in which the cell is located.

## See Also

### Displaying Hidden Components
- [func mouseEntered(with: NSEvent, frame: NSRect, in: NSView)](./mouseentered%28with,frame,in%29.md)
  Displays the cell component over which the mouse is hovering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/mouseexited(with:frame:in:))*