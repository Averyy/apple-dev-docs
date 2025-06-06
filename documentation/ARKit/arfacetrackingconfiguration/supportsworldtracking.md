# supportsWorldTracking

**Framework**: ARKit  
**Kind**: property

A Boolean value that indicates whether the iOS device supports tracking the user’s facial features in a world-tracking session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class var supportsWorldTracking: Bool { get }
```

#### Discussion

Call this function before attempting to enable world tracking in a face tracking configuration using [`isWorldTrackingEnabled`](arfacetrackingconfiguration/isworldtrackingenabled.md).

## See Also

- [var isWorldTrackingEnabled: Bool](arfacetrackingconfiguration/isworldtrackingenabled.md)
  A Boolean value that instructs a session to provide the app with the device’s six degrees of freedom pose during a face-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacetrackingconfiguration/supportsworldtracking)*