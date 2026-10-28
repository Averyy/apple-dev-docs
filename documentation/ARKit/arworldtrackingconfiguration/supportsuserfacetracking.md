# supportsUserFaceTracking

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that tells you whether the iOS device supports tracking the user’s face during a world-tracking session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
class var supportsUserFaceTracking: Bool { get }
```

```objc
@property (class, nonatomic, readonly) BOOL supportsUserFaceTracking;
```

## Discussion

Check the value of this property first, before you enable face tracking using [`userFaceTrackingEnabled`](./userfacetrackingenabled.md).

## See Also

### Tracking the User’s Face
- [var userFaceTrackingEnabled: Bool](./userfacetrackingenabled.md)
  A flag that determines whether ARKit tracks the user’s face in a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/supportsuserfacetracking)*