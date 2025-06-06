# session(_:didChange:)

**Framework**: ARKit  
**Kind**: method

Listen and react to geo-tracking state changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func session(_ session: ARSession, didChange geoTrackingStatus: ARGeoTrackingStatus)
```

#### Discussion

To create and maintain an effective geo-tracking session, an app must react promptly when ARKit changes the geo-tracking status. For more information, see [`ARGeoTrackingStatus`](argeotrackingstatus.md).

ARKit invokes this callback only for [`ARGeoTrackingConfiguration`](argeotrackingconfiguration.md) sessions.

## Parameters

- `session`: The geo-tracking session.
- `geoTrackingStatus`: The new status.

## See Also

- [func session(ARSession, cameraDidChangeTrackingState: ARCamera)](arsessionobserver/session(_:cameradidchangetrackingstate:).md)
  Informs the delegate of changes to the quality of ARKit’s device position tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/session(_:didchange:))*