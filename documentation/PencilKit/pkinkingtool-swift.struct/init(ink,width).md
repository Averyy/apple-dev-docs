# init(ink:width:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Create an inking tool with the specified ink and width.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(ink: PKInk, width: CGFloat)
```

## Parameters

- `ink`: The shape of the tool, which can be [`PKInkTypeMarker`](../pkinktypemarker.md), [`PKInkTypePen`](../pkinktypepen.md), or [`PKInkTypePencil`](../pkinktypepencil.md).
- `width`: The width of a line drawn with the tool.

## See Also

### Creating an inking tool
- [init(PKInkingTool.InkType, color: UIColor, width: CGFloat?)](./init%28_,color,width%29-2l7v.md)
  Creates an ink tool object with the specified color and line width values.
- [init(PKInkingTool.InkType, color: NSColor, width: CGFloat?)](./init%28_,color,width%29-4i3ft.md)
  Creates an ink tool object with the specified color and line width values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct/init(ink:width:))*