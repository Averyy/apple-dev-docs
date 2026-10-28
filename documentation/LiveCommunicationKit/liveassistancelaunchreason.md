# LiveAssistanceLaunchReason

**Framework**: LiveCommunicationKit  
**Kind**: enum  
**Role**: Enumeration

A type that indicates why the live assistance extension needs to launch its container app.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
enum LiveAssistanceLaunchReason
```

## Overview

You provide this type from your extension in the [`LiveAssistanceRequest.Response.requiresUserInput(reason:)`](./liveassistancerequest/response/requiresuserinput%28reason%29.md) enumeration case. Your container app receives a reason string in the [`userInfo`](../Foundation/nsuseractivity/userinfo.md) of the [`NSUserActivity`](../Foundation/nsuseractivity.md) when the system launches your app. Send this value to `init(rawValue:)` to get an instance of `LiveAssistanceLaunchReason` that your app can act on by comparing it to the defined cases of the enumeration. The string you receive from the user activity is only appropriate for instantiating a `LiveAssistanceLaunchReason` to compare against; it’s not appropriate for use in your user interface.

## Topics

### Working with launch reasons
- [LiveAssistanceLaunchReason.signIn](./liveassistancelaunchreason/signin.md)
  A launch reason that indicates the person using the extension isn’t signed into the VRS provider service.
- [LiveAssistanceLaunchReason.additionalInfo](./liveassistancelaunchreason/additionalinfo.md)
  A launch reason that indicates the person using the extension needs to provide some information not related to authentication.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to a container app launch
- [static let containerAppLaunchActivityType: String](./liveassistance/containerapplaunchactivitytype.md)
  The user activity type sent to the container app.
- [static let containerAppLaunchRequestIDKey: String](./liveassistance/containerapplaunchrequestidkey.md)
  A key the container app uses to retrieve a unique identifier for the live assistance request.
- [static let containerAppLaunchReasonKey: String](./liveassistance/containerapplaunchreasonkey.md)
  A key the container app uses to retrieve the reason the app extension requested the framework to launch the container app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancelaunchreason)*