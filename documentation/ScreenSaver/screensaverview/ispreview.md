# isPreview

**Framework**: Screen Saver  
**Kind**: property

A Boolean value that indicates whether the screen saver view is set to a size suitable for previewing its content.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var isPreview: Bool { get }
```

#### Discussion

The system sets the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true) when it creates a smaller preview of your screen saver. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), your view matches the size of the screen. Use this property to adjust the content you present. For example, you might change the drawing parameters or data you display in your view.

## See Also

- [func draw(NSRect)](screensaverview/draw(_:).md)
  Draws the screen saver view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/ispreview)*