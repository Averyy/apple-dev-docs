# init(_:color:width:)

**Framework**: PencilKit  
**Kind**: init

Creates an ink tool object with the specified color and line width values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 11.0+

## Declaration

```swift
init(_ inkType: PKInkingTool.InkType, color: NSColor = NSColor.black, width: CGFloat? = nil)
```

## Parameters

- `inkType`: The shape of the tool, which can be  ,  , or  .
- `color`: The color to apply to drawn lines.
- `width`: The base width to apply to any drawn lines. The value in the   parameter and input from Apple Pencil affects the final width.

## See Also

- [init(PKInkingTool.InkType, color: UIColor, width: CGFloat?)](pkinkingtool-swift.struct/init(_:color:width:)-2l7v.md)
  Creates an ink tool object with the specified color and line width values.
- [init(ink: PKInk, width: CGFloat)](pkinkingtool-swift.struct/init(ink:width:).md)
  Create an inking tool with the specified ink and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct/init(_:color:width:)-4i3ft)*