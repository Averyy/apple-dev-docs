# StartWorkoutIntent

**Framework**: App Intents  
**Kind**: protocol

An App Intent for starting a workout.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol StartWorkoutIntent : InstanceDisplayRepresentable, SystemIntent
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)

#### Overview

On Apple Watch Ultra, this intent registers a start workout action for the Action button. After installing your app, the user can select this action in Settings > Action Button by setting Action to Workout and App to your app.

When implementing this intent, define the following:

- A [`title`](appintent/title.md) property
- A [`workoutStyle`](startworkoutintent/workoutstyle-swift.property.md) property
- A list of [`suggestedWorkouts`](startworkoutintent/suggestedworkouts.md)
- A  [`displayRepresentation`](instancedisplayrepresentable/displayrepresentation.md) property
- A [`perform()`](appintent/perform().md) method

```swift
struct MyStartWorkoutIntent: StartWorkoutIntent {

    // Define the intent's title.
    static var title: LocalizedStringResource = "Start Workout"

    // Define a list of start workout intents that appear below the First Press
    // settings when someone sets your app as the workout app in
    // Settings > Action Button.
    static var suggestedWorkouts: [MyStartWorkoutIntent] = [MyStartWorkoutIntent()]

    // Define a parameter that specifies the type of workout that this
    // intent starts.
    @Parameter(title: "Start Workout Entity")
    var workoutStyle: WorkoutEnum

    // Define an init method that sets the default workout type.
    init() {
        workoutStyle = .workout
    }

    // Set the display representation based on the current workout style.
    var displayRepresentation: DisplayRepresentation {
        WorkoutEnum.caseDisplayRepresentations[workoutStyle] ??
        DisplayRepresentation(title: "Unknown")
    }

    // Launch your app when the system triggers this intent.
    static var openAppWhenRun: Bool { true }

    // Define the method that the system calls when it triggers this event.
    func perform() async throws -> some IntentResult {
        let workoutManager = MyWorkoutManager.shared
        await workoutManager.requestAuthorization()
        await workoutManager.startWorkout()
        return .result()
    }
}
```

> ❗ **Important**: When defining the [`workoutStyle`](startworkoutintent/workoutstyle-swift.property.md) property, ensure that it adopts either the [`AppEnum`](appenum.md) or [`AppEntity`](appentity.md) protocol. Declare this property using the [`AppIntent.Parameter`](appintent/parameter.md) property wrapper.

When defining the [`workoutStyle`](startworkoutintent/workoutstyle-swift.property.md) property, ensure that it adopts either the [`AppEnum`](appenum.md) or [`AppEntity`](appentity.md) protocol. Declare this property using the [`AppIntent.Parameter`](appintent/parameter.md) property wrapper.

For more information, see [`Responding to the Action button on Apple Watch Ultra`](actionbuttonarticle.md).

## Topics

### Creating an intent
- [init(style: Self.WorkoutStyle)](startworkoutintent/init(style:).md)
  Creates a new intent for the specified workout style.
### Defining supported workouts
- [associatedtype WorkoutStyle : AppValue](startworkoutintent/workoutstyle-swift.associatedtype.md)
  The type to use for defining the intent’s workout style.
- [var workoutStyle: Self.WorkoutStyle](startworkoutintent/workoutstyle-swift.property.md)
  The workout style for the intent.
- [static var suggestedWorkouts: [Self]](startworkoutintent/suggestedworkouts.md)
  A list of the supported workout styles.
- [static func invalidateSuggestedWorkouts()](startworkoutintent/invalidatesuggestedworkouts.md)
  Tells the system when the list of suggested workouts changes.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SystemIntent](systemintent.md)

## See Also

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
  Use App Intents to register actions for your app.
- [protocol PauseWorkoutIntent](pauseworkoutintent.md)
  An App Intent that lets someone pause your app’s current workout session.
- [protocol ResumeWorkoutIntent](resumeworkoutintent.md)
  An App Intent that lets someone resume your app’s paused workout session.
- [protocol StartDiveIntent](startdiveintent.md)
  An App Intent that lets people start a dive session when they press the Action button on Apple Watch Ultra.
- [struct ConfirmationActionName](confirmationactionname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/startworkoutintent)*