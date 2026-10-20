# PKEraserTool.EraserType

**Framework**: PencilKit  
**Kind**: enum  
**Role**: Enumeration

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
- [PKEraserTool.EraserType.vector](./erasertype-swift.enum/vector.md)
  An eraser that removes an entire drawn line.
- [PKEraserTool.EraserType.bitmap](./erasertype-swift.enum/bitmap.md)
  An eraser that removes only those portions of the drawing it touches.
- [PKEraserTool.EraserType.fixedWidthBitmap](./erasertype-swift.enum/fixedwidthbitmap.md)
### Getting the width information
- [var defaultWidth: CGFloat](./erasertype-swift.enum/defaultwidth.md)
  The default width for an eraser type.
- [var validWidthRange: ClosedRange<CGFloat>](./erasertype-swift.enum/validwidthrange.md)
  The valid width range for an eraser type.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Getting the eraser type
- [var eraserType: PKEraserTool.EraserType](./erasertype-swift.property.md)
  The behavior adopted by the eraser when deleting content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkerasertool-swift.struct/erasertype-swift.enum)*