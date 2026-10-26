# counterForEventType(_:eventType:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Type Method

Returns a count of events of a given type seen since the window server started.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
class func counterForEventType(_ stateID: CGEventSourceStateID, eventType: CGEventType) -> UInt32
```

```c
extern uint32_t CGEventSourceCounterForEventType(CGEventSourceStateID stateID, CGEventType eventType);
```

#### Return Value

The count of events of the specified type seen since the window server started.

#### Discussion

Quartz provides these counters for applications that monitor user activity. For example, an application could prompt a typist to take a break to reduce repetitive stress injuries.

Modifier keys produce `kCGEventFlagsChanged` events, not `kCGEventKeyDown` events, and do so both on press and release. The volume, brightness, and CD eject keys on some keyboards (both desktop and laptop) do not generate key up or key down events.

For various reasons, the number of key up and key down events may not be the same when all keyboard keys are up. As a result, a mismatch does not necessarily indicate that some keys are down.

Key autorepeat events are not counted.

## Parameters

- `stateID`: The source state to access. Pass one of the constants listed in [`CGEventSourceStateID`](../cgeventsourcestateid.md).
- `eventType`: The event type to access. To get the count of input events—keyboard, mouse, or tablet—specify `kCGAnyInputEventType`.

## See Also

### Functions
- [func CGAcquireDisplayFadeReservation(CGDisplayReservationInterval, UnsafeMutablePointer<CGDisplayFadeReservationToken>?) -> CGError](../cgacquiredisplayfadereservation%28_,_%29.md)
  Reserves the fade hardware for a specified time interval.
- [func CGAssociateMouseAndMouseCursorPosition(boolean_t) -> CGError](../cgassociatemouseandmousecursorposition%28_%29.md)
  Connects or disconnects the mouse and cursor while an application is in the foreground.
- [func CGBeginDisplayConfiguration(UnsafeMutablePointer<CGDisplayConfigRef?>?) -> CGError](../cgbegindisplayconfiguration%28_%29.md)
  Begins a new set of display configuration changes.
- [func CGCancelDisplayConfiguration(CGDisplayConfigRef?) -> CGError](../cgcanceldisplayconfiguration%28_%29.md)
  Cancels a set of display configuration changes.
- [func CGCaptureAllDisplays() -> CGError](../cgcapturealldisplays%28%29.md)
  Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [func CGCaptureAllDisplaysWithOptions(CGCaptureOptions) -> CGError](../cgcapturealldisplayswithoptions%28_%29.md)
  Captures all attached displays, using the specified options.
- [func CGCompleteDisplayConfiguration(CGDisplayConfigRef?, CGConfigureOption) -> CGError](../cgcompletedisplayconfiguration%28_,_%29.md)
  Completes a set of display configuration changes.
- [func CGConfigureDisplayFadeEffect(CGDisplayConfigRef?, CGDisplayFadeInterval, CGDisplayFadeInterval, Float, Float, Float) -> CGError](../cgconfiguredisplayfadeeffect%28_,_,_,_,_,_%29.md)
  Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [func CGConfigureDisplayMirrorOfDisplay(CGDisplayConfigRef?, CGDirectDisplayID, CGDirectDisplayID) -> CGError](../cgconfiguredisplaymirrorofdisplay%28_,_,_%29.md)
  Changes the configuration of a mirroring set.
- [func CGConfigureDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CFDictionary?) -> CGError](../cgconfiguredisplaymode%28_,_,_%29.md)
  Configures the display mode of a display.
- [func CGConfigureDisplayOrigin(CGDisplayConfigRef?, CGDirectDisplayID, Int32, Int32) -> CGError](../cgconfiguredisplayorigin%28_,_,_,_%29.md)
  Configures the origin of a display relative to the global display coordinate space.
- [func CGConfigureDisplayStereoOperation(CGDisplayConfigRef?, CGDirectDisplayID, boolean_t, boolean_t) -> CGError](../cgconfiguredisplaystereooperation%28_,_,_,_%29.md)
  Enables or disables stereo operation for a display, as part of a display configuration.
- [func CGConfigureDisplayWithDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CGDisplayMode?, CFDictionary?) -> CGError](../cgconfiguredisplaywithdisplaymode%28_,_,_,_%29.md)
  Configures the display mode of a display.
- [func CGCursorIsDrawnInFramebuffer() -> boolean_t](../cgcursorisdrawninframebuffer%28%29.md)
  Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory.
- [func CGCursorIsVisible() -> boolean_t](../cgcursorisvisible%28%29.md)
  Returns a Boolean value indicating whether the mouse cursor is visible.
- [CGColorConversionInfoCreateFromList](../cgcolorconversioninfocreatefromlist.md)
  Creates a conversion between an arbitrary number of specified color spaces.
- [CGContextDrawPDFDocument](../cgcontextdrawpdfdocument.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventsource/counterforeventtype(_:eventtype:))*