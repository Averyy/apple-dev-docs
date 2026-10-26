# AVRouteDetector

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVRouteDetector : NSObject
```

## Mentions

- [Supporting AirPlay in your app](./supporting-airplay-in-your-app.md)

#### Overview

If you enable route detection, the object reports whether it detects multiple playback routes. If it does, use [`AVRoutePickerView`](../AVKit/avroutepickerview.md) to present the UI for the user to select an appropriate route.

## Topics

### Detecting routes
- [var isRouteDetectionEnabled: Bool](./avroutedetector/isroutedetectionenabled.md)
  A Boolean value that indicates whether route detection is in an enabled state.
- [var multipleRoutesDetected: Bool](./avroutedetector/multipleroutesdetected.md)
  A Boolean value that indicates whether the object detects more than one playback route.
- [static let AVRouteDetectorMultipleRoutesDetectedDidChange: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/avroutedetectormultipleroutesdetecteddidchange.md)
  A notification the system posts when changes occur to its detected routes.
- [AVRouteDetectorMultipleRoutesDetectedDidChangeNotification](./avroutedetectormultipleroutesdetecteddidchangenotification.md)
  A notification the system posts when changes occur to its detected routes.
### Deprecated
- [var detectsCustomRoutes: Bool](./avroutedetector/detectscustomroutes.md)
  A Boolean value that indicates whether route detection includes custom routes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avroutedetector)*