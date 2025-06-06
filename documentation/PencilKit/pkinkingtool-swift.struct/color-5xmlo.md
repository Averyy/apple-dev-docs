# color

**Framework**: PencilKit  
**Kind**: property

The color of the ink.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var color: UIColor { get set }
```

#### Discussion

The alpha of the final color may vary due to input from Apple Pencil. For example, light pressure from Apple Pencil introduces more transparency into the final color, while additional force increases opacity to create a more solid line.

## See Also

- [var color: NSColor](pkinkingtool-swift.struct/color-22zaw.md)
  The color of the ink.
- [var width: CGFloat](pkinkingtool-swift.struct/width.md)
  The width of the ink.
- [var ink: PKInk](pkinkingtool-swift.struct/ink.md)
  The ink used by this inking tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct/color-5xmlo)*