# isRouteDetectionEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether route detection is in an enabled state.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isRouteDetectionEnabled: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  Enabling route detection significantly increases power consumption. Turn it off when you no longer need it.

 Enabling route detection significantly increases power consumption. Turn it off when you no longer need it.

## See Also

- [var detectsCustomRoutes: Bool](avroutedetector/detectscustomroutes.md)
  A Boolean value that indicates whether route detection includes custom routes.
- [var multipleRoutesDetected: Bool](avroutedetector/multipleroutesdetected.md)
  A Boolean value that indicates whether the object detects more than one playback route.
- [static let AVRouteDetectorMultipleRoutesDetectedDidChange: NSNotification.Name](../foundation/nsnotification/name/2915761-avroutedetectormultipleroutesdet.md)
  A notification the system posts when changes occur to its detected routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avroutedetector/isroutedetectionenabled)*