# CGDisplayChangeSummaryFlags

**Framework**: Core Graphics  
**Kind**: struct

The configuration parameters that are passed to a display reconfiguration callback function.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct CGDisplayChangeSummaryFlags
```

#### Overview

For information about how these constants are used, see the callback [`CGDisplayReconfigurationCallBack`](cgdisplayreconfigurationcallback.md).

## Topics

### Constants
- [static var beginConfigurationFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/beginconfigurationflag.md)
  The display configuration is about to change.
- [static var movedFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/movedflag.md)
  The location of the upper-left corner of the display in the global display coordinate space has changed.
- [static var setMainFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/setmainflag.md)
  The display is now the main display.
- [static var setModeFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/setmodeflag.md)
  The display mode has changed.
- [static var addFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/addflag.md)
  The display has been added to the active display list.
- [static var removeFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/removeflag.md)
  The display has been removed from the active display list.
- [static var enabledFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/enabledflag.md)
  The display has been enabled.
- [static var disabledFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/disabledflag.md)
  The display has been disabled.
- [static var mirrorFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/mirrorflag.md)
  The display is now mirroring another display.
- [static var unMirrorFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/unmirrorflag.md)
  The display is no longer mirroring another display.
- [static var desktopShapeChangedFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/desktopshapechangedflag.md)
### Initializers
- [init(rawValue: UInt32)](cgdisplaychangesummaryflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct CGCaptureOptions](cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [enum CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
- [enum CGColorRenderingIntent](cgcolorrenderingintent.md)
  Handling options for colors that are not located within the destination color space of a graphics context.
- [struct CGConfigureOption](cgconfigureoption.md)
  The scope of the changes in a display configuration transaction.
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
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags)*