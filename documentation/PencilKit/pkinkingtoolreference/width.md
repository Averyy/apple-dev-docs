# width

**Framework**: PencilKit  
**Kind**: property

The base line width for new content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var width: CGFloat { get }
```

#### Discussion

The actual line width at any given point varies based on input from Apple Pencil. For finger-based drawing, the line width is equal to the value in this property.

## See Also

- [var color: UIColor](pkinkingtoolreference/color.md)
  The color of the ink.
- [var ink: PKInk](pkinkingtoolreference/ink.md)
  The ink that this tool creates strokes with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/width)*