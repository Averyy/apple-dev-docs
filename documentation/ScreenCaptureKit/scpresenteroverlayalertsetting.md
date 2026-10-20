# SCPresenterOverlayAlertSetting

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

Configures how to present streaming notifications to a streamer of Presenter Overlay.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
enum SCPresenterOverlayAlertSetting
```

```c
enum SCPresenterOverlayAlertSetting : NSInteger;
```

## Topics

### Alerting Presenters
- [SCPresenterOverlayAlertSetting.always](./scpresenteroverlayalertsetting/always.md)
  Always display an alert when using Presenter Overlay.
- [SCPresenterOverlayAlertSetting.never](./scpresenteroverlayalertsetting/never.md)
  Never display an alert when using Presenter Overlay.
- [SCPresenterOverlayAlertSetting.system](./scpresenteroverlayalertsetting/system.md)
  Displays an alert when using Presenter Overlay based on the System Settings.
### Initializers
- [init?(rawValue: Int)](./scpresenteroverlayalertsetting/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Notifying presenters
- [var presenterOverlayPrivacyAlertSetting: SCPresenterOverlayAlertSetting](./scstreamconfiguration/presenteroverlayprivacyalertsetting.md)
  A value indicating if alerts appear to presenters while using Presenter Overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scpresenteroverlayalertsetting)*