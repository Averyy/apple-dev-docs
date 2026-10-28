# setOnMouseEntered(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies whether the receiver accepts [`mouseEntered(with:)`](./mouseentered%28with%29.md) events.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: This method is not used.

## Declaration

```swift
func setOnMouseEntered(_ flag: Bool)
```

```objc
- (void) setOnMouseEntered:(BOOL) flag;
```

## Discussion

Accepting [`mouseEntered(with:)`](./mouseentered%28with%29.md) event messages allows the cursor to be made the current cursor when the cursor enters a view’s cursor rectangle.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the receiver accepts future [`mouseEntered(with:)`](./mouseentered%28with%29.md) event messages; otherwise it ignores them.

## See Also

### Deprecated methods
- [convenience init(image: NSImage, foregroundColorHint: NSColor?, backgroundColorHint: NSColor?, hotSpot: NSPoint)](./init%28image,foregroundcolorhint,backgroundcolorhint,hotspot%29.md)
  Initializes the cursor with the specified image and hot spot.
- [func mouseEntered(with: NSEvent)](./mouseentered%28with%29.md)
  Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.
- [func mouseExited(with: NSEvent)](./mouseexited%28with%29.md)
  Automatically sent to the receiver when the cursor exits a cursor rectangle owned by the receiver.
- [func setOnMouseExited(Bool)](./setonmouseexited%28_%29.md)
  Sets whether the receiver accepts [`mouseExited(with:)`](./mouseexited%28with%29.md) events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/setonmouseentered(_:))*