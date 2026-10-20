# isRouteDetectionEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (getter=isRouteDetectionEnabled) BOOL routeDetectionEnabled;
```

#### Discussion

The default value is [`false`](../../Swift/false.md).

> **Note**:  Enabling route detection significantly increases power consumption. Turn it off when you no longer need it.

## See Also

### Detecting routes
- [var multipleRoutesDetected: Bool](./multipleroutesdetected.md)
  A Boolean value that indicates whether the object detects more than one playback route.
- [static let AVRouteDetectorMultipleRoutesDetectedDidChange: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/avroutedetectormultipleroutesdetecteddidchange.md)
  A notification the system posts when changes occur to its detected routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avroutedetector/isroutedetectionenabled)*