# openDefaultApplicationsSettingsURLString

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

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

```c
extern NSString * const UIApplicationOpenDefaultApplicationsSettingsURLString;
```

#### Discussion

Create a URL from this value and pass it to the [`open(_:options:completionHandler:)`](./open%28_,options,completionhandler%29.md) method to launch the Settings app and display your app’s custom settings, if it has any:

**Swift**:

```swift
// Create the URL that links to the Settings app for default app selection.
if let url = URL(string: UIApplication.openDefaultApplicationsSettingsURLString) {
    // Ask the system to open that URL.
    await UIApplication.shared.open(url)
}
```

**Objective-C**:

```objc
// Create the URL that links to the Settings app for default app selection.
NSURL *url = [[NSURL alloc] initWithString:UIApplicationOpenDefaultApplicationsSettingsURLString];
// Ask the system to open that URL.
[[UIApplication sharedApplication] openURL:url
                                   options:@{}
                         completionHandler:nil];
```

For design guidance, see Human Interface Guidelines > [Settings](https://developer.apple.com/design/human-interface-guidelines/).

## See Also

### Deep linking to custom settings
- [class let openSettingsURLString: String](./opensettingsurlstring.md)
  The URL string you use to deep link to your app’s custom settings in the Settings app.
- [static let openNotificationSettingsURLString: String](./opennotificationsettingsurlstring.md)
  The URL string you use to deep link to your app’s notification settings in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/opendefaultapplicationssettingsurlstring)*