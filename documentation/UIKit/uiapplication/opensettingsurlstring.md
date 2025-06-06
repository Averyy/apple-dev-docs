# openSettingsURLString

**Framework**: UIKit  
**Kind**: property

The URL string you use to deep link to your app’s custom settings in the Settings app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let openSettingsURLString: String
```

#### Discussion

Create a URL from this value and pass it to the [`open(_:options:completionHandler:)`](uiapplication/open(_:options:completionhandler:).md) method to launch the Settings app and display your app’s custom settings, if it has any.

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/settings/).

## See Also

- [static let openNotificationSettingsURLString: String](uiapplication/opennotificationsettingsurlstring.md)
  The URL string you use to deep link to your app’s notification settings in the Settings app.
- [let UIApplicationOpenNotificationSettingsURLString: String](uiapplicationopennotificationsettingsurlstring.md)
  A constant that provides the URL string you use to deep link to your app’s notification settings in the Settings app.
- [class let openDefaultApplicationsSettingsURLString: String](uiapplication/opendefaultapplicationssettingsurlstring.md)
  The URL string used to select a default app in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/opensettingsurlstring)*