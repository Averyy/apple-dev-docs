# StartDiveIntent

**Framework**: App Intents  
**Kind**: protocol

An App Intent that lets people start a dive session when they press the Action button on Apple Watch Ultra.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
protocol StartDiveIntent : SystemIntent
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)

#### Overview

To implement the start dive action, create a structure that adopts the `StartDiveIntent` protocol.

```swift
struct MyStartDiveIntent: StartDiveIntent {

    static var title: LocalizedStringResource = "Starting a dive session."

    func perform() async throws -> some IntentResult {
        logger.debug("*** Starting a dive session. ***")

        await DiveManager.shared.start()
        return .result(actionButtonIntent: StartDive())
    }
}
```

This intent needs a [`title`](appintent/title.md) property that provides a localized description of the action, and a [`perform()`](appintent/perform().md) method, which the system calls when it triggers the intent.

To read live depth, water pressure, and water temperature data, see [`Accessing submersion data`](https://developer.apple.com/documentation/CoreMotion/accessing-submersion-data).

> ❗ **Important**: Before you can access live dive data, your app needs to include an entitlement to access submersion data. For more information, see [`Express interest in the Submerged Depth and Pressure API`](https://developer.apple.comhttps://developer.apple.com/contact/request/submerged-depth-pressure-api/).

Before you can access live dive data, your app needs to include an entitlement to access submersion data. For more information, see [`Express interest in the Submerged Depth and Pressure API`](https://developer.apple.comhttps://developer.apple.com/contact/request/submerged-depth-pressure-api/).

For more information, see [`Responding to the Action button on Apple Watch Ultra`](actionbuttonarticle.md).

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SystemIntent](systemintent.md)

## See Also

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
  Use App Intents to register actions for your app.
- [protocol StartWorkoutIntent](startworkoutintent.md)
  An App Intent for starting a workout.
- [protocol PauseWorkoutIntent](pauseworkoutintent.md)
  An App Intent that lets someone pause your app’s current workout session.
- [protocol ResumeWorkoutIntent](resumeworkoutintent.md)
  An App Intent that lets someone resume your app’s paused workout session.
- [struct ConfirmationActionName](confirmationactionname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/startdiveintent)*