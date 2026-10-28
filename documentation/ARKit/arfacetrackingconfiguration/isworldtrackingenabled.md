# isWorldTrackingEnabled

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that instructs a session to provide the app with the device’s six degrees of freedom pose during a face-tracking session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var isWorldTrackingEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isWorldTrackingEnabled) BOOL worldTrackingEnabled;
```

## Discussion

Before attempting to enable this property, check whether the iOS device supports user-face tracking in a world-tracking session, by calling [`supportsWorldTracking`](./supportsworldtracking.md).

## See Also

### Enabling World Tracking
- [class var supportsWorldTracking: Bool](./supportsworldtracking.md)
  A Boolean value that indicates whether the iOS device supports tracking the user’s facial features in a world-tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacetrackingconfiguration/isworldtrackingenabled)*