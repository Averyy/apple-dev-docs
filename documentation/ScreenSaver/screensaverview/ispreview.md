# isPreview

**Framework**: Screen Saver  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the screen saver view is set to a size suitable for previewing its content.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var isPreview: Bool { get }
```

```objc
@property (atomic, readonly, getter=isPreview) BOOL preview;
```

## Discussion

The system sets the value of this property to [`true`](../../Swift/true.md) when it creates a smaller preview of your screen saver. When the value is [`false`](../../Swift/false.md), your view matches the size of the screen. Use this property to adjust the content you present. For example, you might change the drawing parameters or data you display in your view.

## See Also

### Drawing the view
- [func draw(NSRect)](./draw%28_%29.md)
  Draws the screen saver view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/ispreview)*