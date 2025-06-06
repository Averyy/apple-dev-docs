# performAsCurrentDrawingAppearance(_:)

**Framework**: AppKit  
**Kind**: method

Sets the appearance to be the active drawing appearance and perform the specified block.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func performAsCurrentDrawingAppearance(_ block: () -> Void)
```

#### Discussion

This method saves and restores the previous current appearance.

## Parameters

- `block`: The block to invoke after setting the appearance to be the current drawing appearance.

## See Also

- [class func currentDrawing() -> NSAppearance](nsappearance/currentdrawing.md)
  The appearance that the system uses for color and asset resolution, and that’s active for drawing, usually from locking focus on a view.
- [class var current: NSAppearance!](nsappearance/current.md)
  Returns the appearance object that’s active on the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/performascurrentdrawingappearance(_:))*