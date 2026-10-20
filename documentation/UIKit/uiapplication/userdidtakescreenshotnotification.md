# userDidTakeScreenshotNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts when a person takes a screenshot on the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let userDidTakeScreenshotNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIApplicationUserDidTakeScreenshotNotification;
```

#### Discussion

This notification doesn’t contain a `userInfo` dictionary. This notification posts after the screenshot is taken.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/userdidtakescreenshotnotification)*