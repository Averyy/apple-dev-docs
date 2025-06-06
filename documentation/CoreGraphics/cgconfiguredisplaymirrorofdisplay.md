# CGConfigureDisplayMirrorOfDisplay(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Changes the configuration of a mirroring set.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func CGConfigureDisplayMirrorOfDisplay(_ config: CGDisplayConfigRef?, _ display: CGDirectDisplayID, _ master: CGDirectDisplayID) -> CGError
```

#### Return Value

A result code. See `Core Graphics Data Types and Constants`.

#### Discussion

Display mirroring and display matte generation are implemented either in hardware (preferred) or software, at the discretion of the device driver.

- Hardware mirroring

With hardware mirroring enabled, all drawing is directed to the primary display—see [`CGDisplayPrimaryDisplay(_:)`](cgdisplayprimarydisplay(_:).md).

If the device driver selects hardware matte generation, the display bounds and row-bytes values are adjusted to reflect the active drawable area.

- Software mirroring

In this form of mirroring, identical content is drawn into each display in the mirroring set. Applications that use the window system need not be concerned about mirroring, as the window system takes care of all flushing of window content to the appropriate displays.

Applications that draw directly to the display, as with display capture, must make sure to draw the same content to all mirrored displays in a software mirror set. When drawing to software mirrored displays using a full screen OpenGL context (not drawing through a window), you should create shared OpenGL contexts for each display and rerender for each display.

You can use the function [`CGGetActiveDisplayList(_:_:_:)`](cggetactivedisplaylist(_:_:_:).md) to determine which displays are active, or drawable. This automatically gives your application the correct view of the current displays.

## Parameters

- `config`: A display configuration, acquired by calling  .
- `display`: The identifier of the display to add to a mirroring set.
- `master`: A display in a mirroring set, or   to disable mirroring. To specify the main display, use  .

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
- [func CGDirectDisplayCopyCurrentMetalDevice(CGDirectDisplayID) -> (any MTLDevice)?](cgdirectdisplaycopycurrentmetaldevice(_:).md)
  Returns the GPU device instance that’s currently driving a display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgconfiguredisplaymirrorofdisplay(_:_:_:))*