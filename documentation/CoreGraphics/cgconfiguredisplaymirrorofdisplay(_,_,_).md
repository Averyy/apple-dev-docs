# CGConfigureDisplayMirrorOfDisplay(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Changes the configuration of a mirroring set.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func CGConfigureDisplayMirrorOfDisplay(_ config: CGDisplayConfigRef?, _ display: CGDirectDisplayID, _ master: CGDirectDisplayID) -> CGError
```

```c
extern CGError CGConfigureDisplayMirrorOfDisplay(CGDisplayConfigRef config, CGDirectDisplayID display, CGDirectDisplayID master);
```

#### Return Value

A result code. See `Core Graphics Data Types and Constants`.

#### Discussion

Display mirroring and display matte generation are implemented either in hardware (preferred) or software, at the discretion of the device driver.

- Hardware mirroring

With hardware mirroring enabled, all drawing is directed to the primary display—see [`CGDisplayPrimaryDisplay(_:)`](./cgdisplayprimarydisplay%28_%29.md).

If the device driver selects hardware matte generation, the display bounds and row-bytes values are adjusted to reflect the active drawable area.

- Software mirroring

In this form of mirroring, identical content is drawn into each display in the mirroring set. Applications that use the window system need not be concerned about mirroring, as the window system takes care of all flushing of window content to the appropriate displays.

Applications that draw directly to the display, as with display capture, must make sure to draw the same content to all mirrored displays in a software mirror set. When drawing to software mirrored displays using a full screen OpenGL context (not drawing through a window), you should create shared OpenGL contexts for each display and rerender for each display.

You can use the function [`CGGetActiveDisplayList(_:_:_:)`](./cggetactivedisplaylist%28_,_,_%29.md) to determine which displays are active, or drawable. This automatically gives your application the correct view of the current displays.

## Parameters

- `config`: A display configuration, acquired by calling [`CGBeginDisplayConfiguration(_:)`](./cgbegindisplayconfiguration%28_%29.md).
- `display`: The identifier of the display to add to a mirroring set.
- `master`: A display in a mirroring set, or `kCGNullDirectDisplay` to disable mirroring. To specify the main display, use [`CGMainDisplayID()`](./cgmaindisplayid%28%29.md).

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
- [func CGDirectDisplayCopyCurrentMetalDevice(CGDirectDisplayID) -> (any MTLDevice)?](./cgdirectdisplaycopycurrentmetaldevice%28_%29.md)
  Returns the GPU device instance that’s currently driving a display.
- [CGColorConversionInfoCreateFromList](./cgcolorconversioninfocreatefromlist.md)
  Creates a conversion between an arbitrary number of specified color spaces.
- [CGContextDrawPDFDocument](./cgcontextdrawpdfdocument.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgconfiguredisplaymirrorofdisplay(_:_:_:))*