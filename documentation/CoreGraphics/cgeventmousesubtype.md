# CGEventMouseSubtype

**Framework**: Core Graphics  
**Kind**: enum

Constants used with the [`CGEventField.mouseEventSubtype`](cgeventfield/mouseeventsubtype.md) event field.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum CGEventMouseSubtype
```

#### Overview

Tablets may generate specially annotated mouse events that contain values associated with the [`CGEventField.mouseEventSubtype`](cgeventfield/mouseeventsubtype.md) event field. To learn how to set these values, see the function [`setIntegerValueField(_:value:)`](cgevent/setintegervaluefield(_:value:).md).

## Topics

### Constants
- [CGEventMouseSubtype.defaultType](cgeventmousesubtype/defaulttype.md)
  Specifies that the event is an ordinary mouse event, and does not contain additional tablet device information.
- [CGEventMouseSubtype.tabletPoint](cgeventmousesubtype/tabletpoint.md)
  Specifies that the mouse event originated from a tablet device, and that the various `kCGTabletEvent` field selectors may be used to obtain tablet-specific data from the mouse event.
- [CGEventMouseSubtype.tabletProximity](cgeventmousesubtype/tabletproximity.md)
### Initializers
- [init?(rawValue: UInt32)](cgeventmousesubtype/init(rawvalue:).md)

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
- [enum CGEventSourceStateID](cgeventsourcestateid.md)
  Constants that specify the possible source states of an event source.
- [enum CGEventSuppressionState](cgeventsuppressionstate.md)
  Specify the event suppression states that can occur after posting an event.
- [enum CGEventTapLocation](cgeventtaplocation.md)
  Constants that specify possible tapping points for events.
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventmousesubtype)*