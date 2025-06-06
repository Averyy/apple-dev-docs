# multipleRoutesDetected

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the object detects more than one playback route.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var multipleRoutesDetected: Bool { get }
```

#### Discussion

The system posts a [`AVRouteDetectorMultipleRoutesDetectedDidChangeNotification`](avroutedetectormultipleroutesdetecteddidchangenotification.md) notification when this property value changes.

## See Also

- [var detectsCustomRoutes: Bool](avroutedetector/detectscustomroutes.md)
  A Boolean value that indicates whether route detection includes custom routes.
- [var isRouteDetectionEnabled: Bool](avroutedetector/isroutedetectionenabled.md)
  A Boolean value that indicates whether route detection is in an enabled state.
- [static let AVRouteDetectorMultipleRoutesDetectedDidChange: NSNotification.Name](../foundation/nsnotification/name/2915761-avroutedetectormultipleroutesdet.md)
  A notification the system posts when changes occur to its detected routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avroutedetector/multipleroutesdetected)*