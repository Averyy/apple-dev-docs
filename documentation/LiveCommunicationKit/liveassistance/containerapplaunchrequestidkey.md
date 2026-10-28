# containerAppLaunchRequestIDKey

**Framework**: LiveCommunicationKit  
**Kind**: property  
**Role**: Type Property

A key the container app uses to retrieve a unique identifier for the live assistance request.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
static let containerAppLaunchRequestIDKey: String
```

## Discussion

When launched with the user activity type [`containerAppLaunchReasonKey`](./containerapplaunchreasonkey.md), your app retrieves this key from the [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary of the [`NSUserActivity`](../../Foundation/nsuseractivity.md) received by the launch method. After your container app finishes performing sign-in or collecting any needed information from the person using the service, your app sends the request id to [`returnToCall(requestID:)`](./returntocall%28requestid%29.md) to return to the FaceTime call and allow your app extension to finish setting up the live assistance service.

## See Also

### Responding to a container app launch
- [static let containerAppLaunchActivityType: String](./containerapplaunchactivitytype.md)
  The user activity type sent to the container app.
- [static let containerAppLaunchReasonKey: String](./containerapplaunchreasonkey.md)
  A key the container app uses to retrieve the reason the app extension requested the framework to launch the container app.
- [enum LiveAssistanceLaunchReason](../liveassistancelaunchreason.md)
  A type that indicates why the live assistance extension needs to launch its container app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistance/containerapplaunchrequestidkey)*