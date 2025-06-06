# width

**Framework**: PencilKit  
**Kind**: property

The width of the ink.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var width: CGFloat { get set }
```

#### Discussion

The actual line width at any given point varies based on input from Apple Pencil. For finger-based drawing, the line width is equal to the value in this property.

## See Also

- [var color: UIColor](pkinkingtool-swift.struct/color-5xmlo.md)
  The color of the ink.
- [var color: NSColor](pkinkingtool-swift.struct/color-22zaw.md)
  The color of the ink.
- [var ink: PKInk](pkinkingtool-swift.struct/ink.md)
  The ink used by this inking tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct/width)*