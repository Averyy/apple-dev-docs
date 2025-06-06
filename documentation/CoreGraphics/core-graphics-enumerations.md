# Core Graphics Enumerations

**Framework**: Core Graphics

## Topics

### Enumerations
- [struct CGCaptureOptions](cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [enum CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
- [enum CGColorRenderingIntent](cgcolorrenderingintent.md)
  Handling options for colors that are not located within the destination color space of a graphics context.
- [struct CGConfigureOption](cgconfigureoption.md)
  The scope of the changes in a display configuration transaction.
- [struct CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md)
  The configuration parameters that are passed to a display reconfiguration callback function.
- [enum CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md)
  Describes a frame update event.
- [enum CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md)
  Use these constants to determine which rectangles your app is interested in.
- [enum CGError](cgerror.md)
  A uniform type for result codes returned by functions in Core Graphics.
- [enum CGEventField](cgeventfield.md)
  Constants used as keys to access specialized fields in low-level events.
- [struct CGEventFilterMask](cgeventfiltermask.md)
  Specify masks for classes of low-level events that can be filtered during event suppression states.
- [struct CGEventFlags](cgeventflags.md)
  Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [enum CGEventMouseSubtype](cgeventmousesubtype.md)
  Constants used with the [`CGEventField.mouseEventSubtype`](cgeventfield/mouseeventsubtype.md) event field.
- [enum CGEventSourceStateID](cgeventsourcestateid.md)
  Constants that specify the possible source states of an event source.
- [enum CGEventSuppressionState](cgeventsuppressionstate.md)
  Specify the event suppression states that can occur after posting an event.
- [enum CGEventTapLocation](cgeventtaplocation.md)
  Constants that specify possible tapping points for events.
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.
- [enum CGEventTapPlacement](cgeventtapplacement.md)
  Constants that specify where a new event tap is inserted into the list of active event taps.
- [enum CGEventType](cgeventtype.md)
  Constants that specify the different types of input events.
- [enum CGGesturePhase](cggesturephase.md)
- [enum CGGlyphDeprecatedEnum](cgglyphdeprecatedenum.md)
- [enum CGImageByteOrderInfo](cgimagebyteorderinfo.md)
- [enum CGMomentumScrollPhase](cgmomentumscrollphase.md)
- [enum CGMouseButton](cgmousebutton.md)
  Constants that specify buttons on a one, two, or three-button mouse.
- [struct CGScreenUpdateOperation](cgscreenupdateoperation.md)
  Types of screen-update operations.
- [enum CGScrollEventUnit](cgscrolleventunit.md)
  Constants that specify the unit of measurement for a scrolling event.
- [enum CGScrollPhase](cgscrollphase.md)
- [enum CGWindowBackingType](cgwindowbackingtype.md)
  The data type used to specify the backing option for a given window.
- [struct CGWindowImageOption](cgwindowimageoption.md)
  The data type to use to specify the type of image to be generated for a window.
- [enum CGWindowLevelKey](cgwindowlevelkey.md)
  Keys that represent the standard window levels in macOS. Quartz includes these keys to support application frameworks like Cocoa. Applications do not need to use them directly.
- [struct CGWindowListOption](cgwindowlistoption.md)
  The data type used to specify the options for gathering a list of windows.
- [enum CGWindowSharingType](cgwindowsharingtype.md)
  The data type used to specify the sharing mode used by a window.
- [enum CGImagePixelFormatInfo](cgimagepixelformatinfo.md)
- [enum CGLineCap](cglinecap.md)
  Styles for rendering the endpoint of a stroked line.
- [enum CGLineJoin](cglinejoin.md)
  Junction types for stroked lines.
- [struct CGPDFAccessPermissions](cgpdfaccesspermissions.md)
- [enum CGPDFTagType](cgpdftagtype.md)
- [enum CGTextEncoding](cgtextencoding.md)
  Text encodings for fonts.
- [enum CGToneMapping](cgtonemapping.md)
- [enum CGPathFillRule](cgpathfillrule.md)
  Rules for determining which regions are interior to a path, used by the [`fillPath(using:)`](cgcontext/fillpath(using:).md) and [`clip(using:)`](cgcontext/clip(using:).md) methods.

## See Also

- [Core Graphics Structures](core-graphics-structures.md)
- [Core Graphics Constants](core-graphics-constants.md)
- [Core Graphics Functions](core-graphics-functions.md)
- [Core Graphics Data Types](core-graphics-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/core-graphics-enumerations)*