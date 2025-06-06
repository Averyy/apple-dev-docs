# CGEventType

**Framework**: Core Graphics  
**Kind**: enum

Constants that specify the different types of input events.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum CGEventType
```

#### Overview

These constants are used:

- In the functions [`tapCreate(tap:place:options:eventsOfInterest:callback:userInfo:)`](cgevent/tapcreate(tap:place:options:eventsofinterest:callback:userinfo:).md) and [`tapCreateForPSN(processSerialNumber:place:options:eventsOfInterest:callback:userInfo:)`](cgevent/tapcreateforpsn(processserialnumber:place:options:eventsofinterest:callback:userinfo:).md) to specify the events of interest for the new event tap.
- To indicate the event type passed to your event tap callback function.
- In the function [`init(mouseEventSource:mouseType:mouseCursorPosition:mouseButton:)`](cgevent/init(mouseeventsource:mousetype:mousecursorposition:mousebutton:).md) to specify the type of mouse event.
- In the functions [`type`](cgevent/type.md) and [`CGEventSetType`](cgeventsettype.md) to identify the event type.
- In the functions [`counterForEventType(_:eventType:)`](cgeventsource/counterforeventtype(_:eventtype:).md) and [`secondsSinceLastEventType(_:eventType:)`](cgeventsource/secondssincelasteventtype(_:eventtype:).md) to indicate the event type.

Note that tablet devices may generate mouse events with embedded tablet data, or tablet pointer and proximity events. Tablet mouse events allow tablets to be used with applications that are not tablet-aware.

## Topics

### Constants
- [CGEventType.null](cgeventtype/null.md)
  Specifies a null event.
- [CGEventType.leftMouseDown](cgeventtype/leftmousedown.md)
  Specifies a mouse down event with the left button.
- [CGEventType.leftMouseUp](cgeventtype/leftmouseup.md)
  Specifies a mouse up event with the left button.
- [CGEventType.rightMouseDown](cgeventtype/rightmousedown.md)
  Specifies a mouse down event with the right button.
- [CGEventType.rightMouseUp](cgeventtype/rightmouseup.md)
  Specifies a mouse up event with the right button.
- [CGEventType.mouseMoved](cgeventtype/mousemoved.md)
  Specifies a mouse moved event.
- [CGEventType.leftMouseDragged](cgeventtype/leftmousedragged.md)
  Specifies a mouse drag event with the left button down.
- [CGEventType.rightMouseDragged](cgeventtype/rightmousedragged.md)
  Specifies a mouse drag event with the right button down.
- [CGEventType.keyDown](cgeventtype/keydown.md)
  Specifies a key down event.
- [CGEventType.keyUp](cgeventtype/keyup.md)
  Specifies a key up event.
- [CGEventType.flagsChanged](cgeventtype/flagschanged.md)
  Specifies a key changed event for a modifier or status key.
- [CGEventType.scrollWheel](cgeventtype/scrollwheel.md)
  Specifies a scroll wheel moved event.
- [CGEventType.tabletPointer](cgeventtype/tabletpointer.md)
  Specifies a tablet pointer event.
- [CGEventType.tabletProximity](cgeventtype/tabletproximity.md)
  Specifies a tablet proximity event.
- [CGEventType.otherMouseDown](cgeventtype/othermousedown.md)
  Specifies a mouse down event with one of buttons 2-31.
- [CGEventType.otherMouseUp](cgeventtype/othermouseup.md)
  Specifies a mouse up event with one of buttons 2-31.
- [CGEventType.otherMouseDragged](cgeventtype/othermousedragged.md)
  Specifies a mouse drag event with one of buttons 2-31 down.
- [CGEventType.tapDisabledByTimeout](cgeventtype/tapdisabledbytimeout.md)
  Specifies an event indicating the event tap is disabled because of timeout.
- [CGEventType.tapDisabledByUserInput](cgeventtype/tapdisabledbyuserinput.md)
  Specifies an event indicating the event tap is disabled because of user input.
### Initializers
- [init?(rawValue: UInt32)](cgeventtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventtype)*