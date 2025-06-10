# sessionWasInterrupted(_:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that the session has temporarily stopped processing frames and tracking device position.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func sessionWasInterrupted(_ session: ARSession)
```

#### Discussion

A session is interrupted when it fails to receive camera or motion sensing data. Session interruptions occur whenever camera capture is not available—for example, when your app is in the background or there are multiple foreground apps—or when the device is too busy to process motion sensor data.

> ❗ **Important**:  An interruption is equivalent to manually pausing the session. Do not call [`pause()`](arsession/pause().md) in response to this callback, as that prevents your app from being notified when the interruption ends.

## Parameters

- `session`: The session providing information.

## See Also

- [func sessionInterruptionEnded(ARSession)](arsessionobserver/sessioninterruptionended(_:).md)
  Tells the delegate that the session has resumed processing frames and tracking device position.
- [func sessionShouldAttemptRelocalization(ARSession) -> Bool](arsessionobserver/sessionshouldattemptrelocalization(_:).md)
  Asks the delegate whether to attempt recovery of world-tracking state after an interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/sessionwasinterrupted(_:))*