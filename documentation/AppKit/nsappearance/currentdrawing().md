# currentDrawing()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

The appearance that the system uses for color and asset resolution, and that’s active for drawing, usually from locking focus on a view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func currentDrawing() -> NSAppearance
```

#### Return Value

The current appearance used for drawing.

## See Also

### Getting and Setting the Current Appearance
- [func performAsCurrentDrawingAppearance(() -> Void)](./performascurrentdrawingappearance%28_%29.md)
  Sets the appearance to be the active drawing appearance and perform the specified block.
- [class var current: NSAppearance!](./current.md)
  Returns the appearance object that’s active on the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/currentdrawing())*