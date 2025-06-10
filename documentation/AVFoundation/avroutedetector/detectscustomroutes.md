# detectsCustomRoutes

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether route detection includes custom routes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var detectsCustomRoutes: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). Only set it to [`true`](https://developer.apple.com/documentation/swift/true) if your app uses an instance of [`AVCustomRoutingController`](https://developer.apple.com/documentation/AVRouting/AVCustomRoutingController).

## See Also

- [var isRouteDetectionEnabled: Bool](avroutedetector/isroutedetectionenabled.md)
  A Boolean value that indicates whether route detection is in an enabled state.
- [var multipleRoutesDetected: Bool](avroutedetector/multipleroutesdetected.md)
  A Boolean value that indicates whether the object detects more than one playback route.
- [static let AVRouteDetectorMultipleRoutesDetectedDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/AVRouteDetectorMultipleRoutesDetectedDidChange.md)
  A notification the system posts when changes occur to its detected routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avroutedetector/detectscustomroutes)*