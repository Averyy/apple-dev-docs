# CGDisplaySwitchToMode(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Switches a display to a different mode.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CGDisplaySetDisplayMode(_:_:_:)`](./cgdisplaysetdisplaymode%28_,_,_%29.md) instead.

## Declaration

```swift
func CGDisplaySwitchToMode(_ display: CGDirectDisplayID, _ mode: CFDictionary?) -> CGError
```

```c
extern CGError CGDisplaySwitchToMode(CGDirectDisplayID display, CFDictionaryRef mode);
```

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

## Discussion

This function switches the display mode of the specified display. The operation is always synchronous; the function does not return until the mode switch is complete. Note that after switching, display parameters and addresses may change.

The selected display mode persists for the life of the calling program. When the program terminates, the display mode automatically reverts to the permanent setting in the Displays panel of System Preferences.

When changing the display mode of a display in a mirroring set, other displays in the mirroring set will be assigned a mode that’s capable of mirroring the bounds of the display being adjusted. To avoid this automatic behavior, you can use the following procedure: call[`CGBeginDisplayConfiguration(_:)`](./cgbegindisplayconfiguration%28_%29.md), call [`CGConfigureDisplayMode(_:_:_:)`](./cgconfiguredisplaymode%28_,_,_%29.md) for each display to explicitly set the mode, and finally call [`CGCompleteDisplayConfiguration(_:_:)`](./cgcompletedisplayconfiguration%28_,_%29.md)

### Special Considerations

This deprecated function takes as a parameter a display mode dictionary. Starting in OS X v10.6, display mode dictionaries have been replaced by the `CGDisplayMode` opaque type.

## Parameters

- `display`: The identifier of the display to be accessed.
- `mode`: A display mode dictionary that contains information about the display mode to set. The dictionary passed in must be a dictionary returned by another Quartz display function such as [`CGDisplayAvailableModes(_:)`](./cgdisplayavailablemodes%28_%29.md) or [`CGDisplayBestModeForParameters(_:_:_:_:_:)`](./cgdisplaybestmodeforparameters%28_,_,_,_,_%29.md). For a list of the properties in a display mode dictionary, see [Display Mode Standard Properties](./display-mode-standard-properties.md) and [Display Mode Optional Properties](./display-mode-optional-properties.md). For general information about using dictionaries, see [`CFDictionary`](../CoreFoundation/cfdictionary.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplayswitchtomode(_:_:))*