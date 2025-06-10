# AVCaptureSceneMonitoringStatus

**Framework**: AVFoundation  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct AVCaptureSceneMonitoringStatus
```

#### Overview

Some features have certain requirements on the scene (lighting condition for Cinematic Video, for example) to produce optimal results; these AVCaptureSceneMonitoringStatus string constants are used to represent such scene statuses for a given feature.

## Topics

### Initializers
- [init(rawValue: String)](avcapturescenemonitoringstatus/init(rawvalue:).md)
### Type Properties
- [static let notEnoughLight: AVCaptureSceneMonitoringStatus](avcapturescenemonitoringstatus/notenoughlight.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescenemonitoringstatus)*