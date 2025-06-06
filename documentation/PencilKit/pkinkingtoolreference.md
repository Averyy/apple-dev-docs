# PKInkingToolReference

**Framework**: PencilKit  
**Kind**: class

An object that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class PKInkingToolReference
```

#### Overview

A [`PKInkingTool`](pkinkingtool-swift.struct.md) object supports the creation of new content on a [`PKCanvasView`](pkcanvasview.md). With an inking tool, the canvas turns touch input from the user into a continuously rendered stroke. The value in the [`width`](pkinkingtoolreference/width.md) property determines the base width of that stroke; however, that base value also depends on input from Apple Pencil, including force, azimuth, and angle data.

Create an inking tool programmatically, or display a [`PKToolPicker`](pktoolpicker.md) object and from which a user can select a tool. Assign the resulting object to the [`tool`](pkcanvasview/tool-6str6.md) property of your [`PKCanvasView`](pkcanvasview.md) object. The canvas uses any subsequent touch sequences to draw new content on the canvas. Assigning a new inking tool doesn’t change the characteristics for any previously drawn strokes.

## Topics

### Creating an inking tool
- [init(inkType: __PKInkType, color: UIColor, width: CGFloat)](pkinkingtoolreference/init(inktype:color:width:).md)
  Creates an ink tool object with the specified color and line width values.
- [convenience init(inkType: __PKInkType, color: UIColor)](pkinkingtoolreference/init(inktype:color:).md)
  Creates an ink tool object with the default line width and the specified color.
- [convenience init(ink: PKInk, width: CGFloat)](pkinkingtoolreference/init(ink:width:).md)
  Create an inking tool with the specified ink and width.
### Getting the inking tool attributes
- [var color: UIColor](pkinkingtoolreference/color.md)
  The color of the ink.
- [var width: CGFloat](pkinkingtoolreference/width.md)
  The base line width for new content.
- [var ink: PKInk](pkinkingtoolreference/ink.md)
  The ink that this tool creates strokes with.
### Getting the tool type
- [var inkType: __PKInkType](pkinkingtoolreference/inktype.md)
  The tool type that determines the shape of the rendered content.
### Working with colors
- [class func convert(UIColor, from: UIUserInterfaceStyle, to: UIUserInterfaceStyle) -> UIColor](pkinkingtoolreference/convert(_:from:to:).md)
  Converts a color from one user interface style to another.
### Getting the standard ink widths
- [class func defaultWidth(forInkType: __PKInkType) -> CGFloat](pkinkingtoolreference/defaultwidth(forinktype:).md)
  Returns the default line width for the specified tool type.
- [class func minimumWidth(forInkType: __PKInkType) -> CGFloat](pkinkingtoolreference/minimumwidth(forinktype:).md)
  Returns the minimum allowed line width for the specified tool type.
- [class func maximumWidth(forInkType: __PKInkType) -> CGFloat](pkinkingtoolreference/maximumwidth(forinktype:).md)
  Returns the maximum allowed line width for the specified tool type.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](pkinkingtoolreference/requiredcontentversion.md)
  The version of PencilKit necessary to use the inking tool.

## Relationships

### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference)*