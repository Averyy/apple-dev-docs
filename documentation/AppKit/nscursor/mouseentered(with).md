# mouseEntered(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: This method is not used.

## Declaration

```swift
func mouseEntered(with event: NSEvent)
```

```objc
- (void) mouseEntered:(NSEvent *) event;
```

#### Discussion

If used after [`setOnMouseEntered(_:)`](./setonmouseentered%28_%29.md) has been called with an argument of [`true`](../../Swift/true.md), [`mouseEntered(with:)`](./mouseentered%28with%29.md) can make the receiver the current cursor.

In your programs, you won’t invoke [`mouseEntered(with:)`](./mouseentered%28with%29.md) explicitly. It’s only included in the class interface so you can override it.

For more information, see [`addTrackingRect(_:owner:userData:assumeInside:)`](../nsview/addtrackingrect%28_,owner,userdata,assumeinside%29.md).

## Parameters

- `event`: The event generated when the cursor enters the cursor rectangle.

## See Also

### Deprecated methods
- [convenience init(image: NSImage, foregroundColorHint: NSColor?, backgroundColorHint: NSColor?, hotSpot: NSPoint)](./init%28image,foregroundcolorhint,backgroundcolorhint,hotspot%29.md)
  Initializes the cursor with the specified image and hot spot.
- [func setOnMouseEntered(Bool)](./setonmouseentered%28_%29.md)
  Specifies whether the receiver accepts [`mouseEntered(with:)`](./mouseentered%28with%29.md) events.
- [func mouseExited(with: NSEvent)](./mouseexited%28with%29.md)
  Automatically sent to the receiver when the cursor exits a cursor rectangle owned by the receiver.
- [func setOnMouseExited(Bool)](./setonmouseexited%28_%29.md)
  Sets whether the receiver accepts [`mouseExited(with:)`](./mouseexited%28with%29.md) events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/mouseentered(with:))*