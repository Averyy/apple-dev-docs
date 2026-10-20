# currentSystem

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the current system cursor.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.6+ - Deprecated in 27.0

> **Deprecated**: No longer recommended. Use ScreenCaptureKit to capture the screen. Use the `showsCursor` property on `SCStreamConfiguration` to control whether or not to include the cursor in the capture. Or, use `NSCursor.currentCursor` if needing to just get the current cursor for this application.

## Declaration

```swift
class var currentSystem: NSCursor? { get }
```

```objc
@property (class, strong, readonly, nullable) NSCursor * currentSystemCursor;
```

#### Return Value

A cursor whose image and hot spot match those of the currently-displayed cursor on the system

#### Discussion

This method returns the current system cursor regardless of which application set the cursor, and whether Cocoa or Carbon APIs were used to set it.

This method replaces the now deprecated QDGetCursorData function.

## See Also

### Deprecated properties
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
- [var isSetOnMouseEntered: Bool](./issetonmouseentered.md)
  A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](./mouseentered%28with%29.md) message.
- [var isSetOnMouseExited: Bool](./issetonmouseexited.md)
  A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](./mouseexited%28with%29.md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/currentsystem)*