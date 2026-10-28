# sendToRemoteWorkoutSession(data:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Sends the provided data to the remote workout session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func sendToRemoteWorkoutSession(data: Data, completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func sendToRemoteWorkoutSession(data: Data) async throws
```

```objc
- (void) sendDataToRemoteWorkoutSession:(NSData *) data completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

Call this method to send data to your remote workout session. You can send data from either the [`HKWorkoutSessionType.mirrored`](../hkworkoutsessiontype/mirrored.md) or [`HKWorkoutSessionType.primary`](../hkworkoutsessiontype/primary.md) session.

```swift
let archivedData = try? NSKeyedArchiver.archivedData(withRootObject: data, requiringSecureCoding: true)
guard let archivedData = archivedData, !archivedData.isEmpty else {
    // Handle the error here.
    fatalError("*** Encoded data is empty ***")
}

// Send the data to the companion iPhone.
Task {
    do {
        try await session.sendToRemoteWorkoutSession(data: archivedData)
    }
    catch {
        // Handle the error here.
        fatalError("*** An error occurred while sending the health data to the companion iPhone: \(error.localizedDescription) ***")
    }
}
```

## Parameters

- `data`: A data object that contains the data your app is sending to the remote workout session.
- `completion`: A block that the system calls when the send attempt is complete. The system passes the following parameters:

  - **`success`**: A Boolean value that indicates whether the system successfully sent the data.
  - **`error`**: If `sucess` is [`false`](../../Swift/false.md), this contains an object that describes the error. Otherwise, it’s `nil`.

## See Also

### Working with remote workout sessions
- [func startMirroringToCompanionDevice(completion: (Bool, (any Error)?) -> Void)](./startmirroringtocompaniondevice%28completion%29.md)
  Starts mirroring the workout session to the companion iOS device.
- [func stopMirroringToCompanionDevice(completion: (Bool, (any Error)?) -> Void)](./stopmirroringtocompaniondevice%28completion%29.md)
  Stops mirroring the workout session to the companion iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/sendtoremoteworkoutsession(data:completion:))*