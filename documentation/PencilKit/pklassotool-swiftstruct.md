# PKLassoTool

**Framework**: PencilKit  
**Kind**: struct

A tool for selecting stroked lines and shapes in a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct PKLassoTool
```

#### Overview

A [`PKLassoTool`](pklassotool-swift.struct.md) object supports the selection of content on a [`PKCanvasView`](pkcanvasview.md). When active, the canvas uses incoming touch events to determine what content to add to the selection.

Create a lasso tool programmatically or display a [`PKToolPicker`](pktoolpicker.md) object from which the user selects the tool. Assign the resulting object to the [`tool`](pkcanvasview/tool-6str6.md) property of your [`PKCanvasView`](pkcanvasview.md) object. The canvas uses any subsequent touch sequences to select content on the canvas.

## Topics

### Creating a lasso tool
- [init()](pklassotool-swift.struct/init.md)
  Creates a lasso tool for selecting content on a canvas view.
### Using reference types
- [class PKLassoToolReference](pklassotoolreference.md)
  A tool for selecting stroked lines and shapes in a canvas view.

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
- [struct PKEraserTool](pkerasertool-swift.struct.md)
  A tool for erasing previously drawn content in a canvas view.
- [protocol PKTool](pktool-swift.protocol.md)
  An interface adopted by drawing and writing tools used by a canvas view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pklassotool-swift.struct)*