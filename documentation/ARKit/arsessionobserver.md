# ARSessionObserver

**Framework**: ARKit  
**Kind**: protocol

Methods you can implement to respond to changes in the state of an AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol ARSessionObserver : NSObjectProtocol
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

#### Overview

This protocol defines optional methods common to the [`ARSessionDelegate`](arsessiondelegate.md), [`ARSCNViewDelegate`](arscnviewdelegate.md), and [`ARSKViewDelegate`](arskviewdelegate.md) protocols. You can implement this protocol’s methods when adopting one of those protocols.

## Topics

### Responding to Tracking Quality Changes
- [func session(ARSession, cameraDidChangeTrackingState: ARCamera)](arsessionobserver/session(_:cameradidchangetrackingstate:).md)
  Informs the delegate of changes to the quality of ARKit’s device position tracking.
- [func session(ARSession, didChange: ARGeoTrackingStatus)](arsessionobserver/session(_:didchange:).md)
  Listen and react to geo-tracking state changes.
### Handling Interruptions
- [func sessionWasInterrupted(ARSession)](arsessionobserver/sessionwasinterrupted(_:).md)
  Tells the delegate that the session has temporarily stopped processing frames and tracking device position.
- [func sessionInterruptionEnded(ARSession)](arsessionobserver/sessioninterruptionended(_:).md)
  Tells the delegate that the session has resumed processing frames and tracking device position.
- [func sessionShouldAttemptRelocalization(ARSession) -> Bool](arsessionobserver/sessionshouldattemptrelocalization(_:).md)
  Asks the delegate whether to attempt recovery of world-tracking state after an interruption.
### Receiving Audio Data
- [func session(ARSession, didOutputAudioSampleBuffer: CMSampleBuffer)](arsessionobserver/session(_:didoutputaudiosamplebuffer:).md)
  Tells the delegate that a new sample buffer of recorded audio is available.
### Handling Errors
- [func session(ARSession, didFailWithError: any Error)](arsessionobserver/session(_:didfailwitherror:).md)
  Tells the delegate that the session has stopped running due to an error.
- [let ARErrorDomain: String](arerrordomain.md)
  The domain for error objects produced by an AR session.
### Managing Collaboration
- [func session(ARSession, didOutputCollaborationData: ARSession.CollaborationData)](arsessionobserver/session(_:didoutputcollaborationdata:).md)
  Provides information for nearby users about your perspective in the environment.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [ARSCNViewDelegate](arscnviewdelegate.md)
- [ARSKViewDelegate](arskviewdelegate.md)
- [ARSessionDelegate](arsessiondelegate.md)

## See Also

- [var delegate: (any ARSessionDelegate)?](arsession/delegate.md)
  An object you provide to receive captured video images and tracking information, or to respond to changes in session status.
- [var delegateQueue: dispatch_queue_t?](arsession/delegatequeue.md)
  The dispatch queue through which the session calls your delegate methods.
- [protocol ARSessionDelegate](arsessiondelegate.md)
  Methods you can implement to receive captured video frame images and tracking state from an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver)*