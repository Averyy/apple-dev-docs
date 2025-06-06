# PKTool

**Framework**: PencilKit  
**Kind**: protocol

An interface adopted by drawing and writing tools used by a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol PKTool
```

#### Overview

Drawing and writing tools associated with a [`PKCanvasView`](pkcanvasview.md) adopt the [`PKTool`](pktool-swift.protocol.md) protocol. Tools are user-facing, and the selected tool determines how the canvas interprets incoming gestures.

Don’t adopt this protocol in your own objects. Instead, create a tool object to provide users with the desired the tool behavior.

## Relationships

### Conforming Types
- [PKEraserTool](pkerasertool-swift.struct.md)
- [PKInkingTool](pkinkingtool-swift.struct.md)
- [PKLassoTool](pklassotool-swift.struct.md)

## See Also

- [Configuring the PencilKit tool picker](configuring-the-pencilkit-tool-picker.md)
  Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.
- [class PKToolPicker](pktoolpicker.md)
  A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.
- [struct PKInkingTool](pkinkingtool-swift.struct.md)
  A structure that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.
- [struct PKEraserTool](pkerasertool-swift.struct.md)
  A tool for erasing previously drawn content in a canvas view.
- [struct PKLassoTool](pklassotool-swift.struct.md)
  A tool for selecting stroked lines and shapes in a canvas view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktool-swift.protocol)*