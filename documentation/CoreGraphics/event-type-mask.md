# Event Type Mask

**Framework**: Core Graphics

Specifies an event mask that represents all event types.

#### Overview

This constant is typically used with the functions [`tapCreate(tap:place:options:eventsOfInterest:callback:userInfo:)`](cgevent/tapcreate(tap:place:options:eventsofinterest:callback:userinfo:).md) and [`tapCreateForPSN(processSerialNumber:place:options:eventsOfInterest:callback:userInfo:)`](cgevent/tapcreateforpsn(processserialnumber:place:options:eventsofinterest:callback:userinfo:).md) to register an event tap that observes all input events.

## See Also

- [enum CGEventField](cgeventfield.md)
  Constants used as keys to access specialized fields in low-level events.
- [struct CGEventFilterMask](cgeventfiltermask.md)
  Specify masks for classes of low-level events that can be filtered during event suppression states.
- [struct CGEventFlags](cgeventflags.md)
  Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [enum CGEventSourceStateID](cgeventsourcestateid.md)
  Constants that specify the possible source states of an event source.
- [Event Source Token](event-source-token.md)
  Specifies any input event type.
- [enum CGEventSuppressionState](cgeventsuppressionstate.md)
  Specify the event suppression states that can occur after posting an event.
- [enum CGEventTapLocation](cgeventtaplocation.md)
  Constants that specify possible tapping points for events.
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.
- [enum CGEventTapPlacement](cgeventtapplacement.md)
  Constants that specify where a new event tap is inserted into the list of active event taps.
- [enum CGEventType](cgeventtype.md)
  Constants that specify the different types of input events.
- [enum CGMouseButton](cgmousebutton.md)
  Constants that specify buttons on a one, two, or three-button mouse.
- [enum CGEventMouseSubtype](cgeventmousesubtype.md)
  Constants used with the [`CGEventField.mouseEventSubtype`](cgeventfield/mouseeventsubtype.md) event field.
- [enum CGScrollEventUnit](cgscrolleventunit.md)
  Constants that specify the unit of measurement for a scrolling event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/event-type-mask)*