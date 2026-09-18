# containerAppLaunchReasonKey

**Framework**: LiveCommunicationKit  
**Kind**: property

A key the container app uses to retrieve the reason the app extension requested the framework to launch the container app.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
static let containerAppLaunchReasonKey: String
```

#### Discussion

When launched with the user activity type [`containerAppLaunchReasonKey`](liveassistance/containerapplaunchreasonkey.md), your app retrieves this key from the [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/userinfo) dictionary of the [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) received by the launch method. The value is a string that you pass to `LiveAssistanceLaunchReason(rawValue:)` to create an instance of the [`LiveAssistanceLaunchReason`](liveassistancelaunchreason.md) enumeration. Compare this instance against the defined cases in the enumeration to determine why the container app launched, such as to perform sign-in or to collect further information or approval. The string you receive from the user activity is only appropriate for instantiating a [`LiveAssistanceLaunchReason`](liveassistancelaunchreason.md) to compare against; it’s not appropriate for use in your user interface.

## See Also

- [static let containerAppLaunchActivityType: String](liveassistance/containerapplaunchactivitytype.md)
  The user activity type sent to the container app.
- [static let containerAppLaunchRequestIDKey: String](liveassistance/containerapplaunchrequestidkey.md)
  A key the container app uses to retrieve a unique identifier for the live assistance request.
- [enum LiveAssistanceLaunchReason](liveassistancelaunchreason.md)
  A type that indicates why the live assistance extension needs to launch its container app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistance/containerapplaunchreasonkey)*