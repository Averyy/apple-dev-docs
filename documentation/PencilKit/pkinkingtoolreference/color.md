# color

**Framework**: PencilKit  
**Kind**: property

The color of the ink.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var color: NSColor { get }
```

#### Discussion

The alpha of the final color may vary due to input from Apple Pencil. For example, light pressure from Apple Pencil introduces more transparency into the final color, while additional force increases opacity to create a more solid line.

## See Also

- [var width: CGFloat](pkinkingtoolreference/width.md)
  The base line width for new content.
- [var ink: PKInk](pkinkingtoolreference/ink.md)
  The ink that this tool creates strokes with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/color)*