# mouseExited(with:)

**Framework**: AppKit  
**Kind**: method

Automatically sent to the receiver when the cursor exits a cursor rectangle owned by the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func mouseExited(with event: NSEvent)
```

#### Discussion

Like [`mouseEntered(with:)`](nscursor/mouseentered(with:).md), this message is part of the class interface only so you can override it.

For a more complete explanation, see [`Mouse-Tracking and Cursor-Update Events`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/MouseTrackingEvents/MouseTrackingEvents.html#//apple_ref/doc/uid/10000060i-CH11) and the NSView method [`addTrackingRect(_:owner:userData:assumeInside:)`](nsview/addtrackingrect(_:owner:userdata:assumeinside:).md).

## Parameters

- `event`: The event generated when the cursor exits the cursor rectangle.

## See Also

- [class func pop()](nscursor/pop-swift.type.method.md)
  Pops the current cursor off the top of the stack.
- [func pop()](nscursor/pop-swift.method.md)
  Sends a [`pop()`](nscursor/pop()-swift.type.method.md) message to the receiver’s class.
- [func push()](nscursor/push.md)
  Puts the receiver on top of the cursor stack and makes it the current cursor.
- [func set()](nscursor/set.md)
  Makes the receiver the current cursor.
- [func mouseEntered(with: NSEvent)](nscursor/mouseentered(with:).md)
  Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.
- [func setOnMouseEntered(Bool)](nscursor/setonmouseentered(_:).md)
  Specifies whether the receiver accepts [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) events.
- [var isSetOnMouseEntered: Bool](nscursor/issetonmouseentered.md)
  A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) message.
- [func setOnMouseExited(Bool)](nscursor/setonmouseexited(_:).md)
  Sets whether the receiver accepts [`mouseExited(with:)`](nscursor/mouseexited(with:).md) events.
- [var isSetOnMouseExited: Bool](nscursor/issetonmouseexited.md)
  A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/mouseexited(with:))*