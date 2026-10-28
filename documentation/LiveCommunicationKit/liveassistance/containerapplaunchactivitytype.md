# containerAppLaunchActivityType

**Framework**: LiveCommunicationKit  
**Kind**: property  
**Role**: Type Property

The user activity type sent to the container app.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
static let containerAppLaunchActivityType: String
```

## Discussion

This string is the value of the [`activityType`](../../Foundation/nsuseractivity/activitytype.md) of the [`NSUserActivity`](../../Foundation/nsuseractivity.md) sent by the framework when it launches the container app, following a request from the app extension for sign-in or other information. Container apps should validate that the user activity received by [`onContinueUserActivity(_:perform:)`](../../SwiftUI/view/oncontinueuseractivity%28_,perform%29.md) (SwiftUI) or [`application(_:continue:restorationHandler:)`](../../UIKit/uiapplicationdelegate/application%28_,continue,restorationhandler%29.md) (UIKit) matches this string. If it does, then the user activity’s [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary contains a request id. The container app sends the request id to [`returnToCall(requestID:)`](./returntocall%28requestid%29.md) after it completes logging in or collecting the other needed information from the person using the service.

Your container app also needs to include this string in the app’s information property list, as a member of the `NSUserActivityTypes` array.

## See Also

### Responding to a container app launch
- [static let containerAppLaunchRequestIDKey: String](./containerapplaunchrequestidkey.md)
  A key the container app uses to retrieve a unique identifier for the live assistance request.
- [static let containerAppLaunchReasonKey: String](./containerapplaunchreasonkey.md)
  A key the container app uses to retrieve the reason the app extension requested the framework to launch the container app.
- [enum LiveAssistanceLaunchReason](../liveassistancelaunchreason.md)
  A type that indicates why the live assistance extension needs to launch its container app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistance/containerapplaunchactivitytype)*