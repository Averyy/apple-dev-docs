# workoutSession(_:didDisconnectFromRemoteDeviceWithError:)

**Framework**: HealthKit  
**Kind**: method

Tells the delegate that the mirrored workout session disconnected from the primary session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
optional func workoutSession(_ workoutSession: HKWorkoutSession, didDisconnectFromRemoteDeviceWithError error: (any Error)?)
```

#### Discussion

After the system calls this method, the provided workout session is no longer valid, and you can no longer use it.

```swift
func clearWorkoutSession() {
    state = .notRunning
    session = nil
}

nonisolated func workoutSession(_ workoutSession: HKWorkoutSession, didDisconnectFromRemoteDeviceWithError error: Error?) {
    Task {
        // Clear the old session.
        await clearWorkoutSession()
    }

    logger.debug("*** Remote workout session disconnected. ***")
    if let error {
        fatalError("*** Disconnected with an error: \(error.localizedDescription) ***")
    }
}
```

If the primary workout session is still running, it automatically tries to reconnect. If successful, the companion iOS device calls the [`workoutSessionMirroringStartHandler`](hkhealthstore/workoutsessionmirroringstarthandler.md) block again, passing in a new, valid [`HKWorkoutSession`](hkworkoutsession.md) instance.

## Parameters

- `workoutSession`: The mirrored workout session that disconnected.
- `error`: If an error caused the disconnection, then this parameter contains the error value. Otherwise, it’s  .

## See Also

- [func workoutSession(HKWorkoutSession, didReceiveDataFromRemoteWorkoutSession: [Data])](hkworkoutsessiondelegate/workoutsession(_:didreceivedatafromremoteworkoutsession:).md)
  Passes data from the remote workout session to the session delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate/workoutsession(_:diddisconnectfromremotedevicewitherror:))*