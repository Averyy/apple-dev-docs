# LiveAssistanceLaunchReason

**Framework**: LiveCommunicationKit  
**Kind**: enum

A type that indicates why the live assistance extension needs to launch its container app.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
enum LiveAssistanceLaunchReason
```

#### Overview

You provide this type from your extension in the [`LiveAssistanceRequest.Response.requiresUserInput(reason:)`](liveassistancerequest/response/requiresuserinput(reason:).md) enumeration case. Your container app receives a reason string in the [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/userinfo) of the [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) when the system launches your app. Send this value to `init(rawValue:)` to get an instance of `LiveAssistanceLaunchReason` that your app can act on by comparing it to the defined cases of the enumeration. The string you receive from the user activity is only appropriate for instantiating a `LiveAssistanceLaunchReason` to compare against; it’s not appropriate for use in your user interface.

## Topics

### Working with launch reasons
- [LiveAssistanceLaunchReason.signIn](liveassistancelaunchreason/signin.md)
  A launch reason that indicates the person using the extension isn’t signed into the VRS provider service.
- [LiveAssistanceLaunchReason.additionalInfo](liveassistancelaunchreason/additionalinfo.md)
  A launch reason that indicates the person using the extension needs to provide some information not related to authentication.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static let containerAppLaunchActivityType: String](liveassistance/containerapplaunchactivitytype.md)
  The user activity type sent to the container app.
- [static let containerAppLaunchRequestIDKey: String](liveassistance/containerapplaunchrequestidkey.md)
  A key the container app uses to retrieve a unique identifier for the live assistance request.
- [static let containerAppLaunchReasonKey: String](liveassistance/containerapplaunchreasonkey.md)
  A key the container app uses to retrieve the reason the app extension requested the framework to launch the container app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancelaunchreason)*