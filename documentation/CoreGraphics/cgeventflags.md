# CGEventFlags

**Framework**: Core Graphics  
**Kind**: struct

Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct CGEventFlags
```

#### Overview

These constants specify masks for the bits in an event flags bit mask. Event flags indicate the modifier key state at the time an event is created, as well as other event-related states. Event flags are used in accessor functions such as [`flags`](cgevent/flags.md), [`CGEventSetFlags`](cgeventsetflags.md), and [`flagsState(_:)`](cgeventsource/flagsstate(_:).md).

## Topics

### Constants
- [static var maskAlphaShift: CGEventFlags](cgeventflags/maskalphashift.md)
  Indicates that the Caps Lock key is down for a keyboard, mouse, or flag-changed event.
- [static var maskShift: CGEventFlags](cgeventflags/maskshift.md)
  Indicates that the Shift key is down for a keyboard, mouse, or flag-changed event.
- [static var maskControl: CGEventFlags](cgeventflags/maskcontrol.md)
  Indicates that the Control key is down for a keyboard, mouse, or flag-changed event.
- [static var maskAlternate: CGEventFlags](cgeventflags/maskalternate.md)
  Indicates that the Alt or Option key is down for a keyboard, mouse, or flag-changed event.
- [static var maskCommand: CGEventFlags](cgeventflags/maskcommand.md)
  Indicates that the Command key is down for a keyboard, mouse, or flag-changed event.
- [static var maskHelp: CGEventFlags](cgeventflags/maskhelp.md)
  Indicates that the Help modifier key is down for a keyboard, mouse, or flag-changed event. This key is not present on most keyboards, and is different than the Help key found in the same row as Home and Page Up.
- [static var maskSecondaryFn: CGEventFlags](cgeventflags/masksecondaryfn.md)
  Indicates that the Fn (Function) key is down for a keyboard, mouse, or flag-changed event. This key is found primarily on laptop keyboards.
- [static var maskNumericPad: CGEventFlags](cgeventflags/masknumericpad.md)
  Identifies key events from the numeric keypad area on extended keyboards.
- [static var maskNonCoalesced: CGEventFlags](cgeventflags/masknoncoalesced.md)
  Indicates that mouse and pen movement events are not being coalesced.
### Initializers
- [init(rawValue: UInt64)](cgeventflags/init(rawvalue:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventflags)*