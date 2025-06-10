# CGCaptureOptions

**Framework**: Core Graphics  
**Kind**: struct

Configuration parameters that are used when capturing displays.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct CGCaptureOptions
```

#### Overview

For information about how these constants are used, see the functions [`CGDisplayCaptureWithOptions(_:_:)`](cgdisplaycapturewithoptions(_:_:).md) and [`CGCaptureAllDisplaysWithOptions(_:)`](cgcapturealldisplayswithoptions(_:).md).

## Topics

### Constants
- [static var noFill: CGCaptureOptions](cgcaptureoptions/nofill.md)
  Disables fill with black.
### Initializers
- [init(rawValue: UInt32)](cgcaptureoptions/init(rawvalue:).md)

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
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcaptureoptions)*