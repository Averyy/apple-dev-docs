# ResumeWorkoutIntent

**Framework**: App Intents  
**Kind**: protocol

An App Intent that lets someone resume your app’s paused workout session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol ResumeWorkoutIntent : SystemIntent
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)

#### Overview

On Apple Watch Ultra, someone can resume your app’s workout by simultaneously pressing the Action button and the side button when your app has a paused workout session.

To implement the resume action, create a structure that adopts the `ResumeWorkoutIntent` protocol.

```swift
struct MyResumeWorkoutIntent: ResumeWorkoutIntent {
    static var title: LocalizedStringResource = "Resume Workout"

    func perform() async throws -> some IntentResult {
        logger.debug("*** Performing a resume intent. ***")
        await MyWorkoutManager.shared.resumeWorkout()
        return .result()
    }
}
```

This intent needs a [`title`](appintent/title.md) property that provides a localized description of the action, and a [`perform()`](appintent/perform().md) method, which the system calls when it triggers the intent.

For more information, see [`Responding to the Action button on Apple Watch Ultra`](actionbuttonarticle.md).

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
  Use App Intents to register actions for your app.
- [protocol StartWorkoutIntent](startworkoutintent.md)
  An App Intent for starting a workout.
- [protocol PauseWorkoutIntent](pauseworkoutintent.md)
  An App Intent that lets someone pause your app’s current workout session.
- [protocol StartDiveIntent](startdiveintent.md)
  An App Intent that lets people start a dive session when they press the Action button on Apple Watch Ultra.
- [struct ConfirmationActionName](confirmationactionname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resumeworkoutintent)*