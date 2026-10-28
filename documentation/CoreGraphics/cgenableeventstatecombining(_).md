# CGEnableEventStateCombining(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Enables or disables the merging of actual key and mouse state with the application-specified state in a synthetic event.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: No longer supported

## Declaration

```swift
func CGEnableEventStateCombining(_ combineState: boolean_t) -> CGError
```

```c
extern CGError CGEnableEventStateCombining(boolean_t combineState);
```

## Return Value

A result code. See the result codes described in [Quartz Display Services](./quartz-display-services.md).

## Discussion

By default, the flags that indicate modifier key state (Command, Option, Shift, Control, and so on) from the system’s keyboard and from other event sources are ORed together as an event is posted into the system, and current key and mouse button state is considered in generating new events. This function allows your application to enable or disable the merging of event state. When combining is turned off, the event state propagated in the events posted by your application reflect state built up only by your application. The state within your application’s generated event will not be combined with the system’s current state, so the system-wide state reflecting key and mouse button state will remain unchanged. When called with `doCombineState` equal to `false`, this function initializes local (per application) state tracking information to a state of all keys, modifiers, and mouse buttons up. When called with `doCombineState` equal to `true`, the current global state of keys, modifiers, and mouse buttons are used in generating events.

This function is not recommended for general use because of undocumented special cases and undesirable side effects. The recommended replacement for this function is to use Quartz events and Quartz event sources. This allows you to control exactly which, if any, external event sources will contribute to the state used to create an event.

## Parameters

- `combineState`: Pass `true` to specify that the actual key and mouse state are merged with the application-specified state in a synthetic event; otherwise, pass `false`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgenableeventstatecombining(_:))*