# CGGetDisplayTransferByFormula(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Gets the coefficients of the gamma transfer formula for a display.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func CGGetDisplayTransferByFormula(_ display: CGDirectDisplayID, _ redMin: UnsafeMutablePointer<CGGammaValue>?, _ redMax: UnsafeMutablePointer<CGGammaValue>?, _ redGamma: UnsafeMutablePointer<CGGammaValue>?, _ greenMin: UnsafeMutablePointer<CGGammaValue>?, _ greenMax: UnsafeMutablePointer<CGGammaValue>?, _ greenGamma: UnsafeMutablePointer<CGGammaValue>?, _ blueMin: UnsafeMutablePointer<CGGammaValue>?, _ blueMax: UnsafeMutablePointer<CGGammaValue>?, _ blueGamma: UnsafeMutablePointer<CGGammaValue>?) -> CGError
```

```c
extern CGError CGGetDisplayTransferByFormula(CGDirectDisplayID display, CGGammaValue *redMin, CGGammaValue *redMax, CGGammaValue *redGamma, CGGammaValue *greenMin, CGGammaValue *greenMax, CGGammaValue *greenGamma, CGGammaValue *blueMin, CGGammaValue *blueMax, CGGammaValue *blueGamma);
```

#### Return Value

A result code. To interpret the result code, see [`CGError`](./cgerror.md).

#### Discussion

For information about the gamma transfer formula, see the description of the function [`CGSetDisplayTransferByFormula(_:_:_:_:_:_:_:_:_:_:)`](./cgsetdisplaytransferbyformula%28_,_,_,_,_,_,_,_,_,_%29.md).

## Parameters

- `display`: The identifier of the display to access.
- `redMin`: The minimum value of the red channel in the gamma table. The value is a number in the interval `[0, redMax]`.
- `redMax`: The maximum value of the red channel in the gamma table. The value is a number in the interval `[redMin, 1]`.
- `redGamma`: A positive value used to compute the red channel in the gamma table.
- `greenMin`: The minimum value of the green channel in the gamma table. The value is a number in the interval `[0, greenMax]`.
- `greenMax`: The maximum value of the green channel in the gamma table. The value is a number in the interval `[greenMin, 1]`.
- `greenGamma`: A positive value used to compute the green channel in the gamma table.
- `blueMin`: The minimum value of the blue channel in the gamma table. The value is a number in the interval `[0, blueMax]`.
- `blueMax`: The maximum value of the blue channel in the gamma table. The value is a number in the interval `[blueMin, 1]`.
- `blueGamma`: A positive value used to compute the blue channel in the gamma table.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggetdisplaytransferbyformula(_:_:_:_:_:_:_:_:_:_:))*