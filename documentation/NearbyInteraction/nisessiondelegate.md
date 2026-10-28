# NISessionDelegate

**Framework**: Nearby Interaction  
**Kind**: protocol  
**Role**: Protocol

An object that monitors and reacts to session updates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
protocol NISessionDelegate : NSObjectProtocol
```

```objc
@protocol NISessionDelegate <NSObject>
```

## Mentions

- [Initiating and maintaining a session](./initiating-and-maintaining-a-session.md)

## Overview

Assign a delegate that Nearby Interaction can use to notify your app of important events that occur during the session life cycle.

## Topics

### Reacting to session start
- [func sessionDidStartRunning(NISession)](./nisessiondelegate/sessiondidstartrunning%28_%29.md)
  Notifies the app when a session starts or resumes running.
### Monitoring peers
- [func session(NISession, didUpdate: [NINearbyObject])](./nisessiondelegate/session%28_,didupdate%29.md)
  Notifies you when the session updates nearby objects.
- [func session(NISession, didGenerateShareableConfigurationData: Data, for: NINearbyObject)](./nisessiondelegate/session%28_,didgenerateshareableconfigurationdata,for%29.md)
  Provides configuration data to share with a third-party accessory.
- [func session(NISession, didRemove: [NINearbyObject], reason: NINearbyObject.RemovalReason)](./nisessiondelegate/session%28_,didremove,reason%29.md)
  Notifies you when the session removes one or more nearby objects.
- [NINearbyObject.RemovalReason](./ninearbyobject/removalreason.md)
  The reason a session removed a nearby object.
### Managing interruption
- [func sessionWasSuspended(NISession)](./nisessiondelegate/sessionwassuspended%28_%29.md)
  Notifies you of a suspended session.
- [func sessionSuspensionEnded(NISession)](./nisessiondelegate/sessionsuspensionended%28_%29.md)
  Notifies you of the end of a session’s suspension.
### Handling errors
- [func session(NISession, didInvalidateWith: any Error)](./nisessiondelegate/session%28_,didinvalidatewith%29.md)
  Notifies you of an invalidated session.
### Coaching the user
- [func session(NISession, didUpdateAlgorithmConvergence: NIAlgorithmConvergence, for: NINearbyObject?)](./nisessiondelegate/session%28_,didupdatealgorithmconvergence,for%29.md)
  Provides recommended actions the user can take to facilitate the framework’s Camera Assistance.
- [enum NIAlgorithmConvergenceStatus](./nialgorithmconvergencestatus-2fnve.md)
  The possible states of Camera Assistance.
- [NIAlgorithmConvergenceStatus.Reason](./nialgorithmconvergencestatus-2fnve/reason.md)
  The possible reasons for the Camera Assistance status.
### Monitoring DL-TDOA measurements
- [func session(NISession, didUpdateDLTDOA: [NIDLTDOAMeasurement])](./nisessiondelegate/session%28_,didupdatedltdoa%29.md)
  Provides device ranging estimates for a Downlink Time-Difference-of-Arrival session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate)*