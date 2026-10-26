# PKLassoToolReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

A tool for selecting stroked lines and shapes in a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class PKLassoToolReference
```

```objc
@interface PKLassoTool : PKTool
```

#### Overview

A [`PKLassoToolReference`](./pklassotoolreference.md) object supports the selection of content on a [`PKCanvasView`](./pkcanvasview.md). When active, the canvas uses incoming touch events to determine what content to add to the selection.

Create a lasso tool programmatically or display a [`PKToolPicker`](./pktoolpicker.md) object from which the user selects the tool. Assign the resulting object to the [`tool`](./pkcanvasview/tool-6str6.md) property of your [`PKCanvasView`](./pkcanvasview.md) object. The canvas uses any subsequent touch sequences to select content on the canvas.

## Topics

### Creating a lasso tool
- [init()](./pklassotoolreference/init%28%29.md)
  Creates a lasso tool object for selecting content on a canvas view.

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
- [PKEraserTool](./pkerasertoolreference.md)
  A tool for erasing previously drawn content in a canvas view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pklassotoolreference)*