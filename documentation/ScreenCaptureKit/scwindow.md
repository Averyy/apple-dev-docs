# SCWindow

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance that represents an onscreen window.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class SCWindow
```

#### Overview

Retrieve the available windows from an instance of [`SCShareableContent`](scshareablecontent.md). Select one or more windows to capture and use them to create an instance of [`SCContentFilter`](sccontentfilter.md). Apply the filter to an instance of [`SCStream`](scstream.md) to limit its output to content matching your criteria.

## Topics

### Identifying windows
- [var windowID: CGWindowID](scwindow/windowid.md)
  The Core Graphics window identifier.
- [var title: String?](scwindow/title.md)
  The string that displays in a window’s title bar.
- [var owningApplication: SCRunningApplication?](scwindow/owningapplication.md)
  The app that owns the window.
- [var windowLayer: Int](scwindow/windowlayer.md)
  The layer of the window relative to other windows.
### Accessing dimensions
- [var frame: CGRect](scwindow/frame.md)
  A rectangle the represents the frame of the window within a display.
### Determining visibility
- [var isOnScreen: Bool](scwindow/isonscreen.md)
  A Boolean value that indicates whether the window is on screen.
- [var isActive: Bool](scwindow/isactive.md)
  A Boolean value that indicates if the window is currently streaming.

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
- [class SCDisplay](scdisplay.md)
  An instance that represents a display device.
- [class SCRunningApplication](scrunningapplication.md)
  An instance that represents an app running on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scwindow)*