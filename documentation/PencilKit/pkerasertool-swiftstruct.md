# PKEraserTool

**Framework**: PencilKit  
**Kind**: struct

A tool for erasing previously drawn content in a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct PKEraserTool
```

#### Overview

A [`PKEraserTool`](pkerasertool-swift.struct.md) object supports the deletion of content from a [`PKCanvasView`](pkcanvasview.md) object. The eraser tool’s type determines whether the canvas removes entire items or just the portion of an item that it touches.

Create an eraser tool programmatically or display a [`PKToolPicker`](pktoolpicker.md) object and let the user select the eraser. Assign the resulting object to the [`tool`](pkcanvasview/tool-6str6.md) property of your [`PKCanvasView`](pkcanvasview.md) object. The canvas uses any subsequent touch sequences to erase content on the canvas.

## Topics

### Creating an eraser tool
- [init(PKEraserTool.EraserType)](pkerasertool-swift.struct/init(_:).md)
  Creates an eraser tool object that removes objects wholly or partially from a canvas view.
- [init(PKEraserTool.EraserType, width: CGFloat)](pkerasertool-swift.struct/init(_:width:).md)
  Creates an eraser tool object with the specified width.
### Getting the eraser type
- [var eraserType: PKEraserTool.EraserType](pkerasertool-swift.struct/erasertype-swift.property.md)
  The behavior adopted by the eraser when deleting content.
- [PKEraserTool.EraserType](pkerasertool-swift.struct/erasertype-swift.enum.md)
  Constants that indicate the behavior of the eraser.
### Specifying the width
- [var width: CGFloat](pkerasertool-swift.struct/width.md)
  The width of the eraser.
### Using reference types
- [class PKEraserToolReference](pkerasertoolreference.md)
  A tool for erasing previously drawn content in a canvas view.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [PKTool](pktool-swift.protocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Configuring the PencilKit tool picker](configuring-the-pencilkit-tool-picker.md)
  Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.
- [class PKToolPicker](pktoolpicker.md)
  A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.
- [struct PKInkingTool](pkinkingtool-swift.struct.md)
  A structure that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.
- [struct PKLassoTool](pklassotool-swift.struct.md)
  A tool for selecting stroked lines and shapes in a canvas view.
- [protocol PKTool](pktool-swift.protocol.md)
  An interface adopted by drawing and writing tools used by a canvas view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkerasertool-swift.struct)*