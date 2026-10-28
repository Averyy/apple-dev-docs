# session(_:didChange:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Listen and react to geo-tracking state changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
optional func session(_ session: ARSession, didChange geoTrackingStatus: ARGeoTrackingStatus)
```

```objc
- (void) session:(ARSession *) session didChangeGeoTrackingStatus:(ARGeoTrackingStatus *) geoTrackingStatus;
```

## Discussion

To create and maintain an effective geo-tracking session, an app must react promptly when ARKit changes the geo-tracking status. For more information, see [`ARGeoTrackingStatus`](../argeotrackingstatus.md).

ARKit invokes this callback only for [`ARGeoTrackingConfiguration`](../argeotrackingconfiguration.md) sessions.

## Parameters

- `session`: The geo-tracking session.
- `geoTrackingStatus`: The new status.

## See Also

### Responding to Tracking Quality Changes
- [func session(ARSession, cameraDidChangeTrackingState: ARCamera)](./session%28_,cameradidchangetrackingstate%29.md)
  Informs the delegate of changes to the quality of ARKit’s device position tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/session(_:didchange:))*