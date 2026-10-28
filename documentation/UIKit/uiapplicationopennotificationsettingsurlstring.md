# UIApplicationOpenNotificationSettingsURLString

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A constant that provides the URL string you use to deep link to your app’s notification settings in the Settings app.

**Availability**:
- iOS 15.4+ - Deprecated in 16.0
- iPadOS 15.4+ - Deprecated in 16.0
- Mac Catalyst 15.4+ - Deprecated in 16.0
- tvOS 15.4+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 8.5+ - Deprecated in 9.0

> **Deprecated**: In Swift, use [`openNotificationSettingsURLString`](./uiapplication/opennotificationsettingsurlstring.md) instead.

## Declaration

```swift
nonisolated
let UIApplicationOpenNotificationSettingsURLString: String
```

```c
extern NSString * const UIApplicationOpenNotificationSettingsURLString;
```

## Discussion

Create a URL from this value and pass it to the [`open(_:options:completionHandler:)`](./uiapplication/open%28_,options,completionhandler%29.md) method to launch the Settings app and display your app’s notification settings, if it has any.

```objc
// Create the URL that deep links to your app's notification settings.
NSURL *url = [[NSURL alloc] initWithString:UIApplicationOpenNotificationSettingsURLString];
// Ask the system to open that URL.
[[UIApplication sharedApplication] openURL:url
                                   options:@{}
                         completionHandler:nil];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationopennotificationsettingsurlstring)*