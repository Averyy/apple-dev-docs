# sessionInterruptionEnded(_:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that the session has resumed processing frames and tracking device position.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func sessionInterruptionEnded(_ session: ARSession)
```

#### Discussion

After a session has been interrupted (see the [`sessionWasInterrupted(_:)`](arsessionobserver/sessionwasinterrupted(_:).md) delegate method), it automatically resumes running whenever the conditions that caused the interruption improve.

When a session resumes, it continues tracking from its last known state. However, if the device has moved since the interruption began, the ARKit world coordinate system and anchor positions no longer match their original real-world frame of reference. To attempt recovery of world tracking from before the interruption, implement the [`sessionShouldAttemptRelocalization(_:)`](arsessionobserver/sessionshouldattemptrelocalization(_:).md) delegate method.

## Parameters

- `session`: The session providing information.

## See Also

- [func sessionWasInterrupted(ARSession)](arsessionobserver/sessionwasinterrupted(_:).md)
  Tells the delegate that the session has temporarily stopped processing frames and tracking device position.
- [func sessionShouldAttemptRelocalization(ARSession) -> Bool](arsessionobserver/sessionshouldattemptrelocalization(_:).md)
  Asks the delegate whether to attempt recovery of world-tracking state after an interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/sessioninterruptionended(_:))*