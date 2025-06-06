# prepareForActivation()

**Framework**: Group Activities  
**Kind**: method

Returns the participant’s preferred option for how to start the activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func prepareForActivation() async -> GroupActivityActivationResult
```

## Mentions

- [Presenting SharePlay activities from your app’s UI](promoting-shareplay-activities-from-your-apps-ui.md)

#### Return Value

The action to take for the activity. Use this value to determine whether to start an activity locally or as a shared experience.

#### Discussion

Call this method as the first step in starting a group activity, instead of calling the [`activate()`](groupactivity/activate().md) method. Specifically, call this method when the participant tries to start an activity directly from your app’s UI — for example, when they try to watch a movie that’s shareable with a group. This method determines if sharing is possible, and may also prompt the participant to choose whether to start the activity locally or share it with the group.

The system learns over time what activities the user commonly shares, and may not prompt the user in all situations. The system also doesn’t prompt the user if the user disabled activity sharing or isn’t a member of an active group.

## See Also

- [enum GroupActivityActivationResult](groupactivityactivationresult.md)
  The result of preparing to start a custom activity.
- [func activate() async throws -> Bool](groupactivity/activate.md)
  Begins the activity immediately and creates a session for the app when a FaceTime call is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivity/prepareforactivation())*