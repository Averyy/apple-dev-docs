# Responding to the Action button on Apple Watch Ultra

**Framework**: Appintents

Use App Intents to register actions for your app.

#### Overview

On Apple Watch Ultra, people can specify the action that the system triggers when they press the Action button. By default, the watch provides actions for starting workouts, starting dives, starting a backtrack navigation session, setting a waypoint, turning on the flashlight, and running a shortcut from the Shortcuts app. To add your dive or workout app to the list of apps that appear when someone chooses Settings > Action Button, use App Intents to register actions for your app.

For workout apps, you can implement the following protocols:

For dive apps, you can implement the following protocols:

> ❗ **Important**: When creating intents for the Action button, don’t implement them in an [`AppIntentsExtension`](appintentsextension.md). Always implement the intents directly in your watchOS app.

##### Start a New Workout Session

Start by creating either an [`AppEnum`](appenum.md) or an [`AppEntity`](appentity.md) that defines the types of workouts that your app supports. If your app supports only a single workout, you can create an enumeration with a single case. Also define the display representation for each type of workout that your app supports. Apple Watch Ultra shows the case description’s title and subtitle below the First Press settings when someone sets your app as the workout app in Settings > Action Button.

```swift
enum WorkoutEnum: String, AppEnum {
    
    // List the types of workout your app supports.
    case running

    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Workout"

    // Define the display representation for each of the workouts your app supports.
    static var caseDisplayRepresentations: [WorkoutEnum: DisplayRepresentation] =
    [.running: DisplayRepresentation(title: "Running", subtitle: "outside run")]
}
```

Next, create a structure that adopts the [`StartWorkoutIntent`](startworkoutintent.md) protocol. Your implementation needs to define the intent’s [`title`](appintent/title.md), a list of [`suggestedWorkouts`](startworkoutintent/suggestedworkouts.md), and a parameter that contains the [`workoutStyle`](startworkoutintent/workoutstyle-swift.property.md).

```swift
struct MyStartWorkoutIntent: StartWorkoutIntent {

    // Define the intent's title.
    static var title: LocalizedStringResource = "Start Workout"
    
    // Define a list of start workout intents that appear below the First Press settings when someone sets your app as the workout app in Settings > Action Button.

    static var suggestedWorkouts: [MyStartWorkoutIntent] = [MyStartWorkoutIntent()]

    // Define a parameter that specifies the type of workout that this intent starts.
    @Parameter(title: "Type of Workout")
    var workoutStyle: WorkoutEnum

    // Define an init method that sets the default workout type.
    init() {
        workoutStyle = .workout
    }

    // Add the display representation, and the perform method here.
}
```

> ❗ **Important**: Define your implementation’s `workoutStyle` property using the [`AppIntent.Parameter`](appintent/parameter.md) property wrapper.

You can dynamically change the list of suggested workouts by changing the value of the [`suggestedWorkouts`](startworkoutintent/suggestedworkouts.md) property and then calling [`invalidateSuggestedWorkouts()`](startworkoutintent/invalidatesuggestedworkouts().md), which tells the system to reread the suggested workouts.

Next, set the display strings for the intent by defining the `displayRepresentation` just after the intent’s initializer.

```swift
var displayRepresentation: DisplayRepresentation {
    WorkoutEnum.caseDisplayRepresentations[workoutStyle] ??
    DisplayRepresentation(title: "Unknown")
}
```

Then, implement your intent’s [`perform()`](appintent/perform().md) method. The system calls this method when anything triggers the intent. In your implementation, you have 30 seconds to start a workout session and return a successful value. If you don’t start a workout session in that time, the system displays an error message, but the app remains in the foreground. People can start a workout session directly from the app, but without a session, the app goes to the background the next time they drop their wrist.

