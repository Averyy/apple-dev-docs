# CGSetDisplayTransferByFormula(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Sets the gamma function for a display by specifying the coefficients of the gamma transfer formula.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func CGSetDisplayTransferByFormula(_ display: CGDirectDisplayID, _ redMin: CGGammaValue, _ redMax: CGGammaValue, _ redGamma: CGGammaValue, _ greenMin: CGGammaValue, _ greenMax: CGGammaValue, _ greenGamma: CGGammaValue, _ blueMin: CGGammaValue, _ blueMax: CGGammaValue, _ blueGamma: CGGammaValue) -> CGError
```

```c
extern CGError CGSetDisplayTransferByFormula(CGDirectDisplayID display, CGGammaValue redMin, CGGammaValue redMax, CGGammaValue redGamma, CGGammaValue greenMin, CGGammaValue greenMax, CGGammaValue greenGamma, CGGammaValue blueMin, CGGammaValue blueMax, CGGammaValue blueGamma);
```

#### Return Value

A result code. See `Core Graphics Data Types and Constants`.

#### Discussion

This function uses the specified parameter values to compute a gamma correction table for the specified display. The values in the table are computed by sampling the following gamma transfer formula for a range of indices from 0 to 1:

```objc
value = Min + ((Max - Min) * pow(index, Gamma))
```

The resulting values are converted to a machine-specific format and loaded into display hardware.

## Parameters

- `display`: The identifier of the display to be accessed.
- `redMin`: The minimum value of the red channel in the gamma table. The value should be a number in the interval [0, redMax).
- `redMax`: The maximum value of the red channel in the gamma table. The value should be a number in the interval (redMin, 1].
- `redGamma`: A positive value used to compute the red channel in the gamma table.
- `greenMin`: The minimum value of the green channel in the gamma table. The value should be a number in the interval [0, greenMax).
- `greenMax`: The maximum value of the green channel in the gamma table. The value should be a number in the interval (greenMin, 1].
- `greenGamma`: A positive value used to compute the green channel in the gamma table.
- `blueMin`: The minimum value of the blue channel in the gamma table. The value should be a number in the interval [0, blueMax).
- `blueMax`: The maximum value of the blue channel in the gamma table. The value should be a number in the interval (blueMin, 1].
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
- [CGColorConversionInfoCreateFromList](./cgcolorconversioninfocreatefromlist.md)
  Creates a conversion between an arbitrary number of specified color spaces.
- [CGContextDrawPDFDocument](./cgcontextdrawpdfdocument.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgsetdisplaytransferbyformula(_:_:_:_:_:_:_:_:_:_:))*