# SCShareableContentStyle

**Framework**: ScreenCaptureKit  
**Kind**: enum

The style of content presented in a stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
enum SCShareableContentStyle
```

## Topics

### Content styles
- [SCShareableContentStyle.application](scshareablecontentstyle/application.md)
  The stream is currently presenting one or more applications.
- [SCShareableContentStyle.display](scshareablecontentstyle/display.md)
  The stream is currently presenting a complete display.
- [SCShareableContentStyle.none](scshareablecontentstyle/none.md)
  The stream isn’t currently presenting any content.
- [SCShareableContentStyle.window](scshareablecontentstyle/window.md)
  The stream is currently presenting one or more windows.
### Initializers
- [init?(rawValue: Int)](scshareablecontentstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class SCShareableContent](scshareablecontent.md)
  An instance that represents a set of displays, apps, and windows that your app can capture.
- [class SCShareableContentInfo](scshareablecontentinfo.md)
  An instance that provides information for the content in a given stream.
- [class SCDisplay](scdisplay.md)
  An instance that represents a display device.
- [class SCRunningApplication](scrunningapplication.md)
  An instance that represents an app running on a device.
- [class SCWindow](scwindow.md)
  An instance that represents an onscreen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontentstyle)*