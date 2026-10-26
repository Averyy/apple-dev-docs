# CGConfigureDisplayWithDisplayMode(_:_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Configures the display mode of a display.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
func CGConfigureDisplayWithDisplayMode(_ config: CGDisplayConfigRef?, _ display: CGDirectDisplayID, _ mode: CGDisplayMode?, _ options: CFDictionary?) -> CGError
```

```c
extern CGError CGConfigureDisplayWithDisplayMode(CGDisplayConfigRef config, CGDirectDisplayID display, CGDisplayModeRef mode, CFDictionaryRef options);
```

#### Return Value

A result code. If the request to change modes is successful, the result is `kCGErrorSuccess`. For other possible values, see [`CGError`](./cgerror.md).

#### Discussion

This function allows you to specify a display mode with which to configure the display using a transaction. Before using this function, call [`CGBeginDisplayConfiguration(_:)`](./cgbegindisplayconfiguration%28_%29.md) to acquire the display configuration token for the desired display. Call [`CGCompleteDisplayConfiguration(_:_:)`](./cgcompletedisplayconfiguration%28_,_%29.md) to execute the transaction.

Using this function to change the mode of a display in a mirroring set might cause Quartz to adjust settings of the other displays in the set. When necessary, Quartz adjusts the bounds, resolutions, and depth of the displays to a safe mode with matching depth and the smallest enclosing size.

## Parameters

- `config`: A display configuration you aquire by calling [`CGBeginDisplayConfiguration(_:)`](./cgbegindisplayconfiguration%28_%29.md).
- `display`: The identifier of the display to configure.
- `mode`: A display mode to configure.
- `options`: Reserved for future expansion. Pass `NULL` for now.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgconfiguredisplaywithdisplaymode(_:_:_:_:))*