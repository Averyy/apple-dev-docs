# color

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The color of the ink.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
var color: UIColor { get set }
```

## Discussion

The alpha of the final color may vary due to input from Apple Pencil. For example, light pressure from Apple Pencil introduces more transparency into the final color, while additional force increases opacity to create a more solid line.

## See Also

### Getting the inking tool attributes
- [var color: NSColor](./color-22zaw.md)
  The color of the ink.
- [var width: CGFloat](./width.md)
  The width of the ink.
- [var ink: PKInk](./ink.md)
  The ink used by this inking tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct/color-5xmlo)*