# CGError

**Framework**: Core Graphics  
**Kind**: enum

A uniform type for result codes returned by functions in Core Graphics.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CGError
```

## Topics

### Constants
- [CGError.cannotComplete](cgerror/cannotcomplete.md)
  The requested operation is inappropriate for the parameters passed in, or the current system state.
- [CGError.failure](cgerror/failure.md)
  A general failure occurred.
- [CGError.illegalArgument](cgerror/illegalargument.md)
  One or more of the parameters passed to a function are invalid. Check for `NULL` pointers.
- [CGError.invalidConnection](cgerror/invalidconnection.md)
  The parameter representing a connection to the window server is invalid.
- [CGError.invalidContext](cgerror/invalidcontext.md)
  The `CPSProcessSerNum` or context identifier parameter is not valid.
- [CGError.invalidOperation](cgerror/invalidoperation.md)
  The requested operation is not valid for the parameters passed in, or the current system state.
- [CGError.noneAvailable](cgerror/noneavailable.md)
  The requested operation could not be completed as the indicated resources were not found.
- [CGError.notImplemented](cgerror/notimplemented.md)
  Return value from obsolete function stubs present for binary compatibility, but not typically called.
- [CGError.rangeCheck](cgerror/rangecheck.md)
  A parameter passed in has a value that is inappropriate, or which does not map to a useful operation or value.
- [CGError.success](cgerror/success.md)
  The requested operation was completed successfully.
- [CGError.typeCheck](cgerror/typecheck.md)
  A data type or token was encountered that did not match the expected type or token.
### Initializers
- [init?(rawValue: Int32)](cgerror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgerror)*