# PKEraserTool.EraserType

**Framework**: PencilKit  
**Kind**: enum

Constants that indicate the behavior of the eraser.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum EraserType
```

## Topics

### Eraser types
- [PKEraserTool.EraserType.vector](pkerasertool-swift.struct/erasertype-swift.enum/vector.md)
  An eraser that removes an entire drawn line.
- [PKEraserTool.EraserType.bitmap](pkerasertool-swift.struct/erasertype-swift.enum/bitmap.md)
  An eraser that removes only those portions of the drawing it touches.
- [PKEraserTool.EraserType.fixedWidthBitmap](pkerasertool-swift.struct/erasertype-swift.enum/fixedwidthbitmap.md)
### Getting the width information
- [var defaultWidth: CGFloat](pkerasertool-swift.struct/erasertype-swift.enum/defaultwidth.md)
  The default width for an eraser type.
- [var validWidthRange: ClosedRange<CGFloat>](pkerasertool-swift.struct/erasertype-swift.enum/validwidthrange.md)
  The valid width range for an eraser type.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var eraserType: PKEraserTool.EraserType](pkerasertool-swift.struct/erasertype-swift.property.md)
  The behavior adopted by the eraser when deleting content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkerasertool-swift.struct/erasertype-swift.enum)*