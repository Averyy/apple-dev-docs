# CGConfigureOption

**Framework**: Core Graphics  
**Kind**: struct

The scope of the changes in a display configuration transaction.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct CGConfigureOption
```

#### Overview

For information about how these constants are used, see the function [`CGCompleteDisplayConfiguration(_:_:)`](cgcompletedisplayconfiguration(_:_:).md).

## Topics

### Initializers
- [init(rawValue: UInt32)](cgconfigureoption/init(rawvalue:).md)
### Type Properties
- [static var forAppOnly: CGConfigureOption](cgconfigureoption/forapponly.md)
  Changes persist for the lifetime of the current application. After the application terminates, the display configuration settings revert to the current login session.
- [static var forSession: CGConfigureOption](cgconfigureoption/forsession.md)
  Changes persist for the lifetime of the current login session. After the current session terminates, the displays revert to the last saved permanent configuration.
- [static var permanently: CGConfigureOption](cgconfigureoption/permanently.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct CGCaptureOptions](cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [enum CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
- [enum CGColorRenderingIntent](cgcolorrenderingintent.md)
  Handling options for colors that are not located within the destination color space of a graphics context.
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
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgconfigureoption)*