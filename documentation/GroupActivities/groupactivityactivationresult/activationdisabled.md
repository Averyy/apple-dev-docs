# GroupActivityActivationResult.activationDisabled

**Framework**: Group Activities  
**Kind**: case

A result that indicates the user disabled the automatic sharing of activities, or prefers to perform the activity locally.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case activationDisabled
```

#### Discussion

Use the available context to determine the best way to proceed with this action. For example, instead of sharing a movie with a group, configure playback locally on the user’s device. For activities that only make sense in a group environment, you might alert the user that you can’t start the activity.

## See Also

- [GroupActivityActivationResult.activationPreferred](groupactivityactivationresult/activationpreferred.md)
  A result that indicates the user wants to share the activity with the group.
- [GroupActivityActivationResult.cancelled](groupactivityactivationresult/cancelled.md)
  A result that indicates the user canceled the activation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivityactivationresult/activationdisabled)*