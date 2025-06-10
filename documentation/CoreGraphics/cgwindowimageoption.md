# CGWindowImageOption

**Framework**: Core Graphics  
**Kind**: struct

The data type to use to specify the type of image to be generated for a window.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct CGWindowImageOption
```

#### Overview

This type is used in conjunction with the constants described in [`Window Image Types`](window-image-types.md).

## Topics

### Initializers
- [init(rawValue: UInt32)](cgwindowimageoption/init(rawvalue:).md)
### Type Properties
- [static var bestResolution: CGWindowImageOption](cgwindowimageoption/bestresolution.md)
  When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [static var boundsIgnoreFraming: CGWindowImageOption](cgwindowimageoption/boundsignoreframing.md)
- [static var nominalResolution: CGWindowImageOption](cgwindowimageoption/nominalresolution.md)
  When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [static var onlyShadows: CGWindowImageOption](cgwindowimageoption/onlyshadows.md)
- [static var shouldBeOpaque: CGWindowImageOption](cgwindowimageoption/shouldbeopaque.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption)*