# CGDisplayStreamUpdateRectType

**Framework**: Core Graphics  
**Kind**: enum

Use these constants to determine which rectangles your app is interested in.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum CGDisplayStreamUpdateRectType
```

## Topics

### Constants
- [CGDisplayStreamUpdateRectType.refreshedRects](cgdisplaystreamupdaterecttype/refreshedrects.md)
  The rectangles for the portions of the display that were redrawn.
- [CGDisplayStreamUpdateRectType.movedRects](cgdisplaystreamupdaterecttype/movedrects.md)
  The rectangles for the portions of the display that were simply moved from one part of the display to another.
- [CGDisplayStreamUpdateRectType.dirtyRects](cgdisplaystreamupdaterecttype/dirtyrects.md)
  The union of both rectangles that were redrawn and rectangles that were moved.
- [CGDisplayStreamUpdateRectType.reducedDirtyRects](cgdisplaystreamupdaterecttype/reduceddirtyrects.md)
  The union is calculated and then simplified. This reduces the number of rectangles returned to your app, but it may report some pixels that were not actually changed.
### Initializers
- [init?(rawValue: Int32)](cgdisplaystreamupdaterecttype/init(rawvalue:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype)*