# CGDisplayFade(_:_:_:_:_:_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Performs a single fade operation.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func CGDisplayFade(_ token: CGDisplayFadeReservationToken, _ duration: CGDisplayFadeInterval, _ startBlend: CGDisplayBlendFraction, _ endBlend: CGDisplayBlendFraction, _ redBlend: Float, _ greenBlend: Float, _ blueBlend: Float, _ synchronous: boolean_t) -> CGError
```

```c
extern CGError CGDisplayFade(CGDisplayFadeReservationToken token, CGDisplayFadeInterval duration, CGDisplayBlendFraction startBlend, CGDisplayBlendFraction endBlend, float redBlend, float greenBlend, float blueBlend, boolean_t synchronous);
```

#### Return Value

A result code. To interpret the result code, see [`CGError`](./cgerror.md).

#### Discussion

Over the fade operation time interval, Quartz interpolates a blending coefficient between the starting and ending values given, applying a nonlinear (sine-based) bias term. Using this coefficient, Quartz blends the video output with the specified color.

The following example shows how to perform a 2-second synchronous fade-out to black:

```objc
CGDisplayFade (
    myToken,
    2.0,                        // 2 seconds
    kCGDisplayBlendNormal,      // starting state
    kCGDisplayBlendSolidColor,  // ending state
    0.0, 0.0, 0.0,              // black
    true                        // wait for completion
);
```

To perform a 2-second asynchronous fade-in from black:

```objc
CGDisplayFade (
    myToken,
    2.0,                        // 2 seconds
    kCGDisplayBlendSolidColor,  // starting state
    kCGDisplayBlendNormal,      // ending state
    0.0, 0.0, 0.0,              // black
    false                       // don't wait for completion
);
```

If you specify an asynchronous fade operation, it’s safe to call [`CGReleaseDisplayFadeReservation(_:)`](./cgreleasedisplayfadereservation%28_%29.md) immediately after this function returns.

## Parameters

- `token`: A reservation token for the fade hardware you acquire by calling [`CGAcquireDisplayFadeReservation(_:_:)`](./cgacquiredisplayfadereservation%28_,_%29.md).
- `duration`: The desired number of seconds for the fade operation. You should use a value in the interval `[0, kCGMaxDisplayReservationInterval`]. If the value is `0`, Quartz applies the ending blend color immediately.
- `startBlend`: An intensity value in the interval `[0, 1]` that specifies the alpha component of the desired blend color at the beginning of the fade operation. For more information, see [Display Fade Blend Fractions](./display-fade-blend-fractions.md).
- `endBlend`: An intensity value in the interval `[0, 1]` that specifies the alpha component of the desired blend color at the end of the fade operation. For more information, see [Display Fade Blend Fractions](./display-fade-blend-fractions.md).
- `redBlend`: An intensity value in the interval `[0, 1]` that specifies the red component of the desired blend color.
- `greenBlend`: An intensity value in the interval `[0, 1]` that specifies the green component of the desired blend color.
- `blueBlend`: An intensity value in the interval `[0, 1]` that specifies the blue component of the desired blend color.
- `synchronous`: Pass `true` if you want the fade operation to be synchronous; otherwise, pass `false`. If a fade operation is synchronous, the function doesn’t return until the operation is complete.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplayfade(_:_:_:_:_:_:_:_:))*