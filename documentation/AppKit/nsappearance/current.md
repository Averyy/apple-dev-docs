# current

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the appearance object that’s active on the current thread.

**Availability**:
- macOS 10.9+ - Deprecated in 12.0

> **Deprecated**: Use [`performAsCurrentDrawingAppearance(_:)`](./performascurrentdrawingappearance%28_%29.md) to temporarily set the drawing appearance, or [`currentDrawingAppearance`](./currentdrawingappearance.md) to access the current drawing appearance.

## Declaration

```swift
class var current: NSAppearance! { get set }
```

```objc
@property (class, strong, null_resettable) NSAppearance * currentAppearance;
```

## Return Value

The appearance object that’s set on the current thread.

## Discussion

When a UI element draws to the screen, it automatically sets its appearance object to the active appearance on the current thread.

## See Also

### Getting and Setting the Current Appearance
- [class func currentDrawing() -> NSAppearance](./currentdrawing%28%29.md)
  The appearance that the system uses for color and asset resolution, and that’s active for drawing, usually from locking focus on a view.
- [func performAsCurrentDrawingAppearance(() -> Void)](./performascurrentdrawingappearance%28_%29.md)
  Sets the appearance to be the active drawing appearance and perform the specified block.
- [currentDrawingAppearance](./currentdrawingappearance.md)
  The appearance that the system uses for color and asset resolution, and that’s active for drawing, usually from locking focus on a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/current)*