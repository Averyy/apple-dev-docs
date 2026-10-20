# PKInkingToolReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface PKInkingTool : PKTool
```

#### Overview

A [`PKInkingTool`](./pkinkingtool-swift.struct.md) object supports the creation of new content on a [`PKCanvasView`](./pkcanvasview.md). With an inking tool, the canvas turns touch input from the user into a continuously rendered stroke. The value in the [`width`](./pkinkingtoolreference/width.md) property determines the base width of that stroke; however, that base value also depends on input from Apple Pencil, including force, azimuth, and angle data.

Create an inking tool programmatically, or display a [`PKToolPicker`](./pktoolpicker.md) object and from which a user can select a tool. Assign the resulting object to the [`tool`](./pkcanvasview/tool-6str6.md) property of your [`PKCanvasView`](./pkcanvasview.md) object. The canvas uses any subsequent touch sequences to draw new content on the canvas. Assigning a new inking tool doesn’t change the characteristics for any previously drawn strokes.

## Topics

### Creating an inking tool
- [init(inkType: __PKInkType, color: UIColor, width: CGFloat)](./pkinkingtoolreference/init%28inktype,color,width%29.md)
  Creates an ink tool object with the specified color and line width values.
- [convenience init(inkType: __PKInkType, color: UIColor)](./pkinkingtoolreference/init%28inktype,color%29.md)
  Creates an ink tool object with the default line width and the specified color.
- [convenience init(ink: PKInk, width: CGFloat)](./pkinkingtoolreference/init%28ink,width%29.md)
  Create an inking tool with the specified ink and width.
### Getting the inking tool attributes
- [var color: UIColor](./pkinkingtoolreference/color.md)
  The color of the ink.
- [var width: CGFloat](./pkinkingtoolreference/width.md)
  The base line width for new content.
- [var ink: PKInk](./pkinkingtoolreference/ink.md)
  The ink that this tool creates strokes with.
### Getting the tool type
- [var inkType: __PKInkType](./pkinkingtoolreference/inktype.md)
  The tool type that determines the shape of the rendered content.
### Working with colors
- [class func convert(UIColor, from: UIUserInterfaceStyle, to: UIUserInterfaceStyle) -> UIColor](./pkinkingtoolreference/convert%28_,from,to%29.md)
  Converts a color from one user interface style to another.
### Getting the standard ink widths
- [class func defaultWidth(forInkType: __PKInkType) -> CGFloat](./pkinkingtoolreference/defaultwidth%28forinktype%29.md)
  Returns the default line width for the specified tool type.
- [class func minimumWidth(forInkType: __PKInkType) -> CGFloat](./pkinkingtoolreference/minimumwidth%28forinktype%29.md)
  Returns the minimum allowed line width for the specified tool type.
- [class func maximumWidth(forInkType: __PKInkType) -> CGFloat](./pkinkingtoolreference/maximumwidth%28forinktype%29.md)
  Returns the maximum allowed line width for the specified tool type.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](./pkinkingtoolreference/requiredcontentversion.md)
  The version of PencilKit necessary to use the inking tool.
### Initializers
- [init(inkType: __PKInkType, color: UIColor, width: CGFloat, azimuth: CGFloat)](./pkinkingtoolreference/init%28inktype,color,width,azimuth%29.md)
### Instance Properties
- [var azimuth: CGFloat](./pkinkingtoolreference/azimuth.md)
  The base angle of the ink.
### Type Methods
- [class func invertColor(CGColor) -> Unmanaged<CGColor>](./pkinkingtoolreference/invertcolor%28_%29.md)
  Converts a color from light to dark appearance or vice versa.

## Relationships

### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtoolreference)*