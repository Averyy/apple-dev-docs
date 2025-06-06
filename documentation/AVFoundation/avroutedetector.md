# AVRouteDetector

**Framework**: AVFoundation  
**Kind**: class

An object that detects available media playback routes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class AVRouteDetector
```

## Mentions

- [Supporting AirPlay in your app](supporting-airplay-in-your-app.md)

#### Overview

If you enable route detection, the object reports whether it detects multiple playback routes. If it does, use [`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView) to present the UI for the user to select an appropriate route.

## Topics

### Detecting Routes
- [var detectsCustomRoutes: Bool](avroutedetector/detectscustomroutes.md)
  A Boolean value that indicates whether route detection includes custom routes.
- [var isRouteDetectionEnabled: Bool](avroutedetector/isroutedetectionenabled.md)
  A Boolean value that indicates whether route detection is in an enabled state.
- [var multipleRoutesDetected: Bool](avroutedetector/multipleroutesdetected.md)
  A Boolean value that indicates whether the object detects more than one playback route.
- [static let AVRouteDetectorMultipleRoutesDetectedDidChange: NSNotification.Name](../foundation/nsnotification/name/2915761-avroutedetectormultipleroutesdet.md)
  A notification the system posts when changes occur to its detected routes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avroutedetector)*