# Display Mode Standard Properties

**Framework**: Core Graphics

Keys for the standard properties in a display mode dictionary.

#### Overview

To learn how to use these keys to access the values in a display mode dictionary, see [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary).

##### Special Considerations

Starting in OS X v10.6, display mode dictionaries have been made obsolete by the display mode opaque type. For more information on display modes, see[`Changing Display Modes (OS X v10.6 or later)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Articles/DisplayModes.html#//apple_ref/doc/uid/TP40004234).

## Topics

### Constants
- [var kCGDisplayWidth: String](kcgdisplaywidth.md)
  Specifies a CFNumber integer value that represents the width of the display in pixels.
- [var kCGDisplayHeight: String](kcgdisplayheight.md)
  Specifies a CFNumber integer value that represents the height of the display in pixels.
- [var kCGDisplayMode: String](kcgdisplaymode.md)
  Specifies a `CFNumber` integer value that represents the I/O Kit display mode number.
- [var kCGDisplayBitsPerPixel: String](kcgdisplaybitsperpixel.md)
  Specifies a CFNumber integer value that represents the number of bits in a pixel.
- [var kCGDisplayBitsPerSample: String](kcgdisplaybitspersample.md)
  Specifies a CFNumber integer value that represents the number of bits in an individual sample (for example, a color value in an RGB pixel).
- [var kCGDisplaySamplesPerPixel: String](kcgdisplaysamplesperpixel.md)
  Specifies a CFNumber integer value that represents the number of samples in a pixel.
- [var kCGDisplayRefreshRate: String](kcgdisplayrefreshrate.md)
  Specifies a `CFNumber` double-precision floating point value that represents the refresh rate of a CRT display.
- [var kCGDisplayModeUsableForDesktopGUI: String](kcgdisplaymodeusablefordesktopgui.md)
  Specifies a CFBoolean value that indicates whether the display is suitable for use with the macOS graphical user interface. The criteria include factors such as sufficient width and height and adequate pixel depth.
- [var kCGDisplayIOFlags: String](kcgdisplayioflags.md)
  Specifies a CFNumber integer value that contains the I/O Kit display mode flags. For more information, see the header file `IOKit/IOGraphicsTypes.h`.
- [var kCGDisplayBytesPerRow: String](kcgdisplaybytesperrow.md)
  Specifies a CFNumber integer value that represents the number of bytes in a row on the display.

## See Also

- [struct CGCaptureOptions](cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [struct CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md)
  The configuration parameters that are passed to a display reconfiguration callback function.
- [struct CGConfigureOption](cgconfigureoption.md)
  The scope of the changes in a display configuration transaction.
- [Display Fade Blend Fractions](display-fade-blend-fractions.md)
  The lower and upper bounds for blend color fractions during a display fade operation.
- [Display Fade Constants](display-fade-constants.md)
  Values relating to fade operations.
- [Display ID Defaults](display-id-defaults.md)
  Default values for a display ID.
- [Display Mode Optional Properties](display-mode-optional-properties.md)
  Keys for optional properties in a display mode dictionary.
- [Reserved Window Levels](reserved-window-levels.md)
  Window level constants.
- [struct CGScreenUpdateOperation](cgscreenupdateoperation.md)
  Types of screen-update operations.
- [enum CGWindowLevelKey](cgwindowlevelkey.md)
  Keys that represent the standard window levels in macOS. Quartz includes these keys to support application frameworks like Cocoa. Applications do not need to use them directly.
- [Window Server Session Properties](window-server-session-properties.md)
  The keys for the standard properties in a window server session dictionary.
- [enum CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md)
  Use these constants to determine which rectangles your app is interested in.
- [enum CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md)
  Describes a frame update event.
- [Display Stream Optional Property Keys](display-stream-optional-property-keys.md)
  These keys are used to populate the `properties` dictionary used when creating a new display stream.
- [Display Stream YCbCr to RGB conversion Matrix Options](display-stream-ycbcr-to-rgb-conversion-matrix-options.md)
  These strings are used to specify a matrix for the [`yCbCrMatrix`](cgdisplaystream/ycbcrmatrix.md) option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/display-mode-standard-properties)*