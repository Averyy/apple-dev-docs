# performAsCurrentDrawingAppearance(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the appearance to be the active drawing appearance and perform the specified block.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func performAsCurrentDrawingAppearance(_ block: () -> Void)
```

```objc
- (void) performAsCurrentDrawingAppearance:(void (^)()) block;
```

## Discussion

This method saves and restores the previous current appearance.

## Parameters

- `block`: The block to invoke after setting the appearance to be the current drawing appearance.

## See Also

### Getting and Setting the Current Appearance
- [class func currentDrawing() -> NSAppearance](./currentdrawing%28%29.md)
  The appearance that the system uses for color and asset resolution, and that’s active for drawing, usually from locking focus on a view.
- [class var current: NSAppearance!](./current.md)
  Returns the appearance object that’s active on the current thread.
- [currentDrawingAppearance](./currentdrawingappearance.md)
  The appearance that the system uses for color and asset resolution, and that’s active for drawing, usually from locking focus on a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/performascurrentdrawingappearance(_:))*