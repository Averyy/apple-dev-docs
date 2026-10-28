# HKWorkoutSessionDelegate

**Framework**: HealthKit  
**Kind**: protocol  
**Role**: Protocol

The session delegate protocol that defines an interface for receiving notifications about errors and changes in the workout session’s state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol HKWorkoutSessionDelegate : NSObjectProtocol
```

```objc
@protocol HKWorkoutSessionDelegate <NSObject>
```

## Mentions

- [Running workout sessions](./running-workout-sessions.md)

## Overview

All the methods are required. HealthKit calls these methods on an anonymous serial background queue.

## Topics

### Tracking workout sessions
- [func workoutSession(HKWorkoutSession, didChangeTo: HKWorkoutSessionState, from: HKWorkoutSessionState, date: Date)](./hkworkoutsessiondelegate/workoutsession%28_,didchangeto,from,date%29.md)
  Tells the delegate that the session’s state changed.
- [func workoutSession(HKWorkoutSession, didFailWithError: any Error)](./hkworkoutsessiondelegate/workoutsession%28_,didfailwitherror%29.md)
  Tells the delegate that the session failed with an error.
- [func workoutSession(HKWorkoutSession, didGenerate: HKWorkoutEvent)](./hkworkoutsessiondelegate/workoutsession%28_,didgenerate%29.md)
  Tells the delegate that the system generated a workout event.
- [func workoutSession(HKWorkoutSession, didBeginActivityWith: HKWorkoutConfiguration, date: Date)](./hkworkoutsessiondelegate/workoutsession%28_,didbeginactivitywith,date%29.md)
  Tells the delegate that a new workout session began.
- [func workoutSession(HKWorkoutSession, didEndActivityWith: HKWorkoutConfiguration, date: Date)](./hkworkoutsessiondelegate/workoutsession%28_,didendactivitywith,date%29.md)
  Tells the session that the current workout activity ended.
### Working with mirrored sessions
- [func workoutSession(HKWorkoutSession, didDisconnectFromRemoteDeviceWithError: (any Error)?)](./hkworkoutsessiondelegate/workoutsession%28_,diddisconnectfromremotedevicewitherror%29.md)
  Tells the delegate that the mirrored workout session disconnected from the primary session.
- [func workoutSession(HKWorkoutSession, didReceiveDataFromRemoteWorkoutSession: [Data])](./hkworkoutsessiondelegate/workoutsession%28_,didreceivedatafromremoteworkoutsession%29.md)
  Passes data from the remote workout session to the session delegate.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Monitoring the session
- [var delegate: (any HKWorkoutSessionDelegate)?](./hkworkoutsession/delegate.md)
  The workout session’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiondelegate)*