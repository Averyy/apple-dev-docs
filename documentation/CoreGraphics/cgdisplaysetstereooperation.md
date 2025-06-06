# CGDisplaySetStereoOperation(_:_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Immediately enables or disables stereo operation for a display.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CGDisplaySetStereoOperation(_ display: CGDirectDisplayID, _ stereo: boolean_t, _ forceBlueLine: boolean_t, _ option: CGConfigureOption) -> CGError
```

#### Return Value

A result code. See `Core Graphics Data Types and Constants`.

#### Discussion

The system normally detects the presence of a stereo window and automatically switches a display containing a stereo window to stereo operation. This function forces a display to stereo operation immediately, and sets options (blue line sync signal) when in stereo operation.

On success, the display resolution, mirroring mode, and available display modes may change due to hardware-specific capabilities and limitations. You should check these settings to verify that they are appropriate for your application.

## Parameters

- `display`: The identifier of the display being configured.
- `stereo`: Pass   if you want to enable stereo operation. To disable it, pass  .
- `forceBlueLine`: When in stereo operation, a display may need to generate a special stereo sync signal as part of the video output.  The sync signal consists of a blue line that occupies the first 25% of the last scan line (for the left eye view), and the first 75% of the last scan line (for the right eye view). The remainder of the scan line is black. To force the display to generate this sync signal, pass  ; otherwise pass  .
- `option`: A constant that specifies the scope of the display configuration changes. For more information, see  .

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaysetstereooperation(_:_:_:_:))*