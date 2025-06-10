# UIApplicationOpenNotificationSettingsURLString

**Framework**: UIKit  
**Kind**: var

A constant that provides the URL string you use to deep link to your app’s notification settings in the Settings app.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
nonisolated
let UIApplicationOpenNotificationSettingsURLString: String
```

#### Discussion

Create a URL from this value and pass it to the [`open(_:options:completionHandler:)`](uiapplication/open(_:options:completionhandler:).md) method to launch the Settings app and display your app’s notification settings, if it has any.

```objc
// Create the URL that deep links to your app's notification settings.
NSURL *url = [[NSURL alloc] initWithString:UIApplicationOpenNotificationSettingsURLString];
// Ask the system to open that URL.
[[UIApplication sharedApplication] openURL:url
                                   options:@{}
                         completionHandler:nil];
```

## See Also

- [class let openSettingsURLString: String](uiapplication/opensettingsurlstring.md)
  The URL string you use to deep link to your app’s custom settings in the Settings app.
- [static let openNotificationSettingsURLString: String](uiapplication/opennotificationsettingsurlstring.md)
  The URL string you use to deep link to your app’s notification settings in the Settings app.
- [class let openDefaultApplicationsSettingsURLString: String](uiapplication/opendefaultapplicationssettingsurlstring.md)
  The URL string used to select a default app in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationopennotificationsettingsurlstring)*