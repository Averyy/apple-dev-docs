# PKEraserType

**Framework**: PencilKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the behavior of the eraser.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```c
enum PKEraserType : NSInteger;
```

## Topics

### Eraser types
- [PKEraserTypeVector](./pkerasertype/pkerasertypevector.md)
  An eraser that removes an entire drawn line.
- [PKEraserTypeBitmap](./pkerasertype/pkerasertypebitmap.md)
  An eraser that removes only those portions of the drawing it touches.
- [PKEraserTypeFixedWidthBitmap](./pkerasertype/pkerasertypefixedwidthbitmap.md)

## See Also

### Getting the eraser type
- [var eraserType: __PKEraserType](./pkerasertoolreference/erasertype.md)
  The behavior adopted by the eraser when deleting content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkerasertype)*