```swift
// Define the method that the system calls when it triggers the intent.
func perform() async throws -> some IntentResult {
    logger.debug("*** Performing a Start Intent. ***")
    
    // Start a workout session inside the perform method.
    let workoutManager = MyWorkoutManager.shared
    try await workoutManager.startWorkout(type: workoutStyle)
    
    // Schedule a task to request authorization and then set up the data source and start collecting data from the workout.
    Task {
        await workoutManager.requestAuthorization()
        
        do {
            try await workoutManager.startCollectingData()
        } catch {
            fatalError("*** An error occurred while setting up the data source: \(error.localizedDescription) ***")
        }
    }
    
    // Return a successful result.
    return .result()
}
```

The start workout intent becomes available as soon as someone downloads your app. This means they can set up the Action button and run your start workout intent without ever launching your app.

Similarly, if you update your app and change the data types that the workout session uses, someone can launch the updated workout from the Action button without launching your app.

To ensure that your app requests authorization for the current set of HealthKit data types it intends to use during its workout sessions, you need to schedule an authorization request from within your intent’s [`perform()`](appintent/perform().md) method. Because someone using your app doesn’t have access to its user interface until after the `perform()` method returns, you need to schedule the request authorization using a [`Task`](https://developer.apple.com/documentation/Swift/Task).

> **Note**: If your app has never requested authorization for any HealthKit data types, the system just launches your app when someone presses the Action button. It doesn’t call your intent’s [`perform()`](appintent/perform().md) method.

Before authorizing the HealthKit data, create and start your workout session.

```swift
func startWorkout(type: WorkoutEnum) throws {
    logger.debug("*** Start a workout of type \(type.rawValue) ***")
    
    logger.debug("==> Creating the workout configuration.")
    let configuration = HKWorkoutConfiguration()
    configuration.activityType = .running
    configuration.locationType = .outdoor
    
    self.configuration = configuration
    
    logger.debug("==> Creating the workout session.")
    let session = try HKWorkoutSession(healthStore: store, configuration: configuration)
    
    session.delegate = self
    self.session = session
    workoutType = type
    
    logger.debug("==> Starting the session.")
    session.startActivity(with: Date())
}
```

The code example above creates a workout configuration for an outdoor run. It then uses the configuration to create the workout session, assigns a workout session delegate to receive state change and errors from the workout, and starts the session.

Because the app hasn’t created a data source for the workout session, the session doesn’t generate any data.

Next, request authorization for all the HealthKit data types that your workout sessions use.

```swift
func requestAuthorization1() async {
    logger.debug("*** Requesting Authorization ***")
    
    // The quantity type to write to the health store.
    let typesToShare: Set = [
        HKQuantityType.workoutType()
    ]

    // The quantity types to read from the health store.
    let typesToRead: Set = [
        HKQuantityType(.heartRate),
        HKQuantityType(.activeEnergyBurned),
        HKQuantityType(.distanceWalkingRunning)
    ]
    
    guard HKHealthStore.isHealthDataAvailable() else {
        logger.debug("*** HealthKit is not supported on this device. ***")
        return
    }
    
    do {
        try await store.requestAuthorization(toShare: typesToShare, read: typesToRead)
    } catch {
        fatalError("*** An error occurred while requesting authorization to read and save data: \(error.localizedDescription) ***")
    }

    enabled = true
}
```

This authorization request can take an arbitrarily long amount of time. Any time you request authorization for new data, the system displays an authorization sheet, and waits until someone either authorizes the data or dismisses the sheet. However, if someone has already authorized the requested data types, the system returns immediately.

After the authorization request finishes, set up the data source, assign a delegate to receive data from the workout builder, and begin collecting data from the workout.

```swift
func startCollectingData() async throws {
    precondition(enabled == true)
    guard let configuration else { fatalError("*** You need to create a workout configuration before calling this method. ***") }
    guard let session else { fatalError("*** You need to create a session before calling this method. ***") }
    
    logger.debug("==> Setting the session's data source.")
    let builder = session.associatedWorkoutBuilder()
    builder.dataSource = HKLiveWorkoutDataSource(healthStore: store,
                                                 workoutConfiguration: configuration)
    
    builder.delegate = self
    
    logger.debug("==> Begin collecting data.")
    try await builder.beginCollection(at: Date())
    
    self.builder = builder

    logger.debug("==> Donate the mark lap intent as the Action button's next action.")
    try await MyStartWorkoutIntent().donate(result: .result(actionButtonIntent: MyMarkLapIntent()))
}
```

In the code example above, the last line donates the `MyMarkLapIntent()` as the next action for the Action button. Donating the next action is described in more detail below.

After implementing your [`StartWorkoutIntent`](startworkoutintent.md), build and run your app to load it onto the test device or Simulator. Then, on the test device, choose Settings > Action Button. Tap Action and choose Workout, then tap App and choose your app.

![A screenshot from Apple Watch Ultra showing the Action button settings, with](https://docs-assets.developer.apple.com/published/a95aeca8e27eb34e1a3f946125986df9/Setting-A-Workout-Action%402x.png)

The device starts a new workout session when you press the Action button.

> ❗ **Important**: The system always launches your app before running the [`perform()`](appintent/perform().md) method for your [`StartWorkoutIntent`](startworkoutintent.md) or [`StartDiveIntent`](startdiveintent.md) structures.  By default, these intents set their [`openAppWhenRun`](appintent/openappwhenrun.md) property to `true`. To ensure these intents run as expected, don’t change the property’s value.

##### Support Multiple Workout Types

Your app can provide a list of suggested workout types, letting people associate a particular workout type with the Action button.

To suggest multiple workout types, start by defining the different types of workouts that your app supports in your [`AppEnum`](appenum.md) implementation.

```swift
enum WorkoutEnum: String, AppEnum {

    // List the types of workout your app supports.
    case walking
    case running
    case swimming
    case cycling

    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Workout"

    // Set the display representation here.
}
```

Then set a display representation for each case.

```swift
static var caseDisplayRepresentations: [WorkoutEnum: DisplayRepresentation] =
[.walking: DisplayRepresentation(title: "Walking", subtitle: "outside walk"),
 .running: DisplayRepresentation(title: "Running", subtitle: "outside run"),
 .swimming: DisplayRepresentation(title: "Swimming", subtitle: "lap swim"),
 .cycling: DisplayRepresentation(title: "Cycling", subtitle: "outside cycling")
]
```

Next, in your [`StartWorkoutIntent`](startworkoutintent.md) implementation, define the set of suggested workouts.

```swift
static var suggestedWorkouts: [MyStartWorkoutIntent] =
[MyStartWorkoutIntent(style: .walking),
 MyStartWorkoutIntent(style: .running),
 MyStartWorkoutIntent(style: .swimming),
 MyStartWorkoutIntent(style: .cycling)]
```

Then, in the [`perform()`](appintent/perform().md) method, check the intent’s [`workoutStyle`](startworkoutintent/workoutstyle-swift.property.md) and create the corresponding workout session.

```swift
func perform() async throws -> some IntentResult {

    let workoutManager = MyWorkoutManager.shared
    await workoutManager.requestAuthorization()
    await workoutManager.startWorkout(type: workoutStyle)
    return .result()
}
```

Create a configuration for the specified type of workout.

```swift
func startWorkout(type: WorkoutEnum) throws {
    logger.debug("*** Should be starting a workout of type \(type.rawValue) ***")
    
    logger.debug("==> Creating the workout configuration.")
    let configuration = HKWorkoutConfiguration()
    
    switch type {
    case .walking:
        configuration.activityType = .walking
    case .running:
        configuration.activityType = .running
    case .swimming:
        configuration.activityType = .swimming
    case .cycling:
        configuration.activityType = .cycling
    }
    configuration.activityType = type.activityType()
    
    if type == .swimming {
        configuration.locationType = .indoor
        configuration.swimmingLocationType = .pool
        configuration.lapLength = HKQuantity(unit: HKUnit.yard(), doubleValue: 25.0)
    } else {
        configuration.locationType = .outdoor
    }
    
    self.configuration = configuration
    
    logger.debug("==> Creating the workout session.")
    let session = try HKWorkoutSession(healthStore: store, configuration: configuration)
    
    session.delegate = self
    self.session = session
    workoutType = type
    
    logger.debug("==> Starting the session.")
    session.startActivity(with: Date())
}
```

And, finally, request authorization for all the data types that your workout sessions use.

```swift
// The quantity types to read from the health store.
let typesToRead: Set = [
    HKQuantityType(.heartRate),
    HKQuantityType(.activeEnergyBurned),
    HKQuantityType(.distanceCycling),
    HKQuantityType(.distanceSwimming),
    HKQuantityType(.distanceWalkingRunning)
]
```

Build and run your app again. When you open the Action button settings, you can specify a particular workout for the First Press > Workout setting.

![A screenshot from Apple Watch Ultra showing the Action button’s First Press](https://docs-assets.developer.apple.com/published/7894190ae7b19168716e416cad6aa30e/Specifying-The-Workout-Type%402x.png)

And pressing the Action button launches the selected type of workout.

##### Donate the Next Action

Apple Watch Ultra runs the next action when someone presses the Action button while a workout or dive session is already running. This means the first time someone presses the Action button, the system starts your session. If they press the Action button any other time during the session, it triggers the next action.

To set the next action, implement a structure that adopts the [`AppIntent`](appintent.md) protocol.

```swift
struct MarkLapIntent: AppIntent {
    static var title: LocalizedStringResource = "Mark Lap"

    func perform() async throws -> some IntentResult {
        logger.debug("*** Perform a mark lap intent. ***")
        await MyWorkoutManager.shared.markLap(at: Date())
        return .result()
    }
}
```

This intent needs a [`title`](appintent/title.md) property that provides a localized description of the action, and a [`perform()`](appintent/perform().md) method, which the system calls when it triggers the intent.

Next, donate the app intent as the current session’s next action. For example, in your start workout intent’s `perform()` method, you can donate the next action for the new session by returning [`result(actionButtonIntent:)`](intentresult/result(actionbuttonintent:).md).

However, in most cases you want to donate a next action regardless of whether the user presses the Action button or launches the session from within your app. To ensure that your app donates the correct intent, simply return `.result()` from your start intent, and then donate the next intent as soon as the session starts.

Previous code examples show how to donate the `MyMarkLapIntent` in its `startCollectingData()` method. The app then calls this method when starting a workout from the Action button or from the app’s user interface.

```swift
logger.debug("==> Donate the mark lap intent as the Action button's next action.")
try await MyStartWorkoutIntent().donate(result: .result(actionButtonIntent: MyMarkLapIntent()))
```

You can donate as many action intents as you need; however, your app can use only the most recently donated intent as the next action. Donating a new intent changes the next action.

##### Pause and Resume a Workout

Apple Watch Ultra supports pausing and resuming a current workout session by simultaneously pressing both the Action button and the side button.

To implement the pause action, create a structure that adopts the [`PauseWorkoutIntent`](pauseworkoutintent.md) protocol.

```swift
struct MyPauseWorkoutIntent: PauseWorkoutIntent {
    static var title: LocalizedStringResource = "Pause Workout"

    func perform() async throws -> some IntentResult {
        logger.debug("*** Performing a pause intent. ***")
        await MyWorkoutManager.shared.pauseWorkout()
        return .result()
    }
}
```

This intent needs a [`title`](appintent/title.md) property that provides a localized description of the action, and a [`perform()`](appintent/perform().md) method, which the system calls when it triggers the intent.

Similarly, to implement the resume action, create a structure that adopts the [`ResumeWorkoutIntent`](resumeworkoutintent.md) protocol.

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

If your app doesn’t implement structures that adopt these protocols, the system ignores simultaneous presses.

##### Start a New Dive Session

Dive sessions work similarly to workout sessions. To start a dive session, implement a structure that adopts the [`StartDiveIntent`](startdiveintent.md) protocol. Typically, people start the dive session just before entering the water. Your app can then donate App Intents that help them use your app while in the water. For example, while in the water they can’t use the touch screen, but the Action button and Digital Crown function normally.

```swift
struct MyStartDiveSessionIntent: StartDiveIntent {

    static var title: LocalizedStringResource = "Starting a dive session."

    func perform() async throws -> some IntentResult {
        logger.debug("*** Starting a dive session. ***")

        await DiveManager.shared.start()
        return .result(actionButtonIntent: MyCollectSubmergedDataIntent())
    }
}
```

This intent needs a [`title`](appintent/title.md) property that provides a localized description of the action, and a [`perform()`](appintent/perform().md) method, which the system calls when it triggers the intent.

To read live depth, water pressure, and water temperature data, see [`Accessing submersion data`](https://developer.apple.com/documentation/CoreMotion/accessing-submersion-data).

> ❗ **Important**: Before you can access live dive data, your app needs to include an entitlement to access submersion data. For more information, see [`Express interest in the Submerged Depth and Pressure API`](https://developer.apple.comhttps://developer.apple.com/contact/request/submerged-depth-pressure-api/).

Unlike workout sessions, the start dive intent supports only a single type of session. You can donate next actions for your dive session; however, you can’t create intents to pause or resume the session.

##### Passing Data to the Intents

The previous examples use singleton objects to share data between the different parts of your app; however, App Intents support dependency injection, letting you define the data in your main app, and access it in your intents.

In your intents, create a property that uses the [`AppDependency`](appdependency.md) property wrapper.

```swift
struct MyStartWorkoutIntent: StartWorkoutIntent {
  @Dependency var workoutManager: MyWorkoutManager

  // Add remaining code here.
}
```

Then, as early as possible when your app launches, use the [`AppDependencyManager`](appdependencymanager.md) to define the dependency.

```swift
AppDependencyManager.shared.add { MyWorkoutManager() }
```

You can set the dependency in your app’s [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/WatchKit/WKApplicationDelegate/applicationDidFinishLaunching()) method. Or, if your app uses SwiftUI life cycles, add an `init()` method to your [`App`](https://developer.apple.com/documentation/SwiftUI/App) structure, and set it there.

One of the main advantages of dependency injection is that you can easily replace your main data object with a mock object during testing.

> **Note**: You can only use dependency injection to pass data objects from your main app to its intents. If you need to pass the data to other parts of your app, you need to use a different approach.

##### Debug Intents

To see console output and respond to breakpoints in Xcode, use the following steps to debug your intents:

1. Build and run your app in Xcode.
2. On the test device or Simulator, send your app to the background. For example, press Shift-Command-H in Simulator to send your app to the background.
3. Make sure you set the actions you want to test by choosing Settings > Action Button.
4. Press the Action button to test the primary and next actions. On a test device, you can also test the pause and resume actions for workout sessions by pressing the Action button and the side button simultaneously.

Any logging from your intents appears in Xcode’s console. The system also pauses execution for any breakpoints you set in Xcode.

## See Also

- [protocol StartWorkoutIntent](startworkoutintent.md)
  An App Intent for starting a workout.
- [protocol PauseWorkoutIntent](pauseworkoutintent.md)
  An App Intent that lets someone pause your app’s current workout session.
- [protocol ResumeWorkoutIntent](resumeworkoutintent.md)
  An App Intent that lets someone resume your app’s paused workout session.
- [protocol StartDiveIntent](startdiveintent.md)
  An App Intent that lets people start a dive session when they press the Action button on Apple Watch Ultra.
- [struct ConfirmationActionName](confirmationactionname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppIntents/actionbuttonarticle)*