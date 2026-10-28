# openNotificationSettingsURLString

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The URL string you use to deep link to your app’s notification settings in the Settings app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS
- visionOS

## Declaration

```swift
nonisolated
static let openNotificationSettingsURLString: String
```

## Discussion

Create a URL from this value and pass it to the [`open(_:options:completionHandler:)`](./open%28_,options,completionhandler%29.md) method to launch the Settings app and display your app’s notification settings, if it has any.

```swift
// Create the URL that deep links to your app's notification settings.
if let url = URL(string: UIApplication.openNotificationSettingsURLString) {
    // Ask the system to open that URL.
    await UIApplication.shared.open(url)
}
```

## See Also

### Deep linking to custom settings
- [class let openSettingsURLString: String](./opensettingsurlstring.md)
  The URL string you use to deep link to your app’s custom settings in the Settings app.
- [class let openDefaultApplicationsSettingsURLString: String](./opendefaultapplicationssettingsurlstring.md)
  The URL string used to select a default app in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/opennotificationsettingsurlstring)*