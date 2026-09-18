# containerAppLaunchActivityType

**Framework**: LiveCommunicationKit  
**Kind**: property

The user activity type sent to the container app.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
static let containerAppLaunchActivityType: String
```

#### Discussion

This string is the value of the [`activityType`](https://developer.apple.com/documentation/foundation/nsuseractivity/activitytype) of the [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) sent by the framework when it launches the container app, following a request from the app extension for sign-in or other information. Container apps should validate that the user activity received by [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/swiftui/view/oncontinueuseractivity(_:perform:)) (SwiftUI) or [`application(_:continue:restorationHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:continue:restorationhandler:)) (UIKit) matches this string. If it does, then the user activity’s [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/userinfo) dictionary contains a request id. The container app sends the request id to [`returnToCall(requestID:)`](liveassistance/returntocall(requestid:).md) after it completes logging in or collecting the other needed information from the person using the service.

Your container app also needs to include this string in the app’s information property list, as a member of the `NSUserActivityTypes` array.

## See Also

- [static let containerAppLaunchRequestIDKey: String](liveassistance/containerapplaunchrequestidkey.md)
  A key the container app uses to retrieve a unique identifier for the live assistance request.
- [static let containerAppLaunchReasonKey: String](liveassistance/containerapplaunchreasonkey.md)
  A key the container app uses to retrieve the reason the app extension requested the framework to launch the container app.
- [enum LiveAssistanceLaunchReason](liveassistancelaunchreason.md)
  A type that indicates why the live assistance extension needs to launch its container app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistance/containerapplaunchactivitytype)*