# current

**Framework**: AppKit  
**Kind**: property

Returns the appearance object that’s active on the current thread.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class var current: NSAppearance! { get set }
```

#### Return Value

The appearance object that’s set on the current thread.

#### Discussion

When a UI element draws to the screen, it automatically sets its appearance object to the active appearance on the current thread.

## See Also

- [class func currentDrawing() -> NSAppearance](nsappearance/currentdrawing.md)
  The appearance that the system uses for color and asset resolution, and that’s active for drawing, usually from locking focus on a view.
- [func performAsCurrentDrawingAppearance(() -> Void)](nsappearance/performascurrentdrawingappearance(_:).md)
  Sets the appearance to be the active drawing appearance and perform the specified block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/current)*