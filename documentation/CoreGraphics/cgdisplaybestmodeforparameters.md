# CGDisplayBestModeForParameters(_:_:_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Returns information about the display mode closest to a specified depth and screen size.

**Availability**:
- Mac Catalyst 13.1+

## Declaration

```swift
func CGDisplayBestModeForParameters(_ display: CGDirectDisplayID, _ bitsPerPixel: Int, _ width: Int, _ height: Int, _ exactMatch: UnsafeMutablePointer<boolean_t>?) -> CFDictionary?
```

#### Return Value

A display mode dictionary, or `NULL` if the display is invalid. The dictionary is owned by the system and you should not release it. The dictionary contains information about the display mode closest to the specified depth and screen size. For a list of the properties in a display mode dictionary, see [`Display Mode Standard Properties`](display-mode-standard-properties.md) and [`Display Mode Optional Properties`](display-mode-optional-properties.md). For general information about using dictionaries, see [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary).

#### Discussion

This function tries to find an optimal display mode for the specified display. The function first tries to find a mode with the specified pixel depth and dimensions equal to or greater than the specified width and height. If no depth match is found, it tries to find a mode with greater depth and the same or greater dimensions. If a suitable display mode is not found, this function simply returns the current display mode.

##### Special Considerations

This deprecated function selects a display mode closest to the specified parameters. Starting in OS X v10.6 new display mode APIs should be used to query display modes so that an application can tailor its definition of “best” to its graphics and memory needs.

## Parameters

- `display`: The identifier of the display to optimize.
- `bitsPerPixel`: Optimal display depth in bits per pixel. Note that this value is not the same as pixel depth, which is the number of bits per channel or component.
- `width`: Optimal display width in pixel units.
- `height`: Optimal display height in pixel units.
- `exactMatch`: A pointer to a Boolean variable. On return, its value is   if an exact match in display depth, width, and height is found; otherwise,  . If this information is not needed, pass  .

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaybestmodeforparameters(_:_:_:_:_:))*