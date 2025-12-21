# mouseEntered(with:)

**Framework**: AppKit  
**Kind**: method

Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func mouseEntered(with event: NSEvent)
```

#### Discussion

If used after [`setOnMouseEntered(_:)`](nscursor/setonmouseentered(_:).md) has been called with an argument of [`true`](https://developer.apple.com/documentation/Swift/true), [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) can make the receiver the current cursor.

In your programs, you won’t invoke [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) explicitly. It’s only included in the class interface so you can override it.

For a more complete explanation, see [`Mouse-Tracking and Cursor-Update Events`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/MouseTrackingEvents/MouseTrackingEvents.html#//apple_ref/doc/uid/10000060i-CH11) and the `NSView` method [`addTrackingRect(_:owner:userData:assumeInside:)`](nsview/addtrackingrect(_:owner:userdata:assumeinside:).md).

## Parameters

- `event`: The event generated when the cursor enters the cursor rectangle.

## See Also

- [convenience init(image: NSImage, foregroundColorHint: NSColor?, backgroundColorHint: NSColor?, hotSpot: NSPoint)](nscursor/init(image:foregroundcolorhint:backgroundcolorhint:hotspot:).md)
  Initializes the cursor with the specified image and hot spot.
- [func setOnMouseEntered(Bool)](nscursor/setonmouseentered(_:).md)
  Specifies whether the receiver accepts [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) events.
- [var isSetOnMouseEntered: Bool](nscursor/issetonmouseentered.md)
  A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) message.
- [func mouseExited(with: NSEvent)](nscursor/mouseexited(with:).md)
  Automatically sent to the receiver when the cursor exits a cursor rectangle owned by the receiver.
- [func setOnMouseExited(Bool)](nscursor/setonmouseexited(_:).md)
  Sets whether the receiver accepts [`mouseExited(with:)`](nscursor/mouseexited(with:).md) events.
- [var isSetOnMouseExited: Bool](nscursor/issetonmouseexited.md)
  A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/mouseentered(with:))*