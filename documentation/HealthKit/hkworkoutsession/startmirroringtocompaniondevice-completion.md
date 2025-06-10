# startMirroringToCompanionDevice(completion:)

**Framework**: HealthKit  
**Kind**: method

Starts mirroring the workout session to the companion iOS device.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
func startMirroringToCompanionDevice() async throws
```

#### Discussion

Call this method in your watchOS app to start a mirrored workout session on the companion iOS app. If your iOS app isn’t running, the system launches it in the background. The iOS companion app must assign a completion handler to its HealthKit Store’s [`workoutSessionMirroringStartHandler`](hkhealthstore/workoutsessionmirroringstarthandler.md) property to process the incoming session.

> ❗ **Important**:  This method fails if you call it on a workout session that ended.

```swift
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
    fatalError("*** An error occurred while starting the workout: \(error.localizedDescription) ***")
}
```

## Parameters

- `completion`: A block that the system calls when the start request is complete. The system sets the following parameters:

## See Also

- [func stopMirroringToCompanionDevice(completion: (Bool, (any Error)?) -> Void)](hkworkoutsession/stopmirroringtocompaniondevice(completion:).md)
  Stops mirroring the workout session to the companion iOS device.
- [func sendToRemoteWorkoutSession(data: Data, completion: (Bool, (any Error)?) -> Void)](hkworkoutsession/sendtoremoteworkoutsession(data:completion:).md)
  Sends the provided data to the remote workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/startmirroringtocompaniondevice(completion:))*