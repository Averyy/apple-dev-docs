# CGSetLocalEventsFilterDuringSuppressionState(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: No longer supported

## Declaration

```swift
func CGSetLocalEventsFilterDuringSuppressionState(_ filter: CGEventFilterMask, _ state: CGEventSuppressionState) -> CGError
```

```c
extern CGError CGSetLocalEventsFilterDuringSuppressionState(CGEventFilterMask filter, CGEventSuppressionState state);
```

#### Return Value

A result code. See the result codes described in [Quartz Display Services](./quartz-display-services.md).

#### Discussion

By default, the system suppresses local hardware events from the keyboard and mouse during a short interval after a synthetic event is posted and during a synthetic mouse drag (mouse movement with the left or only mouse button down).

Some applications may want to enable events from some of the local hardware. For example, if you post mouse events only, you may wish to permit local keyboard hardware events to pass through.

This function lets you specify a state (event suppression interval or mouse drag), and a mask of event categories to be passed through. The new filter state takes effect with the next synthetic event you post.

This function is not recommended for general use because of undocumented special cases and undesirable side effects. The recommended replacement for this function is [`setLocalEventsFilterDuringSuppressionState(_:state:)`](./cgeventsource/setlocaleventsfilterduringsuppressionstate%28_,state%29.md), which allows the filter behavior to be associated only with events created from a specific event source.

## Parameters

- `filter`: The class of local hardware events to enable after a synthetic event is posted. Pass one of the constants listed in [`CGEventFilterMask`](./cgeventfiltermask.md).
- `state`: The type of interval during which the filter is applied. Pass one of the constants listed in [`CGEventSuppressionState`](./cgeventsuppressionstate.md).

## See Also

### Functions
- [func CGAcquireDisplayFadeReservation(CGDisplayReservationInterval, UnsafeMutablePointer<CGDisplayFadeReservationToken>?) -> CGError](./cgacquiredisplayfadereservation%28_,_%29.md)
  Reserves the fade hardware for a specified time interval.
- [func CGAssociateMouseAndMouseCursorPosition(boolean_t) -> CGError](./cgassociatemouseandmousecursorposition%28_%29.md)
  Connects or disconnects the mouse and cursor while an application is in the foreground.
- [func CGBeginDisplayConfiguration(UnsafeMutablePointer<CGDisplayConfigRef?>?) -> CGError](./cgbegindisplayconfiguration%28_%29.md)
  Begins a new set of display configuration changes.
- [func CGCancelDisplayConfiguration(CGDisplayConfigRef?) -> CGError](./cgcanceldisplayconfiguration%28_%29.md)
  Cancels a set of display configuration changes.
- [func CGCaptureAllDisplays() -> CGError](./cgcapturealldisplays%28%29.md)
  Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [func CGCaptureAllDisplaysWithOptions(CGCaptureOptions) -> CGError](./cgcapturealldisplayswithoptions%28_%29.md)
  Captures all attached displays, using the specified options.
- [func CGCompleteDisplayConfiguration(CGDisplayConfigRef?, CGConfigureOption) -> CGError](./cgcompletedisplayconfiguration%28_,_%29.md)
  Completes a set of display configuration changes.
- [func CGConfigureDisplayFadeEffect(CGDisplayConfigRef?, CGDisplayFadeInterval, CGDisplayFadeInterval, Float, Float, Float) -> CGError](./cgconfiguredisplayfadeeffect%28_,_,_,_,_,_%29.md)
  Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [func CGConfigureDisplayMirrorOfDisplay(CGDisplayConfigRef?, CGDirectDisplayID, CGDirectDisplayID) -> CGError](./cgconfiguredisplaymirrorofdisplay%28_,_,_%29.md)
  Changes the configuration of a mirroring set.
- [func CGConfigureDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CFDictionary?) -> CGError](./cgconfiguredisplaymode%28_,_,_%29.md)
  Configures the display mode of a display.
- [func CGConfigureDisplayOrigin(CGDisplayConfigRef?, CGDirectDisplayID, Int32, Int32) -> CGError](./cgconfiguredisplayorigin%28_,_,_,_%29.md)
  Configures the origin of a display relative to the global display coordinate space.
- [func CGConfigureDisplayStereoOperation(CGDisplayConfigRef?, CGDirectDisplayID, boolean_t, boolean_t) -> CGError](./cgconfiguredisplaystereooperation%28_,_,_,_%29.md)
  Enables or disables stereo operation for a display, as part of a display configuration.
- [func CGConfigureDisplayWithDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CGDisplayMode?, CFDictionary?) -> CGError](./cgconfiguredisplaywithdisplaymode%28_,_,_,_%29.md)
  Configures the display mode of a display.
- [func CGCursorIsDrawnInFramebuffer() -> boolean_t](./cgcursorisdrawninframebuffer%28%29.md)
  Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory.
- [func CGCursorIsVisible() -> boolean_t](./cgcursorisvisible%28%29.md)
  Returns a Boolean value indicating whether the mouse cursor is visible.
- [CGColorConversionInfoCreateFromList](./cgcolorconversioninfocreatefromlist.md)
  Creates a conversion between an arbitrary number of specified color spaces.
- [CGContextDrawPDFDocument](./cgcontextdrawpdfdocument.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgsetlocaleventsfilterduringsuppressionstate(_:_:))*