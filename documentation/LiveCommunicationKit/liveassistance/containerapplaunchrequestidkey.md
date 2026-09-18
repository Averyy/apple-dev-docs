# containerAppLaunchRequestIDKey

**Framework**: LiveCommunicationKit  
**Kind**: property

A key the container app uses to retrieve a unique identifier for the live assistance request.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
static let containerAppLaunchRequestIDKey: String
```

#### Discussion

When launched with the user activity type [`containerAppLaunchReasonKey`](liveassistance/containerapplaunchreasonkey.md), your app retrieves this key from the [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/userinfo) dictionary of the [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) received by the launch method. After your container app finishes performing sign-in or collecting any needed information from the person using the service, your app sends the request id to [`returnToCall(requestID:)`](liveassistance/returntocall(requestid:).md) to return to the FaceTime call and allow your app extension to finish setting up the live assistance service.

## See Also

- [static let containerAppLaunchActivityType: String](liveassistance/containerapplaunchactivitytype.md)
  The user activity type sent to the container app.
- [static let containerAppLaunchReasonKey: String](liveassistance/containerapplaunchreasonkey.md)
  A key the container app uses to retrieve the reason the app extension requested the framework to launch the container app.
- [enum LiveAssistanceLaunchReason](liveassistancelaunchreason.md)
  A type that indicates why the live assistance extension needs to launch its container app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistance/containerapplaunchrequestidkey)*