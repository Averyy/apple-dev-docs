# CGMouseButton

**Framework**: Core Graphics  
**Kind**: enum

Constants that specify buttons on a one, two, or three-button mouse.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum CGMouseButton
```

#### Overview

Quartz supports up to 32 mouse buttons. The first three buttons are specified using these three constants. Additional buttons are specified in USB order using the integers 3 to 31.

These constants are used:

- In the function [`init(mouseEventSource:mouseType:mouseCursorPosition:mouseButton:)`](cgevent/init(mouseeventsource:mousetype:mousecursorposition:mousebutton:).md) to specify the button that’s changing state.
- In the function [`buttonState(_:button:)`](cgeventsource/buttonstate(_:button:).md) to specify the button that’s being tested.
- To specify the value of the `kCGMouseEventButtonNumber` event field when modifying an event.

## Topics

### Constants
- [CGMouseButton.left](cgmousebutton/left.md)
- [CGMouseButton.right](cgmousebutton/right.md)
- [CGMouseButton.center](cgmousebutton/center.md)
### Initializers
- [init?(rawValue: UInt32)](cgmousebutton/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CGCaptureOptions](cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [enum CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
- [enum CGColorRenderingIntent](cgcolorrenderingintent.md)
  Handling options for colors that are not located within the destination color space of a graphics context.
- [struct CGConfigureOption](cgconfigureoption.md)
  The scope of the changes in a display configuration transaction.
- [struct CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md)
  The configuration parameters that are passed to a display reconfiguration callback function.
- [enum CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md)
  Describes a frame update event.
- [enum CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md)
  Use these constants to determine which rectangles your app is interested in.
- [enum CGError](cgerror.md)
  A uniform type for result codes returned by functions in Core Graphics.
- [enum CGEventField](cgeventfield.md)
  Constants used as keys to access specialized fields in low-level events.
- [struct CGEventFilterMask](cgeventfiltermask.md)
  Specify masks for classes of low-level events that can be filtered during event suppression states.
- [struct CGEventFlags](cgeventflags.md)
  Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [enum CGEventMouseSubtype](cgeventmousesubtype.md)
  Constants used with the [`CGEventField.mouseEventSubtype`](cgeventfield/mouseeventsubtype.md) event field.
- [enum CGEventSourceStateID](cgeventsourcestateid.md)
  Constants that specify the possible source states of an event source.
- [enum CGEventSuppressionState](cgeventsuppressionstate.md)
  Specify the event suppression states that can occur after posting an event.
- [enum CGEventTapLocation](cgeventtaplocation.md)
  Constants that specify possible tapping points for events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgmousebutton)*