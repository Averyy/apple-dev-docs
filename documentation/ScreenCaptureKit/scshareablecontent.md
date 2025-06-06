# SCShareableContent

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance that represents a set of displays, apps, and windows that your app can capture.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
class SCShareableContent
```

#### Overview

Use the [`displays`](scshareablecontent/displays.md), [`windows`](scshareablecontent/windows.md), and [`applications`](scshareablecontent/applications.md) properties to create a [`SCContentFilter`](sccontentfilter.md) object that specifies what display content to capture. You apply the filter to an instance of [`SCStream`](scstream.md) to limit its output to only the content matching your filter.

## Topics

### Retrieving shareable content
- [class func getWithCompletionHandler((SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getwithcompletionhandler(_:).md)
  Retrieves the displays, apps, and windows that your app can capture.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnly: Bool, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonly:completionhandler:).md)
  Retrieves the displays, apps, and windows that match your criteria.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyAbove: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonlyabove:completionhandler:).md)
  Retrieves the displays, apps, and windows that are in front of the specified window.
- [class func getExcludingDesktopWindows(Bool, onScreenWindowsOnlyBelow: SCWindow, completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getexcludingdesktopwindows(_:onscreenwindowsonlybelow:completionhandler:).md)
  Retrieves the displays, apps, and windows that are behind the specified window.
- [class func info(for: SCContentFilter) -> SCShareableContentInfo](scshareablecontent/info(for:).md)
  Retrieves any available sharable content information that matches the provided filter.
### Inspecting shareable content
- [var windows: [SCWindow]](scshareablecontent/windows.md)
  The windows available for capture.
- [var displays: [SCDisplay]](scshareablecontent/displays.md)
  The displays available for capture.
- [var applications: [SCRunningApplication]](scshareablecontent/applications.md)
  The apps available for capture.
### Type Methods
- [class func getCurrentProcessShareableContent(completionHandler: (SCShareableContent?, (any Error)?) -> Void)](scshareablecontent/getcurrentprocessshareablecontent(completionhandler:).md)

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

- [class SCShareableContentInfo](scshareablecontentinfo.md)
  An instance that provides information for the content in a given stream.
- [enum SCShareableContentStyle](scshareablecontentstyle.md)
  The style of content presented in a stream.
- [class SCDisplay](scdisplay.md)
  An instance that represents a display device.
- [class SCRunningApplication](scrunningapplication.md)
  An instance that represents an app running on a device.
- [class SCWindow](scwindow.md)
  An instance that represents an onscreen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontent)*