# SCPresenterOverlayAlertSetting

**Framework**: ScreenCaptureKit  
**Kind**: enum

Configures how to present streaming notifications to a streamer of Presenter Overlay.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
enum SCPresenterOverlayAlertSetting
```

## Topics

### Alerting Presenters
- [SCPresenterOverlayAlertSetting.always](scpresenteroverlayalertsetting/always.md)
  Always display an alert when using Presenter Overlay.
- [SCPresenterOverlayAlertSetting.never](scpresenteroverlayalertsetting/never.md)
  Never display an alert when using Presenter Overlay.
- [SCPresenterOverlayAlertSetting.system](scpresenteroverlayalertsetting/system.md)
  Displays an alert when using Presenter Overlay based on the System Settings.
### Initializers
- [init?(rawValue: Int)](scpresenteroverlayalertsetting/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var presenterOverlayPrivacyAlertSetting: SCPresenterOverlayAlertSetting](scstreamconfiguration/presenteroverlayprivacyalertsetting.md)
  A value indicating if alerts appear to presenters while using Presenter Overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scpresenteroverlayalertsetting)*