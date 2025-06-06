# init(inkType:color:)

**Framework**: PencilKit  
**Kind**: init

Creates an ink tool object with the default line width and the specified color.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
convenience init(inkType type: __PKInkType, color: UIColor)
```

#### Return Value

A new inking tool with the specified type and color.

#### Discussion

This method sets the line width to the value returned by [`defaultWidth(forInkType:)`](pkinkingtoolreference/defaultwidth(forinktype:).md).

## Parameters

- `type`: The shape of the tool. You may specify  ,  , or  .
- `color`: The color to apply to drawn lines.

## See Also

- [init(inkType: __PKInkType, color: UIColor, width: CGFloat)](pkinkingtoolreference/init(inktype:color:width:).md)
  Creates an ink tool object with the specified color and line width values.
- [convenience init(ink: PKInk, width: CGFloat)](pkinkingtoolreference/init(ink:width:).md)
  Create an inking tool with the specified ink and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference/init(inktype:color:))*