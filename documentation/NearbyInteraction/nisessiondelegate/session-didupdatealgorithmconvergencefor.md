# session(_:didUpdateAlgorithmConvergence:for:)

**Framework**: Nearby Interaction  
**Kind**: method

Provides recommended actions the user can take to facilitate the framework’s Camera Assistance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
optional func session(_ session: NISession, didUpdateAlgorithmConvergence convergence: NIAlgorithmConvergence, for object: NINearbyObject?)
```

#### Discussion

The framework invokes this callback when [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md) is `true` to notify the app of the current convergence state and user-coaching recommendations.

## Parameters

- `session`: The session for which the app leverages Camera Assistance.
- `convergence`: The framework’s state and user recommendations for Camera Assistance.
- `object`: The peer device or third-party accessory. If  , the status refers to the session.

## See Also

- [enum NIAlgorithmConvergenceStatus](nialgorithmconvergencestatus-2fnve.md)
  The possible states of Camera Assistance.
- [NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason.md)
  The possible reasons for the Camera Assistance status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate/session(_:didupdatealgorithmconvergence:for:))*