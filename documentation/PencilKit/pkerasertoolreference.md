# PKEraserToolReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

A tool for erasing previously drawn content in a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class PKEraserToolReference
```

```objc
@interface PKEraserTool : PKTool
```

#### Overview

A [`PKEraserTool`](./pkerasertool-swift.struct.md) object supports the deletion of content from a [`PKCanvasView`](./pkcanvasview.md) object. The eraser tool’s type determines whether the canvas removes entire items or just the portion of an item that it touches.

Create an eraser tool programmatically or display a [`PKToolPicker`](./pktoolpicker.md) object and let the user select the eraser. Assign the resulting object to the [`tool`](./pkcanvasview/tool-6str6.md) property of your [`PKCanvasView`](./pkcanvasview.md) object. The canvas uses any subsequent touch sequences to erase content on the canvas.

## Topics

### Creating an eraser tool
- [init(eraserType: __PKEraserType)](./pkerasertoolreference/init%28erasertype%29.md)
  Creates an eraser tool object that removes objects wholly or partially from a canvas view.
- [init(eraserType: __PKEraserType, width: CGFloat)](./pkerasertoolreference/init%28erasertype,width%29.md)
### Getting the eraser type
- [var eraserType: __PKEraserType](./pkerasertoolreference/erasertype.md)
  The behavior adopted by the eraser when deleting content.
- [PKEraserType](./pkerasertype.md)
  Constants that indicate the behavior of the eraser.
### Getting the width information
- [var width: CGFloat](./pkerasertoolreference/width.md)
  The width of the eraser.
- [class func defaultWidth(for: __PKEraserType) -> CGFloat](./pkerasertoolreference/defaultwidth%28for%29.md)
  The default width for the specified eraser type.
- [class func minimumWidth(for: __PKEraserType) -> CGFloat](./pkerasertoolreference/minimumwidth%28for%29.md)
  The minimum width for the specified eraser type.
- [class func maximumWidth(for: __PKEraserType) -> CGFloat](./pkerasertoolreference/maximumwidth%28for%29.md)
  The maximum width for the specified eraser type.

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
### Inherits From
- [PKTool](./pktool-c.class.md)

## See Also

### Tools
- [Configuring the PencilKit tool picker](./configuring-the-pencilkit-tool-picker.md)
  Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.
- [PKToolPicker](./pktoolpicker.md)
  A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.
- [PKInkingTool](./pkinkingtoolreference.md)
  An object that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.
- [PKLassoTool](./pklassotoolreference.md)
  A tool for selecting stroked lines and shapes in a canvas view.
- [PKTool](./pktool-c.class.md)
  An abstract base class for tools used by a canvas view.
- [PKResponderState](./pkresponderstate.md)
  An object that controls PencilKit behavior associated with a responder.
- [PKToolPickerVisibility](./pktoolpickervisibility.md)
  Constants that describe the visibility state of a tool picker.
- [PKToolPickerDelegate](./pktoolpicker/delegate-swift.protocol.md)
- [PKToolPickerCustomItemControlOptions](./pktoolpickercustomitem/controloptions.md)
  Options for which controls to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkerasertoolreference)*