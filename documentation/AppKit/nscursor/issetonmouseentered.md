# isSetOnMouseEntered

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](./mouseentered%28with%29.md) message.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: This method is not used.

## Declaration

```swift
var isSetOnMouseEntered: Bool { get }
```

```objc
@property (readonly, getter=isSetOnMouseEntered) BOOL setOnMouseEntered;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver will become current when it receives a [`mouseEntered(with:)`](./mouseentered%28with%29.md) message; otherwise, [`false`](../../Swift/false.md).

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
- [class var resizeUpDown: NSCursor](./resizeupdown.md)
  Returns the resize-up-and-down system cursor.
- [var isSetOnMouseExited: Bool](./issetonmouseexited.md)
  A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](./mouseexited%28with%29.md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/issetonmouseentered)*