# presenterOverlayPrivacyAlertSetting

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A value indicating if alerts appear to presenters while using Presenter Overlay.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
var presenterOverlayPrivacyAlertSetting: SCPresenterOverlayAlertSetting { get set }
```

```objc
@property (nonatomic, assign) SCPresenterOverlayAlertSetting presenterOverlayPrivacyAlertSetting;
```

#### Discussion

The default value is [`SCPresenterOverlayAlertSetting.system`](../scpresenteroverlayalertsetting/system.md).

## See Also

### Notifying presenters
- [enum SCPresenterOverlayAlertSetting](../scpresenteroverlayalertsetting.md)
  Configures how to present streaming notifications to a streamer of Presenter Overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/presenteroverlayprivacyalertsetting)*