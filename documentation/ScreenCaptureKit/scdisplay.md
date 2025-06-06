# SCDisplay

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance that represents a display device.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class SCDisplay
```

#### Overview

A display object represents a physical display connected to a Mac. Query the display to retrieve its unique identifier and onscreen coordinates.

Retrieve the available displays from an instance of [`SCShareableContent`](scshareablecontent.md). Select a display to capture and use it to create an instance of [`SCContentFilter`](sccontentfilter.md). Apply the filter to an instance of [`SCStream`](scstream.md) to limit its output to content matching your criteria.

## Topics

### Identifying displays
- [var displayID: CGDirectDisplayID](scdisplay/displayid.md)
  The Core Graphics display identifier.
### Accessing dimensions
- [var frame: CGRect](scdisplay/frame.md)
  The frame of the display.
- [var width: Int](scdisplay/width.md)
  The width of the display in points.
- [var height: Int](scdisplay/height.md)
  The height of the display in points.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SCShareableContent](scshareablecontent.md)
  An instance that represents a set of displays, apps, and windows that your app can capture.
- [class SCShareableContentInfo](scshareablecontentinfo.md)
  An instance that provides information for the content in a given stream.
- [enum SCShareableContentStyle](scshareablecontentstyle.md)
  The style of content presented in a stream.
- [class SCRunningApplication](scrunningapplication.md)
  An instance that represents an app running on a device.
- [class SCWindow](scwindow.md)
  An instance that represents an onscreen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scdisplay)*