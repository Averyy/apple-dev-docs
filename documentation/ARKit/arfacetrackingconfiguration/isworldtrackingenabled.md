# isWorldTrackingEnabled

**Framework**: ARKit  
**Kind**: property

A Boolean value that instructs a session to provide the app with the device’s six degrees of freedom pose during a face-tracking session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isWorldTrackingEnabled: Bool { get set }
```

#### Discussion

Before attempting to enable this property, check whether the iOS device supports user-face tracking in a world-tracking session, by calling [`supportsWorldTracking`](arfacetrackingconfiguration/supportsworldtracking.md).

## See Also

- [class var supportsWorldTracking: Bool](arfacetrackingconfiguration/supportsworldtracking.md)
  A Boolean value that indicates whether the iOS device supports tracking the user’s facial features in a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacetrackingconfiguration/isworldtrackingenabled)*