# Display Stream Optional Property Keys

**Framework**: Core Graphics

These keys are used to populate the `properties` dictionary used when creating a new display stream.

## Topics

### Constants
- [class let sourceRect: CFString](cgdisplaystream/sourcerect.md)
  This key specifies that the display stream only samples a subset of the display’s framebuffer.
- [class let destinationRect: CFString](cgdisplaystream/destinationrect.md)
  This key specifies that the display stream outputs the frame data into a subset of the output `IOSurface` object.
- [class let preserveAspectRatio: CFString](cgdisplaystream/preserveaspectratio.md)
  This key specifies whether the display stream preserves the aspect ratio of the source pixel data. If this key is not included in the dictionary, then the aspect ratio is preserved. If the aspect ratio is preserved, then the display stream adds black bars to the output data. If the aspect ratio is not preserved, then the pixel data is stretched to fit the output buffer’s dimensions. The value associated with the key must be a `CFBoolean`.
- [class let colorSpace: CFString](cgdisplaystream/colorspace.md)
  This key specifies the color space of the output buffer. If this key is not included in the dictionary, the output buffer uses the same color space as the display. The value associated with this key must be a [`CGColorSpace`](cgcolorspace.md) for the desired color space.
- [class let minimumFrameTime: CFString](cgdisplaystream/minimumframetime.md)
  This key specifies the desired minimum time between frame updates, allowing you to throttle the rate at which updates are received. If this key is not included in the dictionary, the default value is `0`, meaning that updates are not throttled. The value must be specified as a `CFNumber`.
- [class let showCursor: CFString](cgdisplaystream/showcursor.md)
  This key specifies whether the cursor should appear in the stream. If this key is not included in the dictionary, the cursor is visible. The value must be specified as a `CFBoolean`.
- [class let queueDepth: CFString](cgdisplaystream/queuedepth.md)
  This key specifies the number of frames to keep in the queue. If this key is not included in the dictionary, the default value is `3` frames. Specifying more frames uses more memory, but may allow you to process frame data without stalling the display stream. The value associated with this key should be specified as a `CFNumber`, and should not exceed `8` frames.
- [class let yCbCrMatrix: CFString](cgdisplaystream/ycbcrmatrix.md)
  This key should only be included if you the display stream is creating output frames in either the 420v or 420f formats. It is used to specify the YCbCr matrix applied to the output surface.

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
- [Display Mode Standard Properties](display-mode-standard-properties.md)
  Keys for the standard properties in a display mode dictionary.
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
- [Display Stream YCbCr to RGB conversion Matrix Options](display-stream-ycbcr-to-rgb-conversion-matrix-options.md)
  These strings are used to specify a matrix for the [`yCbCrMatrix`](cgdisplaystream/ycbcrmatrix.md) option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/display-stream-optional-property-keys)*