# SCShareableContentStyle

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

The style of content presented in a stream.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum SCShareableContentStyle
```

```c
enum SCShareableContentStyle : NSInteger;
```

## Topics

### Content styles
- [SCShareableContentStyle.application](./scshareablecontentstyle/application.md)
  The stream is currently presenting one or more applications.
- [SCShareableContentStyle.display](./scshareablecontentstyle/display.md)
  The stream is currently presenting a complete display.
- [SCShareableContentStyle.none](./scshareablecontentstyle/none.md)
  The stream isn’t currently presenting any content.
- [SCShareableContentStyle.window](./scshareablecontentstyle/window.md)
  The stream is currently presenting one or more windows.
### Initializers
- [init?(rawValue: Int)](./scshareablecontentstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Shareable content
- [class SCShareableContent](./scshareablecontent.md)
  An instance that represents a set of displays, apps, and windows that your app can capture.
- [class SCShareableContentInfo](./scshareablecontentinfo.md)
  An instance that provides information for the content in a given stream.
- [class SCDisplay](./scdisplay.md)
  An instance that represents a display device.
- [class SCRunningApplication](./scrunningapplication.md)
  An instance that represents an app running on a device.
- [class SCWindow](./scwindow.md)
  An instance that represents an onscreen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontentstyle)*