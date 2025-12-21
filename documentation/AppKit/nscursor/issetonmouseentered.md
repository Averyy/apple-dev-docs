# isSetOnMouseEntered

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) message.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var isSetOnMouseEntered: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver will become current when it receives a [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) message; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [convenience init(image: NSImage, foregroundColorHint: NSColor?, backgroundColorHint: NSColor?, hotSpot: NSPoint)](nscursor/init(image:foregroundcolorhint:backgroundcolorhint:hotspot:).md)
  Initializes the cursor with the specified image and hot spot.
- [func mouseEntered(with: NSEvent)](nscursor/mouseentered(with:).md)
  Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.
- [func setOnMouseEntered(Bool)](nscursor/setonmouseentered(_:).md)
  Specifies whether the receiver accepts [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) events.
- [func mouseExited(with: NSEvent)](nscursor/mouseexited(with:).md)
  Automatically sent to the receiver when the cursor exits a cursor rectangle owned by the receiver.
- [func setOnMouseExited(Bool)](nscursor/setonmouseexited(_:).md)
  Sets whether the receiver accepts [`mouseExited(with:)`](nscursor/mouseexited(with:).md) events.
- [var isSetOnMouseExited: Bool](nscursor/issetonmouseexited.md)
  A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/issetonmouseentered)*