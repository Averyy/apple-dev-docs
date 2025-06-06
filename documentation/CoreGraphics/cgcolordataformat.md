# CGColorDataFormat

**Framework**: Core Graphics  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CGColorDataFormat
```

## Topics

### Initializers
- [init()](cgcolordataformat/init.md)
- [init(version: UInt32, colorspace_info: Unmanaged<CFTypeRef>!, bitmap_info: CGBitmapInfo, bits_per_component: Int, bytes_per_row: Int, intent: CGColorRenderingIntent, decode: UnsafeMutablePointer<CGFloat>!)](cgcolordataformat/init(version:colorspace_info:bitmap_info:bits_per_component:bytes_per_row:intent:decode:).md)
### Instance Properties
- [var bitmap_info: CGBitmapInfo](cgcolordataformat/bitmap_info.md)
- [var bits_per_component: Int](cgcolordataformat/bits_per_component.md)
- [var bytes_per_row: Int](cgcolordataformat/bytes_per_row.md)
- [var colorspace_info: Unmanaged<CFTypeRef>!](cgcolordataformat/colorspace_info.md)
- [var decode: UnsafeMutablePointer<CGFloat>!](cgcolordataformat/decode.md)
- [var intent: CGColorRenderingIntent](cgcolordataformat/intent.md)
- [var version: UInt32](cgcolordataformat/version.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

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
- [struct CGScreenUpdateMoveDelta](cgscreenupdatemovedelta.md)
  The distance, in pixel units, that an onscreen region moves.
- [struct CGScreenUpdateOperation](cgscreenupdateoperation.md)
  Types of screen-update operations.
- [struct CGWindowImageOption](cgwindowimageoption.md)
  The data type to use to specify the type of image to be generated for a window.
- [struct CGWindowListOption](cgwindowlistoption.md)
  The data type used to specify the options for gathering a list of windows.
- [struct CGColorBufferFormat](cgcolorbufferformat.md)
- [struct CGPDFAccessPermissions](cgpdfaccesspermissions.md)
- [struct CGPSConverterCallbacks](cgpsconvertercallbacks.md)
  A structure for holding the callbacks provided when you create a PostScript converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolordataformat)*