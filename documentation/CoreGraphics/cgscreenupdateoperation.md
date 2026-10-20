# CGScreenUpdateOperation

**Framework**: Core Graphics  
**Kind**: struct  
**Role**: Structure

Types of screen-update operations.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct CGScreenUpdateOperation
```

```c
enum CGScreenUpdateOperation : uint32_t;
```

#### Overview

For information about how these constants are used, see the function [`CGWaitForScreenUpdateRects(_:_:_:_:_:)`](./cgwaitforscreenupdaterects%28_,_,_,_,_%29.md).

## Topics

### Constants
- [static var refresh: CGScreenUpdateOperation](./cgscreenupdateoperation/refresh.md)
  A screen-refresh operation.
- [static var move: CGScreenUpdateOperation](./cgscreenupdateoperation/move.md)
  A screen-move operation.
- [static var reducedDirtyRectangleCount: CGScreenUpdateOperation](./cgscreenupdateoperation/reduceddirtyrectanglecount.md)
### Initializers
- [init(rawValue: UInt32)](./cgscreenupdateoperation/init%28rawvalue%29.md)

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
- [struct CGEventFilterMask](./cgeventfiltermask.md)
  Specify masks for classes of low-level events that can be filtered during event suppression states.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgscreenupdateoperation)*