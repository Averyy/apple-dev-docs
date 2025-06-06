# SCRunningApplication

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance that represents an app running on a device.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class SCRunningApplication
```

#### Overview

Retrieve the available apps from an instance of [`SCShareableContent`](scshareablecontent.md). Select one or more apps to capture and use them to create an instance of [`SCContentFilter`](sccontentfilter.md). Apply the filter to an instance of [`SCStream`](scstream.md) to limit its output to content matching your criteria.

## Topics

### Inspecting an app
- [var processID: pid_t](scrunningapplication/processid.md)
  The system process identifier of the app.
- [var bundleIdentifier: String](scrunningapplication/bundleidentifier.md)
  The unique bundle identifier of the app.
- [var applicationName: String](scrunningapplication/applicationname.md)
  The display name of the app.

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
- [class SCWindow](scwindow.md)
  An instance that represents an onscreen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scrunningapplication)*