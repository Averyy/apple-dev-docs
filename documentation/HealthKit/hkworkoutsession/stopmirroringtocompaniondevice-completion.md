# stopMirroringToCompanionDevice(completion:)

**Framework**: HealthKit  
**Kind**: method

Stops mirroring the workout session to the companion iOS device.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
func stopMirroringToCompanionDevice() async throws
```

#### Discussion

Call this method in your watchOS app to stop the mirrored workout session on the companion iOS app. After the mirroring stops, the system calls the [`workoutSession(_:didDisconnectFromRemoteDeviceWithError:)`](hkworkoutsessiondelegate/workoutsession(_:diddisconnectfromremotedevicewitherror:).md) method on the iOS companion’s session delegate.

```swift
session.end()

// Stop the workout builder and save the workout data.
do {
    try await builder.endCollection(at: Date())
    try await builder.finishWorkout()
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while stoping the workout: \(error.localizedDescription) ***")
}

// Stop the mirrored workout on the iOS companion.
do {
    try await session.stopMirroringToCompanionDevice()
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while stoping the mirrored workout: \(error.localizedDescription) ***")
}
```

## Parameters

- `completion`: A block that the system calls when the stop request is complete. The system sets the following parameters:

## See Also

- [func startMirroringToCompanionDevice(completion: (Bool, (any Error)?) -> Void)](hkworkoutsession/startmirroringtocompaniondevice(completion:).md)
  Starts mirroring the workout session to the companion iOS device.
- [func sendToRemoteWorkoutSession(data: Data, completion: (Bool, (any Error)?) -> Void)](hkworkoutsession/sendtoremoteworkoutsession(data:completion:).md)
  Sends the provided data to the remote workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/stopmirroringtocompaniondevice(completion:))*