# init(image:foregroundColorHint:backgroundColorHint:hotSpot:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes the cursor with the specified image and hot spot.

**Availability**:
- macOS 10.0+ - Deprecated in 10.12

> **Deprecated**: Color hints are ignored. Use [`init(image:hotSpot:)`](./init%28image,hotspot%29.md) instead.

## Declaration

```swift
convenience init(image newImage: NSImage, foregroundColorHint fg: NSColor?, backgroundColorHint bg: NSColor?, hotSpot: NSPoint)
```

```objc
- (instancetype) initWithImage:(NSImage *) newImage foregroundColorHint:(NSColor *) fg backgroundColorHint:(NSColor *) bg hotSpot:(NSPoint) hotSpot;
```

## Return Value

The initialized cursor object.

## Parameters

- `newImage`: The image to assign to the cursor.
- `fg`: The foreground color. This is currently ignored.
- `bg`: The background color. This is currently ignored.
- `hotSpot`: The point to assign as the cursor’s hot spot.

## See Also

### Deprecated methods
- [func mouseEntered(with: NSEvent)](./mouseentered%28with%29.md)
  Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.
- [func setOnMouseEntered(Bool)](./setonmouseentered%28_%29.md)
  Specifies whether the receiver accepts [`mouseEntered(with:)`](./mouseentered%28with%29.md) events.
- [func mouseExited(with: NSEvent)](./mouseexited%28with%29.md)
  Automatically sent to the receiver when the cursor exits a cursor rectangle owned by the receiver.
- [func setOnMouseExited(Bool)](./setonmouseexited%28_%29.md)
  Sets whether the receiver accepts [`mouseExited(with:)`](./mouseexited%28with%29.md) events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/init(image:foregroundcolorhint:backgroundcolorhint:hotspot:))*