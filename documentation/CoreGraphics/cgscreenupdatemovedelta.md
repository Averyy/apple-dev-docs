# CGScreenUpdateMoveDelta

**Framework**: Core Graphics  
**Kind**: struct

The distance, in pixel units, that an onscreen region moves.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct CGScreenUpdateMoveDelta
```

#### Overview

Move operation notifications are restricted to changes that move a region by an integer number of pixels. The fields `dX` and `dY` describe the direction of movement:

- Positive values of `dX` indicate movement to the right.
- Negative values of `dX` indicate movement to the left.
- Positive values of `dY` indicate movement downward.
- Negative values of `dY` indicate movement upward.

## Topics

### Initializers
- [init()](cgscreenupdatemovedelta/init.md)
- [init(dX: Int32, dY: Int32)](cgscreenupdatemovedelta/init(dx:dy:).md)
### Instance Properties
- [var dX: Int32](cgscreenupdatemovedelta/dx.md)
- [var dY: Int32](cgscreenupdatemovedelta/dy.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CGPSConverter](cgpsconverter.md)
  An opaque data type used to convert PostScript data to PDF data.
- [struct CGCaptureOptions](cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [struct CGConfigureOption](cgconfigureoption.md)
  The scope of the changes in a display configuration transaction.
- [struct CGDeviceColor](cgdevicecolor.md)
- [struct CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md)
  The configuration parameters that are passed to a display reconfiguration callback function.
- [struct CGEventFilterMask](cgeventfiltermask.md)
  Specify masks for classes of low-level events that can be filtered during event suppression states.
- [struct CGEventFlags](cgeventflags.md)
  Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [typealias CGEventTapInformation](cgeventtapinformation.md)
  Defines the structure used to report information about event taps.
- [struct CGScreenUpdateOperation](cgscreenupdateoperation.md)
  Types of screen-update operations.
- [struct CGWindowImageOption](cgwindowimageoption.md)
  The data type to use to specify the type of image to be generated for a window.
- [struct CGWindowListOption](cgwindowlistoption.md)
  The data type used to specify the options for gathering a list of windows.
- [struct CGColorBufferFormat](cgcolorbufferformat.md)
- [struct CGColorDataFormat](cgcolordataformat.md)
- [struct CGPDFAccessPermissions](cgpdfaccesspermissions.md)
- [struct CGPSConverterCallbacks](cgpsconvertercallbacks.md)
  A structure for holding the callbacks provided when you create a PostScript converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgscreenupdatemovedelta)*