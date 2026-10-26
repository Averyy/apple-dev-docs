# CGSetLocalEventsFilterDuringSupressionState

**Framework**: Core Graphics  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```c
#define CGSetLocalEventsFilterDuringSupressionState(filter, state)
```

## See Also

### Deprecated Functions
- [func CGPostKeyboardEvent(CGCharCode, CGKeyCode, boolean_t) -> CGError](./cgpostkeyboardevent%28_,_,_%29.md)
  Synthesizes a low-level keyboard event on the local machine.
- [CGPostMouseEvent](./cgpostmouseevent.md)
  Synthesizes a low-level mouse-button event on the local machine.
- [CGPostScrollWheelEvent](./cgpostscrollwheelevent.md)
  Synthesizes a low-level scrolling event on the local machine.
- [func CGEnableEventStateCombining(boolean_t) -> CGError](./cgenableeventstatecombining%28_%29.md)
  Enables or disables the merging of actual key and mouse state with the application-specified state in a synthetic event.
- [func CGInhibitLocalEvents(boolean_t) -> CGError](./cginhibitlocalevents%28_%29.md)
  Turns off local hardware events in the current session.
- [func CGSetLocalEventsFilterDuringSuppressionState(CGEventFilterMask, CGEventSuppressionState) -> CGError](./cgsetlocaleventsfilterduringsuppressionstate%28_,_%29.md)
  Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted.
- [func CGSetLocalEventsSuppressionInterval(CFTimeInterval) -> CGError](./cgsetlocaleventssuppressioninterval%28_%29.md)
  Sets the time interval in seconds that local hardware events are suppressed after posting a synthetic event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgsetlocaleventsfilterduringsupressionstate)*