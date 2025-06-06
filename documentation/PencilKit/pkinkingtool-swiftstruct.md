# PKInkingTool

**Framework**: PencilKit  
**Kind**: struct

A structure that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct PKInkingTool
```

## Mentions

- [Supporting backward compatibility for ink types](supporting-backward-compatibility-for-ink-types.md)

#### Overview

A [`PKInkingTool`](pkinkingtool-swift.struct.md) object supports the creation of new content on a [`PKCanvasView`](pkcanvasview.md). With an inking tool, the canvas turns touch input from the user into a continuously rendered stroke. The value in the [`width`](pkinkingtool-swift.struct/width.md) property determines the base width of that stroke; however, that base value also depends on input from Apple Pencil, including force, azimuth, and angle data.

Create an inking tool programmatically, or display a [`PKToolPicker`](pktoolpicker.md) object and from which a user can select a tool. Assign the resulting object to the [`tool`](pkcanvasview/tool-6str6.md) property of your [`PKCanvasView`](pkcanvasview.md) object. The canvas uses any subsequent touch sequences to draw new content on the canvas. Assigning a new inking tool doesn’t change the characteristics for any previously drawn strokes.

## Topics

### Creating an inking tool
- [init(PKInkingTool.InkType, color: UIColor, width: CGFloat?)](pkinkingtool-swift.struct/init(_:color:width:)-2l7v.md)
  Creates an ink tool object with the specified color and line width values.
- [init(PKInkingTool.InkType, color: NSColor, width: CGFloat?)](pkinkingtool-swift.struct/init(_:color:width:)-4i3ft.md)
  Creates an ink tool object with the specified color and line width values.
- [init(ink: PKInk, width: CGFloat)](pkinkingtool-swift.struct/init(ink:width:).md)
  Create an inking tool with the specified ink and width.
### Getting the width information
- [var defaultWidth: CGFloat](pkinkingtool-swift.struct/inktype-swift.enum/defaultwidth.md)
  The default line width for the specified tool type.
- [var validWidthRange: ClosedRange<CGFloat>](pkinkingtool-swift.struct/inktype-swift.enum/validwidthrange.md)
  The range of widths allowed for an ink of this type.
### Getting the inking tool attributes
- [var color: UIColor](pkinkingtool-swift.struct/color-5xmlo.md)
  The color of the ink.
- [var color: NSColor](pkinkingtool-swift.struct/color-22zaw.md)
  The color of the ink.
- [var width: CGFloat](pkinkingtool-swift.struct/width.md)
  The width of the ink.
- [var ink: PKInk](pkinkingtool-swift.struct/ink.md)
  The ink used by this inking tool.
### Getting the tool type
- [var inkType: PKInkingTool.InkType](pkinkingtool-swift.struct/inktype-swift.property.md)
  The tool type that determines the shape of the rendered content.
- [PKInkingTool.InkType](pkinkingtool-swift.struct/inktype-swift.enum.md)
  The type that defines the shape of stroked lines.
### Working with colors
- [static func convertColor(UIColor, from: UIUserInterfaceStyle, to: UIUserInterfaceStyle) -> UIColor](pkinkingtool-swift.struct/convertcolor(_:from:to:).md)
  Convert a color from one user interface style to another.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](pkinkingtool-swift.struct/requiredcontentversion.md)
  The version of PencilKit necessary to use the inking tool.
### Using reference types
- [class PKInkingToolReference](pkinkingtoolreference.md)
  An object that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [PKTool](pktool-swift.protocol.md)

## See Also

- [Configuring the PencilKit tool picker](configuring-the-pencilkit-tool-picker.md)
  Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.
- [class PKToolPicker](pktoolpicker.md)
  A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.
- [struct PKEraserTool](pkerasertool-swift.struct.md)
  A tool for erasing previously drawn content in a canvas view.
- [struct PKLassoTool](pklassotool-swift.struct.md)
  A tool for selecting stroked lines and shapes in a canvas view.
- [protocol PKTool](pktool-swift.protocol.md)
  An interface adopted by drawing and writing tools used by a canvas view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct)*