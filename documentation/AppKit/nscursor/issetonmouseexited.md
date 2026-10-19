# isSetOnMouseExited

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var isSetOnMouseExited: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [class var currentSystem: NSCursor?](nscursor/currentsystem.md)
  Returns the current system cursor.
- [class var resizeDown: NSCursor](nscursor/resizedown.md)
  Returns the resize-down system cursor.
- [class var resizeLeft: NSCursor](nscursor/resizeleft.md)
  Returns the resize-left system cursor.
- [class var resizeLeftRight: NSCursor](nscursor/resizeleftright.md)
  Returns the resize-left-and-right system cursor.
- [class var resizeRight: NSCursor](nscursor/resizeright.md)
  Returns the resize-right system cursor.
- [class var resizeUp: NSCursor](nscursor/resizeup.md)
  Returns the resize-up system cursor.
- [class var resizeUpDown: NSCursor](nscursor/resizeupdown.md)
  Returns the resize-up-and-down system cursor.
- [var isSetOnMouseEntered: Bool](nscursor/issetonmouseentered.md)
  A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/issetonmouseexited)*