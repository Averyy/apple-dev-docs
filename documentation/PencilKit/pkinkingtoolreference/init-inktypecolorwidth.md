# init(inkType:color:width:)

**Framework**: PencilKit  
**Kind**: init

Creates an ink tool object with the specified color and line width values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(inkType type: __PKInkType, color: NSColor, width: CGFloat)
```

#### Return Value

A new inking tool with the specified type, color, and width.

## Parameters

- `type`: The shape of the tool. You may specify  ,  , or  .
- `color`: The color to apply to drawn lines.
- `width`: The base width to apply to any drawn lines. The value in the   parameter and input from Apple Pencil affects the final actual width.

## See Also

- [convenience init(inkType: __PKInkType, color: UIColor)](pkinkingtoolreference/init(inktype:color:).md)
  Creates an ink tool object with the default line width and the specified color.
- [convenience init(ink: PKInk, width: CGFloat)](pkinkingtoolreference/init(ink:width:).md)
  Create an inking tool with the specified ink and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/init(inktype:color:width:))*