# CGWindowListCreateImage(_:_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Returns a composite image based on a dynamically generated list of windows.

## Declaration

```swift
func CGWindowListCreateImage(_ screenBounds: CGRect, _ listOption: CGWindowListOption, _ windowID: CGWindowID, _ imageOption: CGWindowImageOption) -> CGImage?
```

#### Return Value

A composite image formed from the contents of the specified set of windows. If the windows are unreadable or no windows meet the specified criteria, this function returns an image that is either 0 by 0 pixels in size or is of the specified size but is filled with the transparent black color. If you call this function from outside of a GUI security session or when no window server is running, this function returns `NULL`.

#### Discussion

Any windows that are onscreen but whose sharing setting is set to [`CGWindowSharingType.none`](cgwindowsharingtype/none.md) are skipped and not included in the resulting image. If this results in no windows being available in the selected range, this function returns `NULL`.

## Parameters

- `screenBounds`: The rectangle that you want to capture. The coordinates of the rectangle must be specified in screen coordinates, where the screen origin is in the upper-left corner of the main display and y-axis values increase downward. Specify   to indicate the minimum rectangle that encloses the specified windows. Specify   to capture the entire desktop area.
- `listOption`: The options describing which windows to include in the image. Typical options let you choose all windows or windows above or below the window specified in the   parameter. For more information, see  .
- `windowID`: The ID of the window to use as a reference point when determining which other windows to include in the image. For options that do not require a reference window, this parameter can be  .
- `imageOption`: The options that determine which parts of the window to capture. If you specified   for the   parameter, these options affect the resulting bounding box used for the image. For example, if you include a window’s screen effects in the image, the bounding box may need to be slightly larger to accommodate those effects. For a list of possible options, see  .

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlistcreateimage(_:_:_:_:))*