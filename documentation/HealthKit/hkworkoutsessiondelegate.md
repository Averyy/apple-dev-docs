# HKWorkoutSessionDelegate

**Framework**: HealthKit  
**Kind**: protocol

The session delegate protocol that defines an interface for receiving notifications about errors and changes in the workout session’s state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol HKWorkoutSessionDelegate : NSObjectProtocol
```

## Mentions

- [Running workout sessions](running-workout-sessions.md)

#### Overview

All the methods are required. HealthKit calls these methods on an anonymous serial background queue.

## Topics

### Tracking workout sessions
- [func workoutSession(HKWorkoutSession, didChangeTo: HKWorkoutSessionState, from: HKWorkoutSessionState, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didchangeto:from:date:).md)
  Tells the delegate that the session’s state changed.
- [func workoutSession(HKWorkoutSession, didFailWithError: any Error)](hkworkoutsessiondelegate/workoutsession(_:didfailwitherror:).md)
  Tells the delegate that the session failed with an error.
- [func workoutSession(HKWorkoutSession, didGenerate: HKWorkoutEvent)](hkworkoutsessiondelegate/workoutsession(_:didgenerate:).md)
  Tells the delegate that the system generated a workout event.
- [func workoutSession(HKWorkoutSession, didBeginActivityWith: HKWorkoutConfiguration, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didbeginactivitywith:date:).md)
  Tells the delegate that a new workout session began.
- [func workoutSession(HKWorkoutSession, didEndActivityWith: HKWorkoutConfiguration, date: Date)](hkworkoutsessiondelegate/workoutsession(_:didendactivitywith:date:).md)
  Tells the session that the current workout activity ended.
### Working with mirrored sessions
- [func workoutSession(HKWorkoutSession, didDisconnectFromRemoteDeviceWithError: (any Error)?)](hkworkoutsessiondelegate/workoutsession(_:diddisconnectfromremotedevicewitherror:).md)
  Tells the delegate that the mirrored workout session disconnected from the primary session.
- [func workoutSession(HKWorkoutSession, didReceiveDataFromRemoteWorkoutSession: [Data])](hkworkoutsessiondelegate/workoutsession(_:didreceivedatafromremoteworkoutsession:).md)
  Passes data from the remote workout session to the session delegate.
### Instance Methods
- [func workoutSession(HKWorkoutSession, didUpdateGeneratedTypes: Set<HKSampleType>)](hkworkoutsessiondelegate/workoutsession(_:didupdategeneratedtypes:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any HKWorkoutSessionDelegate)?](hkworkoutsession/delegate.md)
  The workout session’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate)*