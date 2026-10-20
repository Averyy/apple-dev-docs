# init(_:color:width:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates an ink tool object with the specified color and line width values.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(_ inkType: PKInkingTool.InkType, color: NSColor = NSColor.black, width: CGFloat? = nil)
```

## Parameters

- `inkType`: The shape of the tool, which can be [`PKInkingTool.InkType.marker`](./inktype-swift.enum/marker.md), [`PKInkingTool.InkType.pen`](./inktype-swift.enum/pen.md), or [`PKInkingTool.InkType.pencil`](./inktype-swift.enum/pencil.md).
- `color`: The color to apply to drawn lines.
- `width`: The base width to apply to any drawn lines. The value in the `inkType` parameter and input from Apple Pencil affects the final width.

## See Also

### Creating an inking tool
- [init(PKInkingTool.InkType, color: UIColor, width: CGFloat?)](./init%28_,color,width%29-2l7v.md)
  Creates an ink tool object with the specified color and line width values.
- [init(ink: PKInk, width: CGFloat)](./init%28ink,width%29.md)
  Create an inking tool with the specified ink and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct/init(_:color:width:)-4i3ft)*