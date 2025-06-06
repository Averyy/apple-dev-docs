# PKInkingTool.InkType

**Framework**: PencilKit  
**Kind**: enum

The type that defines the shape of stroked lines.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum InkType
```

## Topics

### Choosing ink types
- [PKInkingTool.InkType.marker](pkinkingtool-swift.struct/inktype-swift.enum/marker.md)
  An inking tool that creates the appearance of a felt-tip marker.
- [PKInkingTool.InkType.pen](pkinkingtool-swift.struct/inktype-swift.enum/pen.md)
  An inking tool that creates the appearance of a pen-based drawing.
- [PKInkingTool.InkType.pencil](pkinkingtool-swift.struct/inktype-swift.enum/pencil.md)
  An inking tool that creates the appearance of a narrow line from a pencil.
- [PKInkingTool.InkType.monoline](pkinkingtool-swift.struct/inktype-swift.enum/monoline.md)
  An inking tool that creates the appearance of a monoline pen.
- [PKInkingTool.InkType.fountainPen](pkinkingtool-swift.struct/inktype-swift.enum/fountainpen.md)
  An inking tool that creates the appearance of a calligraphy pen.
- [PKInkingTool.InkType.watercolor](pkinkingtool-swift.struct/inktype-swift.enum/watercolor.md)
  An inking tool that creates the appearance of a watercolor brush.
- [PKInkingTool.InkType.crayon](pkinkingtool-swift.struct/inktype-swift.enum/crayon.md)
  An inking tool that creates the appearance of a crayon.
### Getting the width information
- [var defaultWidth: CGFloat](pkinkingtool-swift.struct/inktype-swift.enum/defaultwidth.md)
  The default line width for the specified tool type.
- [var validWidthRange: ClosedRange<CGFloat>](pkinkingtool-swift.struct/inktype-swift.enum/validwidthrange.md)
  The range of widths allowed for an ink of this type.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](pkinkingtool-swift.struct/inktype-swift.enum/requiredcontentversion.md)
  The version of PencilKit necessary to use the ink type.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var inkType: PKInkingTool.InkType](pkinkingtool-swift.struct/inktype-swift.property.md)
  The tool type that determines the shape of the rendered content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct/inktype-swift.enum)*