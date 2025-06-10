# CGEventTapLocation

**Framework**: Core Graphics  
**Kind**: enum

Constants that specify possible tapping points for events.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum CGEventTapLocation
```

#### Overview

In addition to the three tapping points described above, an event tap may also be placed where annotated events are delivered to a specific application. For more information, see the function [`tapCreateForPSN(processSerialNumber:place:options:eventsOfInterest:callback:userInfo:)`](cgevent/tapcreateforpsn(processserialnumber:place:options:eventsofinterest:callback:userinfo:).md).

## Topics

### Constants
- [CGEventTapLocation.cghidEventTap](cgeventtaplocation/cghideventtap.md)
  Specifies that an event tap is placed at the point where HID system events enter the window server.
- [CGEventTapLocation.cgSessionEventTap](cgeventtaplocation/cgsessioneventtap.md)
  Specifies that an event tap is placed at the point where HID system and remote control events enter a login session.
- [CGEventTapLocation.cgAnnotatedSessionEventTap](cgeventtaplocation/cgannotatedsessioneventtap.md)
  Specifies that an event tap is placed at the point where session events have been annotated to flow to an application.
### Initializers
- [init?(rawValue: UInt32)](cgeventtaplocation/init(rawvalue:).md)

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
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventtaplocation)*