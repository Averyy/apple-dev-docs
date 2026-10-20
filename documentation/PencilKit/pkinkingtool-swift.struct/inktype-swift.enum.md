# PKInkingTool.InkType

**Framework**: PencilKit  
**Kind**: enum  
**Role**: Enumeration

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
- [PKInkingTool.InkType.marker](./inktype-swift.enum/marker.md)
  An inking tool that creates the appearance of a felt-tip marker.
- [PKInkingTool.InkType.pen](./inktype-swift.enum/pen.md)
  An inking tool that creates the appearance of a pen-based drawing.
- [PKInkingTool.InkType.pencil](./inktype-swift.enum/pencil.md)
  An inking tool that creates the appearance of a narrow line from a pencil.
- [PKInkingTool.InkType.monoline](./inktype-swift.enum/monoline.md)
  An inking tool that creates the appearance of a monoline pen.
- [PKInkingTool.InkType.fountainPen](./inktype-swift.enum/fountainpen.md)
  An inking tool that creates the appearance of a calligraphy pen.
- [PKInkingTool.InkType.watercolor](./inktype-swift.enum/watercolor.md)
  An inking tool that creates the appearance of a watercolor brush.
- [PKInkingTool.InkType.crayon](./inktype-swift.enum/crayon.md)
  An inking tool that creates the appearance of a crayon.
### Getting the width information
- [var defaultWidth: CGFloat](./inktype-swift.enum/defaultwidth.md)
  The default line width for the specified tool type.
- [var validWidthRange: ClosedRange<CGFloat>](./inktype-swift.enum/validwidthrange.md)
  The range of widths allowed for an ink of this type.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](./inktype-swift.enum/requiredcontentversion.md)
  The version of PencilKit necessary to use the ink type.
### Enumeration Cases
- [PKInkingTool.InkType.reed](./inktype-swift.enum/reed.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Getting the tool type
- [var inkType: PKInkingTool.InkType](./inktype-swift.property.md)
  The tool type that determines the shape of the rendered content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct/inktype-swift.enum)*