# init(originator:action:url:)

**Framework**: Group Activities  
**Kind**: init

Creates a new event with the specified participant and action details.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(originator: Participant, action: GroupSessionEvent.Action, url: URL?)
```

## Parameters

- `originator`: The participant that initiated the event.
- `action`: The action to report for the event. The system uses this   value to generate a localized description of the action in the system UI.
- `url`: The location in your app where the action occurred. Specify a   universal link into your app that takes the participant to the action   details. Specify   to bring your app to the foreground   without navigating to a specific location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/init(originator:action:url:))*