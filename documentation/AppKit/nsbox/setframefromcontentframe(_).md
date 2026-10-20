# setFrameFromContentFrame(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Places the receiver so its content view lies on the specified frame.

**Availability**:
- macOS

## Declaration

```swift
func setFrameFromContentFrame(_ contentFrame: NSRect)
```

```objc
- (void) setFrameFromContentFrame:(NSRect) contentFrame;
```

## Parameters

- `contentFrame`: The rectangle specifying the frame of the box’s content view, reckoned in the coordinate system of the box’s superview. The box is marked for redisplay.

## See Also

### Related Documentation
- [var contentViewMargins: NSSize](./contentviewmargins.md)
  The distances between the border and the content view.
- [var needsDisplay: Bool](../nsview/needsdisplay.md)
  A Boolean value that determines whether the view needs to be redrawn before being displayed.
- [var frame: NSRect](../nsview/frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
### Sizing
- [func sizeToFit()](./sizetofit%28%29.md)
  Resizes and moves the receiver’s content view so it just encloses its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbox/setframefromcontentframe(_:))*