# ARSessionObserver

**Framework**: ARKit  
**Kind**: protocol  
**Role**: Protocol

Methods you can implement to respond to changes in the state of an AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
protocol ARSessionObserver : NSObjectProtocol
```

```objc
@protocol ARSessionObserver <NSObject>
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](./managing-session-life-cycle-and-tracking-quality.md)

## Overview

This protocol defines optional methods common to the [`ARSessionDelegate`](./arsessiondelegate.md), [`ARSCNViewDelegate`](./arscnviewdelegate.md), and [`ARSKViewDelegate`](./arskviewdelegate.md) protocols. You can implement this protocol’s methods when adopting one of those protocols.

## Topics

### Responding to Tracking Quality Changes
- [func session(ARSession, cameraDidChangeTrackingState: ARCamera)](./arsessionobserver/session%28_,cameradidchangetrackingstate%29.md)
  Informs the delegate of changes to the quality of ARKit’s device position tracking.
- [func session(ARSession, didChange: ARGeoTrackingStatus)](./arsessionobserver/session%28_,didchange%29.md)
  Listen and react to geo-tracking state changes.
### Handling Interruptions
- [func sessionWasInterrupted(ARSession)](./arsessionobserver/sessionwasinterrupted%28_%29.md)
  Tells the delegate that the session has temporarily stopped processing frames and tracking device position.
- [func sessionInterruptionEnded(ARSession)](./arsessionobserver/sessioninterruptionended%28_%29.md)
  Tells the delegate that the session has resumed processing frames and tracking device position.
- [func sessionShouldAttemptRelocalization(ARSession) -> Bool](./arsessionobserver/sessionshouldattemptrelocalization%28_%29.md)
  Asks the delegate whether to attempt recovery of world-tracking state after an interruption.
### Receiving Audio Data
- [func session(ARSession, didOutputAudioSampleBuffer: CMSampleBuffer)](./arsessionobserver/session%28_,didoutputaudiosamplebuffer%29.md)
  Tells the delegate that a new sample buffer of recorded audio is available.
### Handling Errors
- [func session(ARSession, didFailWithError: any Error)](./arsessionobserver/session%28_,didfailwitherror%29.md)
  Tells the delegate that the session has stopped running due to an error.
- [let ARErrorDomain: String](./arerrordomain.md)
  The domain for error objects produced by an AR session.
### Managing Collaboration
- [func session(ARSession, didOutputCollaborationData: ARSession.CollaborationData)](./arsessionobserver/session%28_,didoutputcollaborationdata%29.md)
  Provides information for nearby users about your perspective in the environment.
### Instance Methods
- [func session(ARSession, didChangeViewRotationAngle: CGFloat)](./arsessionobserver/session%28_,didchangeviewrotationangle%29.md)
  This is called when the view rotation angle changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [ARSCNViewDelegate](./arscnviewdelegate.md)
- [ARSKViewDelegate](./arskviewdelegate.md)
- [ARSessionDelegate](./arsessiondelegate.md)

## See Also

### Responding to events
- [var delegate: (any ARSessionDelegate)?](./arsession/delegate.md)
  An object you provide to receive captured video images and tracking information, or to respond to changes in session status.
- [var delegateQueue: dispatch_queue_t?](./arsession/delegatequeue.md)
  The dispatch queue through which the session calls your delegate methods.
- [protocol ARSessionDelegate](./arsessiondelegate.md)
  Methods you can implement to receive captured video frame images and tracking state from an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver)*