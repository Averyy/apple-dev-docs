# multipleRoutesDetected

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL multipleRoutesDetected;
```

#### Discussion

The system posts a [`AVRouteDetectorMultipleRoutesDetectedDidChangeNotification`](../avroutedetectormultipleroutesdetecteddidchangenotification.md) notification when this property value changes.

## See Also

### Detecting routes
- [var isRouteDetectionEnabled: Bool](./isroutedetectionenabled.md)
  A Boolean value that indicates whether route detection is in an enabled state.
- [static let AVRouteDetectorMultipleRoutesDetectedDidChange: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/avroutedetectormultipleroutesdetecteddidchange.md)
  A notification the system posts when changes occur to its detected routes.
- [AVRouteDetectorMultipleRoutesDetectedDidChangeNotification](../avroutedetectormultipleroutesdetecteddidchangenotification.md)
  A notification the system posts when changes occur to its detected routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avroutedetector/multipleroutesdetected)*