# activate()

**Framework**: Group Activities  
**Kind**: method

Begins the activity immediately and creates a session for the app when a FaceTime call is active.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func activate() async throws -> Bool
```

## Mentions

- [Presenting SharePlay activities from your app’s UI](promoting-shareplay-activities-from-your-apps-ui.md)

#### Discussion

Typically, you call this method only when the [`prepareForActivation()`](groupactivity/prepareforactivation().md) method delivers the [`GroupActivityActivationResult.activationPreferred`](groupactivityactivationresult/activationpreferred.md) result. However, you may call it directly if your activity only makes sense in a group setting. For example, call it if the activity applies only to groups and can’t be performed without other participants.

If a FaceTime call is active, this method configures a session. The system also invites other participants to join the activity. If a session will be delivered to your app this function returns true, otherwise it returns false. A case where this function could return false is when a session is created and handed off to an Apple TV. If a call isn’t active or a session wasn’t created, this method throws an error

## See Also

- [func prepareForActivation() async -> GroupActivityActivationResult](groupactivity/prepareforactivation.md)
  Returns the participant’s preferred option for how to start the activity.
- [enum GroupActivityActivationResult](groupactivityactivationresult.md)
  The result of preparing to start a custom activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivity/activate())*