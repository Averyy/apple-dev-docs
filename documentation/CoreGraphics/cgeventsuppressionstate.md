# CGEventSuppressionState

**Framework**: Core Graphics  
**Kind**: enum

Specify the event suppression states that can occur after posting an event.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum CGEventSuppressionState
```

#### Overview

These constants specify the types of event suppression intervals during which an event filter is applied after posting an event.

## Topics

### Constants
- [CGEventSuppressionState.eventSuppressionStateSuppressionInterval](cgeventsuppressionstate/eventsuppressionstatesuppressioninterval.md)
  Specifies that certain local hardware events may be suppressed for a short interval after posting an event.
- [CGEventSuppressionState.eventSuppressionStateRemoteMouseDrag](cgeventsuppressionstate/eventsuppressionstateremotemousedrag.md)
  Specifies that certain local hardware events may be suppressed during a mouse drag operation (mouse movement with the left or only mouse button down).
- [CGEventSuppressionState.numberOfEventSuppressionStates](cgeventsuppressionstate/numberofeventsuppressionstates.md)
### Enumeration Cases
- [CGEventSuppressionState.numberOfEventSuppressionStates](cgeventsuppressionstate/numberofeventsuppressionstates.md)
### Initializers
- [init?(rawValue: UInt32)](cgeventsuppressionstate/init(rawvalue:).md)

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
- [enum CGEventTapLocation](cgeventtaplocation.md)
  Constants that specify possible tapping points for events.
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventsuppressionstate)*