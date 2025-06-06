# CGGetEventTapList(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Gets a list of currently installed event taps.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CGGetEventTapList(_ maxNumberOfTaps: UInt32, _ tapList: UnsafeMutablePointer<CGEventTapInformation>?, _ eventTapCount: UnsafeMutablePointer<UInt32>?) -> CGError
```

#### Return Value

A result code. See the result codes described in [`Quartz Display Services`](quartz-display-services.md).

#### Discussion

Each call to this function has the side effect of resetting the minimum and maximum latency values in the `tapList` parameter to the corresponding average values. Values reported in these fields reflect the minimum and maximum values seen since the preceding call, or the instantiation of the tap. This allows a monitoring tool to evaluate the best and worst case latency over time and under various operating conditions.

## Parameters

- `maxNumberOfTaps`: The length of the array you provide in the   parameter.
- `tapList`: An array of event tap information structures. You are responsible for allocating storage for the array. On return, your array contains a list of currently installed event taps. If you pass   in this parameter, the   parameter is ignored, and the   variable is filled in with the number of event taps that are currently installed.
- `eventTapCount`: A pointer to a   variable. On return, the variable contains actual number of array elements filled in.

## See Also

- [func CGAcquireDisplayFadeReservation(CGDisplayReservationInterval, UnsafeMutablePointer<CGDisplayFadeReservationToken>?) -> CGError](cgacquiredisplayfadereservation(_:_:).md)
  Reserves the fade hardware for a specified time interval.
- [func CGAssociateMouseAndMouseCursorPosition(boolean_t) -> CGError](cgassociatemouseandmousecursorposition(_:).md)
  Connects or disconnects the mouse and cursor while an application is in the foreground.
- [func CGBeginDisplayConfiguration(UnsafeMutablePointer<CGDisplayConfigRef?>?) -> CGError](cgbegindisplayconfiguration(_:).md)
  Begins a new set of display configuration changes.
- [func CGCancelDisplayConfiguration(CGDisplayConfigRef?) -> CGError](cgcanceldisplayconfiguration(_:).md)
  Cancels a set of display configuration changes.
- [func CGCaptureAllDisplays() -> CGError](cgcapturealldisplays().md)
  Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [func CGCaptureAllDisplaysWithOptions(CGCaptureOptions) -> CGError](cgcapturealldisplayswithoptions(_:).md)
  Captures all attached displays, using the specified options.
- [func CGCompleteDisplayConfiguration(CGDisplayConfigRef?, CGConfigureOption) -> CGError](cgcompletedisplayconfiguration(_:_:).md)
  Completes a set of display configuration changes.
- [func CGConfigureDisplayFadeEffect(CGDisplayConfigRef?, CGDisplayFadeInterval, CGDisplayFadeInterval, Float, Float, Float) -> CGError](cgconfiguredisplayfadeeffect(_:_:_:_:_:_:).md)
  Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [func CGConfigureDisplayMirrorOfDisplay(CGDisplayConfigRef?, CGDirectDisplayID, CGDirectDisplayID) -> CGError](cgconfiguredisplaymirrorofdisplay(_:_:_:).md)
  Changes the configuration of a mirroring set.
- [func CGConfigureDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CFDictionary?) -> CGError](cgconfiguredisplaymode(_:_:_:).md)
  Configures the display mode of a display.
- [func CGConfigureDisplayOrigin(CGDisplayConfigRef?, CGDirectDisplayID, Int32, Int32) -> CGError](cgconfiguredisplayorigin(_:_:_:_:).md)
  Configures the origin of a display relative to the global display coordinate space.
- [func CGConfigureDisplayStereoOperation(CGDisplayConfigRef?, CGDirectDisplayID, boolean_t, boolean_t) -> CGError](cgconfiguredisplaystereooperation(_:_:_:_:).md)
  Enables or disables stereo operation for a display, as part of a display configuration.
- [func CGConfigureDisplayWithDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CGDisplayMode?, CFDictionary?) -> CGError](cgconfiguredisplaywithdisplaymode(_:_:_:_:).md)
  Configures the display mode of a display.
- [func CGCursorIsDrawnInFramebuffer() -> boolean_t](cgcursorisdrawninframebuffer().md)
  Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory.
- [func CGCursorIsVisible() -> boolean_t](cgcursorisvisible().md)
  Returns a Boolean value indicating whether the mouse cursor is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggeteventtaplist(_:_:_:))*