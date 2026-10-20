# resizeUpDown

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the resize-up-and-down system cursor.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use either `+[NSCursor rowResizeCursorInDirections:]` or `+[NSCursor frameResizeCursorFromPosition:inDirections:]` instead, depending on whether a divider is being re-positioned or a rectangular frame is being resized.

## Declaration

```swift
class var resizeUpDown: NSCursor { get }
```

```objc
@property (class, strong, readonly) NSCursor * resizeUpDownCursor;
```

#### Return Value

The resize-up-and-down cursor. This cursor is used when moving or resizing an object and the object can be moved up or down.

## See Also

### Deprecated properties
- [class var currentSystem: NSCursor?](./currentsystem.md)
  Returns the current system cursor.
- [class var resizeDown: NSCursor](./resizedown.md)
  Returns the resize-down system cursor.
- [class var resizeLeft: NSCursor](./resizeleft.md)
  Returns the resize-left system cursor.
- [class var resizeLeftRight: NSCursor](./resizeleftright.md)
  Returns the resize-left-and-right system cursor.
- [class var resizeRight: NSCursor](./resizeright.md)
  Returns the resize-right system cursor.
- [class var resizeUp: NSCursor](./resizeup.md)
  Returns the resize-up system cursor.
- [var isSetOnMouseEntered: Bool](./issetonmouseentered.md)
  A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](./mouseentered%28with%29.md) message.
- [var isSetOnMouseExited: Bool](./issetonmouseexited.md)
  A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](./mouseexited%28with%29.md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/resizeupdown)*