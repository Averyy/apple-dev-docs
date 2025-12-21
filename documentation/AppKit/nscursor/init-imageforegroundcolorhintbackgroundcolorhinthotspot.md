# init(image:foregroundColorHint:backgroundColorHint:hotSpot:)

**Framework**: AppKit  
**Kind**: init

Initializes the cursor with the specified image and hot spot.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init(image newImage: NSImage, foregroundColorHint fg: NSColor?, backgroundColorHint bg: NSColor?, hotSpot: NSPoint)
```

#### Return Value

The initialized cursor object.

## Parameters

- `newImage`: The image to assign to the cursor.
- `fg`: The foreground color. This is currently ignored.
- `bg`: The background color. This is currently ignored.
- `hotSpot`: The point to assign as the cursor’s hot spot.

## See Also

- [func mouseEntered(with: NSEvent)](nscursor/mouseentered(with:).md)
  Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/init(image:foregroundcolorhint:backgroundcolorhint:hotspot:))*