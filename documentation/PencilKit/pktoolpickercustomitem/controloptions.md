# PKToolPickerCustomItem.ControlOptions

**Framework**: PencilKit  
**Kind**: struct  
**Role**: Structure

Options for which controls to present.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct ControlOptions
```

```c
enum PKToolPickerCustomItemControlOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./controloptions/init%28rawvalue%29.md)
### Type Properties
- [static var opacity: PKToolPickerCustomItem.ControlOptions](./controloptions/opacity.md)
  Present an opacity control if color adjustment is supported.
- [static var width: PKToolPickerCustomItem.ControlOptions](./controloptions/width.md)
  Present a width control if width adjustment is supported.
### Enumeration Cases
- [PKToolPickerCustomItemControlNone](../pktoolpickercustomitemcontroloptions/pktoolpickercustomitemcontrolnone.md)
  Present neither a width nor opacity control.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

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
- [PKToolPickerDelegate](../pktoolpicker/delegate-swift.protocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickercustomitem/controloptions)*