# openSettingsURLString

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The URL string you use to deep link to your app’s custom settings in the Settings app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let openSettingsURLString: String
```

```c
extern NSString * const UIApplicationOpenSettingsURLString;
```

#### Discussion

Create a URL from this value and pass it to the [`open(_:options:completionHandler:)`](./open%28_,options,completionhandler%29.md) method to launch the Settings app and display your app’s custom settings, if it has any.

**Swift**:

```swift
// Create the URL that deep links to your app's custom settings.
if let url = URL(string: UIApplication.openSettingsURLString) {
    // Ask the system to open that URL.
    await UIApplication.shared.open(url)
}
```

**Objective-C**:

```objc
// Create the URL that deep links to your app's custom settings.
NSURL *url = [[NSURL alloc] initWithString:UIApplicationOpenSettingsURLString];
// Ask the system to open that URL.
[[UIApplication sharedApplication] openURL:url
                                   options:@{}
                         completionHandler:nil];
```

For design guidance, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/settings/).

## See Also

### Deep linking to custom settings
- [static let openNotificationSettingsURLString: String](./opennotificationsettingsurlstring.md)
  The URL string you use to deep link to your app’s notification settings in the Settings app.
- [class let openDefaultApplicationsSettingsURLString: String](./opendefaultapplicationssettingsurlstring.md)
  The URL string used to select a default app in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/opensettingsurlstring)*