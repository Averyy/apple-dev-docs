# PKToolPicker.Delegate

**Framework**: PencilKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
protocol Delegate : NSObjectProtocol
```

```objc
@protocol PKToolPickerDelegate <NSObject>
```

## Topics

### Instance Methods
- [func toolPickerWillDismiss(PKToolPicker) -> Bool](./delegate-swift.protocol/toolpickerwilldismiss%28_%29.md)
  This is called when the user dismisses the tool picker using a built-in control. This is **not** called when the tool picker hides from a responder change or other programatic request. By default, using the dismissal control on the tool picker causes the tool picker to resign the first responder. The delegate may override that default behavior, taking responsibility for the dismissal of the picker, by returning true from this method.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Tools
- [Configuring the PencilKit tool picker](../configuring-the-pencilkit-tool-picker.md)
  Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.
- [PKToolPicker](../pktoolpicker.md)
  A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.
- [PKInkingTool](../pkinkingtoolreference.md)
  An object that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.
- [PKEraserTool](../pkerasertoolreference.md)
  A tool for erasing previously drawn content in a canvas view.
- [PKLassoTool](../pklassotoolreference.md)
  A tool for selecting stroked lines and shapes in a canvas view.
- [PKTool](../pktool-c.class.md)
  An abstract base class for tools used by a canvas view.
- [PKResponderState](../pkresponderstate.md)
  An object that controls PencilKit behavior associated with a responder.
- [PKToolPickerVisibility](../pktoolpickervisibility.md)
  Constants that describe the visibility state of a tool picker.
- [PKToolPickerCustomItemControlOptions](../pktoolpickercustomitem/controloptions.md)
  Options for which controls to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/delegate-swift.protocol)*