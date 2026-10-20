# CGEventFilterMask

**Framework**: Core Graphics  
**Kind**: struct  
**Role**: Structure

Specify masks for classes of low-level events that can be filtered during event suppression states.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct CGEventFilterMask
```

```c
enum CGEventFilterMask : uint32_t;
```

## Topics

### Initializers
- [init(rawValue: UInt32)](./cgeventfiltermask/init%28rawvalue%29.md)
### Type Properties
- [static var permitLocalKeyboardEvents: CGEventFilterMask](./cgeventfiltermask/permitlocalkeyboardevents.md)
- [static var permitLocalMouseEvents: CGEventFilterMask](./cgeventfiltermask/permitlocalmouseevents.md)
- [static var permitSystemDefinedEvents: CGEventFilterMask](./cgeventfiltermask/permitsystemdefinedevents.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Enumerations
- [struct CGCaptureOptions](./cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [enum CGColorConversionInfoTransformType](./cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
- [enum CGColorRenderingIntent](./cgcolorrenderingintent.md)
  Handling options for colors that are not located within the destination color space of a graphics context.
- [struct CGConfigureOption](./cgconfigureoption.md)
  The scope of the changes in a display configuration transaction.
- [struct CGDisplayChangeSummaryFlags](./cgdisplaychangesummaryflags.md)
  The configuration parameters that are passed to a display reconfiguration callback function.
- [enum CGDisplayStreamFrameStatus](./cgdisplaystreamframestatus.md)
  Describes a frame update event.
- [enum CGDisplayStreamUpdateRectType](./cgdisplaystreamupdaterecttype.md)
  Use these constants to determine which rectangles your app is interested in.
- [enum CGError](./cgerror.md)
  A uniform type for result codes returned by functions in Core Graphics.
- [enum CGEventField](./cgeventfield.md)
  Constants used as keys to access specialized fields in low-level events.
- [struct CGEventFlags](./cgeventflags.md)
  Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [enum CGEventMouseSubtype](./cgeventmousesubtype.md)
  Constants used with the [`CGEventField.mouseEventSubtype`](./cgeventfield/mouseeventsubtype.md) event field.
- [enum CGEventSourceStateID](./cgeventsourcestateid.md)
  Constants that specify the possible source states of an event source.
- [enum CGEventSuppressionState](./cgeventsuppressionstate.md)
  Specify the event suppression states that can occur after posting an event.
- [enum CGEventTapLocation](./cgeventtaplocation.md)
  Constants that specify possible tapping points for events.
- [enum CGEventTapOptions](./cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventfiltermask)*