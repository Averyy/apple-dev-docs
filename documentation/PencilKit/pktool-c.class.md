# PKTool

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

An abstract base class for tools used by a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```objc
@interface PKTool : NSObject
```

## Overview

A [`PKTool`](./pktool-c.class.md) object is an abstract base class for tool types associated with a [`PKCanvasView`](./pkcanvasview.md). Tools are user-facing, and the selected tool determines how the canvas interprets incoming gestures.

Don’t create [`PKTool`](./pktool-c.class.md) objects directly. Instead, create one of its subclasses to provide users with the desired the tool behavior.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [PKEraserToolReference](./pkerasertoolreference.md)
- [PKInkingToolReference](./pkinkingtoolreference.md)
- [PKLassoToolReference](./pklassotoolreference.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Tools
- [Configuring the PencilKit tool picker](./configuring-the-pencilkit-tool-picker.md)
  Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.
- [class PKToolPicker](./pktoolpicker.md)
  A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.
- [class PKInkingToolReference](./pkinkingtoolreference.md)
  An object that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.
- [class PKEraserToolReference](./pkerasertoolreference.md)
  A tool for erasing previously drawn content in a canvas view.
- [class PKLassoToolReference](./pklassotoolreference.md)
  A tool for selecting stroked lines and shapes in a canvas view.
- [class PKResponderState](./pkresponderstate.md)
  An object that controls PencilKit behavior associated with a responder.
- [enum PKToolPickerVisibility](./pktoolpickervisibility.md)
  Constants that describe the visibility state of a tool picker.
- [PKToolPicker.Delegate](./pktoolpicker/delegate-swift.protocol.md)
- [PKToolPickerCustomItem.ControlOptions](./pktoolpickercustomitem/controloptions.md)
  Options for which controls to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktool-c.class)*