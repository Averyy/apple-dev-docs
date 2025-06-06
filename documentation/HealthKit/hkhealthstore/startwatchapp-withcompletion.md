# startWatchApp(with:completion:)

**Framework**: HealthKit  
**Kind**: method

Launches or wakes the companion watchOS app to create a new workout session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func startWatchApp(toHandle workoutConfiguration: HKWorkoutConfiguration) async throws
```

#### Discussion

Use this method to launch the companion watchOS app on a paired Apple Watch. After launching, the system calls the handle method on the watchOS app’s delegate and passes the provided workout configuration. Use the workout configuration to start a new workout session on the watch.

To launch a mirrored workout from the iOS companion app, call this method in the iOS companion.

```swift
let configuration = HKWorkoutConfiguration()
configuration.activityType = .running
configuration.locationType = .outdoor

do {
    try await store.startWatchApp(toHandle: configuration)
}
catch {
    // Handle the error here.
    fatalError("*** An error occurred while starting a workout on Apple Watch: \(error.localizedDescription) ***")
}

logger.debug("*** Workout Session Started ***")
```

Next, set up the mirrored workout in the [`WKApplicationDelegate`](https://developer.apple.com/documentation/WatchKit/WKApplicationDelegate) object’s [`handle(_:)`](https://developer.apple.com/documentation/WatchKit/WKApplicationDelegate/handle(_:)-1pfoc) method.

```swift
class AppDelegate: NSObject, WKApplicationDelegate {

    func handle(_ workoutConfiguration: HKWorkoutConfiguration) {
        Task {
            await WorkoutManager.shared.startWorkout()
            logger.debug("Successfully started workout")
        }
    }
}

extension WorkoutManager {
    func startWorkout() async {

        let configuration = HKWorkoutConfiguration()
        configuration.activityType = .running
        configuration.locationType = .outdoor

        let session: HKWorkoutSession
        do {
            session = try HKWorkoutSession(healthStore: store,
                                           configuration: configuration)
        } catch {
            // Handle failure here.
            fatalError("*** An error occurred: \(error.localizedDescription) ***")
        }

        let builder = session.associatedWorkoutBuilder()

        let source = HKLiveWorkoutDataSource(healthStore: store,
                                             workoutConfiguration: configuration)

        source.enableCollection(for: HKQuantityType(.stepCount), predicate: nil)
        builder.dataSource = source

        session.delegate = self
        builder.delegate = self

        self.session = session
        self.builder = builder

        let start = Date()

        // Start the mirrored session on the companion iPhone.
        do {
            try await session.startMirroringToCompanionDevice()
        }
        catch {
            fatalError("*** Unable to start the mirrored workout: \(error.localizedDescription) ***")
        }

        // Start the workout session.
        session.startActivity(with: start)

        do {
            try await builder.beginCollection(at: start)
        } catch {
            // Handle the error here.
            fatalError("*** An error occurred while starting the workout: \(error.localizedDescription) ***")
        }

        logger.debug("*** Workout Session Started ***")
    }
}
```

## Parameters

- `workoutConfiguration`: The configuration data for a new workout session on the watch.
- `completion`: A block that this method calls after launching the Watch app. The system calls this block, passing the following parameters:

## See Also

- [var workoutSessionMirroringStartHandler: ((HKWorkoutSession) -> Void)?](hkhealthstore/workoutsessionmirroringstarthandler.md)
  A block that the system calls when it starts a mirrored workout session.
- [func pause(HKWorkoutSession)](hkhealthstore/pause(_:).md)
  Pauses the provided workout session.
- [func resumeWorkoutSession(HKWorkoutSession)](hkhealthstore/resumeworkoutsession(_:).md)
  Resumes the provided workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/startwatchapp(with:completion:))*