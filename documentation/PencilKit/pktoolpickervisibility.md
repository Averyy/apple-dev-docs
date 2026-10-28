# PKToolPickerVisibility

**Framework**: PencilKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the visibility state of a tool picker.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
enum PKToolPickerVisibility
```

```c
enum PKToolPickerVisibility : NSInteger;
```

## Overview

Set the `toolPickerVisibility` property on a `PKResponderState` to control whether a tool picker is visible, offscreen but responsive, or inactive for a given responder. When set to [`PKToolPickerVisibilityInherited`](./pktoolpickervisibility/pktoolpickervisibilityinherited.md), the visibility is determined by the next responder in the chain. If no responder in the chain provides a visibility, the tool picker defaults to [`PKToolPickerVisibility.visible`](./pktoolpickervisibility/visible.md).

## Topics

### Visibility states
- [PKToolPickerVisibility.inactive](./pktoolpickervisibility/inactive.md)
  No active tool picker.
- [PKToolPickerVisibility.hidden](./pktoolpickervisibility/hidden.md)
  Tool picker is active but offscreen, and can appear temporarily in response to user actions.
- [PKToolPickerVisibility.visible](./pktoolpickervisibility/visible.md)
  Tool picker is active and onscreen.
- [PKToolPickerVisibilityInherited](./pktoolpickervisibility/pktoolpickervisibilityinherited.md)
  Inherit the tool picker visibility from the next responder.
### Initializers
- [init?(rawValue: Int)](./pktoolpickervisibility/init%28rawvalue%29.md)
### Instance Methods
- [func toggle()](./pktoolpickervisibility/toggle%28%29.md)
  Toggles between hidden / visible.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [PKLassoTool](./pklassotoolreference.md)
  A tool for selecting stroked lines and shapes in a canvas view.
- [PKTool](./pktool-c.class.md)
  An abstract base class for tools used by a canvas view.
- [PKResponderState](./pkresponderstate.md)
  An object that controls PencilKit behavior associated with a responder.
- [PKToolPickerDelegate](./pktoolpicker/delegate-swift.protocol.md)
- [PKToolPickerCustomItemControlOptions](./pktoolpickercustomitem/controloptions.md)
  Options for which controls to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickervisibility)*