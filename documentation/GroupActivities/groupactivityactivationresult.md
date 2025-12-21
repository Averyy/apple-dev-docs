# GroupActivityActivationResult

**Framework**: Group Activities  
**Kind**: enum

The result of preparing to start a custom activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum GroupActivityActivationResult
```

#### Overview

When you call [`prepareForActivation()`](groupactivity/prepareforactivation().md), the system determines whether you share the activity with other participants in a FaceTime call, or perform it locally. After making the determination, it passes a `GroupActivityActivationResult` value to the method’s completion handler. Use that value to start the activity in the selected setting.

## Topics

### Getting the activation results
- [GroupActivityActivationResult.activationPreferred](groupactivityactivationresult/activationpreferred.md)
  A result that indicates the user wants to share the activity with the group.
- [GroupActivityActivationResult.activationDisabled](groupactivityactivationresult/activationdisabled.md)
  A result that indicates the user disabled the automatic sharing of activities, or prefers to perform the activity locally.
- [GroupActivityActivationResult.cancelled](groupactivityactivationresult/cancelled.md)
  A result that indicates the user canceled the activation request.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Defining your app’s SharePlay activities](defining-your-apps-shareplay-activities.md)
  Configure your app’s SharePlay support and define the activities that people can perform from your app.
- [Supporting coordinated media playback](../AVFoundation/supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [protocol GroupActivity](groupactivity.md)
  A type that can advertise your app’s activities to other participants.
- [struct GroupActivityMetadata](groupactivitymetadata.md)
  Text and image content that describes an activity to potential participants.
- [struct GroupActivityTransferRepresentation](groupactivitytransferrepresentation.md)
  A type that lets you start a group activity from a known context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivityactivationresult)*