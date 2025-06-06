# openDefaultApplicationsSettingsURLString

**Framework**: UIKit  
**Kind**: property

The URL string used to select a default app in the Settings app.

**Availability**:
- iOS 18.3+
- iPadOS 18.3+
- Mac Catalyst 18.3+
- tvOS 18.3+
- visionOS 2.3+

## Declaration

```swift
nonisolated
class let openDefaultApplicationsSettingsURLString: String
```

#### Discussion

Create a URL from this value and pass it to the [`open(_:options:completionHandler:)`](uiapplication/open(_:options:completionhandler:).md) method to launch the Settings app and display your app’s custom settings, if it has any:

For design guidance, see Human Interface Guidelines > [`Settings`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/).

## See Also

- [class let openSettingsURLString: String](uiapplication/opensettingsurlstring.md)
  The URL string you use to deep link to your app’s custom settings in the Settings app.
- [static let openNotificationSettingsURLString: String](uiapplication/opennotificationsettingsurlstring.md)
  The URL string you use to deep link to your app’s notification settings in the Settings app.
- [let UIApplicationOpenNotificationSettingsURLString: String](uiapplicationopennotificationsettingsurlstring.md)
  A constant that provides the URL string you use to deep link to your app’s notification settings in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/opendefaultapplicationssettingsurlstring)*