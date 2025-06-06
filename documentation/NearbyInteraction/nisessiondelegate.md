# NISessionDelegate

**Framework**: Nearby Interaction  
**Kind**: protocol

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

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Overview

Assign a delegate that Nearby Interaction can use to notify your app of important events that occur during the session life cycle.

## Topics

### Reacting to session start
- [func sessionDidStartRunning(NISession)](nisessiondelegate/sessiondidstartrunning(_:).md)
  Notifies the app when a session starts or resumes running.
### Monitoring peers
- [func session(NISession, didUpdate: [NINearbyObject])](nisessiondelegate/session(_:didupdate:).md)
  Notifies you when the session updates nearby objects.
- [func session(NISession, didGenerateShareableConfigurationData: Data, for: NINearbyObject)](nisessiondelegate/session(_:didgenerateshareableconfigurationdata:for:).md)
  Provides configuration data to share with a third-party accessory.
- [func session(NISession, didRemove: [NINearbyObject], reason: NINearbyObject.RemovalReason)](nisessiondelegate/session(_:didremove:reason:).md)
  Notifies you when the session removes one or more nearby objects.
- [NINearbyObject.RemovalReason](ninearbyobject/removalreason.md)
  The reason a session removed a nearby object.
### Managing interruption
- [func sessionWasSuspended(NISession)](nisessiondelegate/sessionwassuspended(_:).md)
  Notifies you of a suspended session.
- [func sessionSuspensionEnded(NISession)](nisessiondelegate/sessionsuspensionended(_:).md)
  Notifies you of the end of a session’s suspension.
### Handling errors
- [func session(NISession, didInvalidateWith: any Error)](nisessiondelegate/session(_:didinvalidatewith:).md)
  Notifies you of an invalidated session.
### Coaching the user
- [func session(NISession, didUpdateAlgorithmConvergence: NIAlgorithmConvergence, for: NINearbyObject?)](nisessiondelegate/session(_:didupdatealgorithmconvergence:for:).md)
  Provides recommended actions the user can take to facilitate the framework’s Camera Assistance.
- [enum NIAlgorithmConvergenceStatus](nialgorithmconvergencestatus-2fnve.md)
  The possible states of Camera Assistance.
- [NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason.md)
  The possible reasons for the Camera Assistance status.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NINearbyObject](ninearbyobject.md)
  Location information for a peer device in an interaction session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate)*