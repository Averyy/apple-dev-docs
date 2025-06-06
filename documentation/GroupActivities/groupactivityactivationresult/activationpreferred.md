# GroupActivityActivationResult.activationPreferred

**Framework**: Group Activities  
**Kind**: case

A result that indicates the user wants to share the activity with the group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case activationPreferred
```

#### Discussion

When you receive this result in your completion handler, call the [`activate()`](groupactivity/activate().md) method of your [`GroupActivity`](groupactivity.md) type to advertise the activity to other participants in the group.

## See Also

- [GroupActivityActivationResult.activationDisabled](groupactivityactivationresult/activationdisabled.md)
  A result that indicates the user disabled the automatic sharing of activities, or prefers to perform the activity locally.
- [GroupActivityActivationResult.cancelled](groupactivityactivationresult/cancelled.md)
  A result that indicates the user canceled the activation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivityactivationresult/activationpreferred)*