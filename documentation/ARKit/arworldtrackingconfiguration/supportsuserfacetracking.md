# supportsUserFaceTracking

**Framework**: ARKit  
**Kind**: property

A Boolean value that tells you whether the iOS device supports tracking the user’s face during a world-tracking session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class var supportsUserFaceTracking: Bool { get }
```

#### Discussion

Check the value of this property first, before you enable face tracking using [`userFaceTrackingEnabled`](arworldtrackingconfiguration/userfacetrackingenabled.md).

## See Also

- [var userFaceTrackingEnabled: Bool](arworldtrackingconfiguration/userfacetrackingenabled.md)
  A flag that determines whether ARKit tracks the user’s face in a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/supportsuserfacetracking)*