# SRWristDetection

**Framework**: SensorKit  
**Kind**: class

The configuration of a watch on the wearer’s wrist.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRWristDetection
```

#### Overview

The [`onWristState`](srsensor/onwriststate.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Inspecting Watch Configuration
- [var crownOrientation: SRWristDetection.CrownOrientation](srwristdetection/crownorientation-swift.property.md)
  A value that indicates the direction the Digital Crown faces with respect to the user.
- [SRWristDetection.CrownOrientation](srwristdetection/crownorientation-swift.enum.md)
  Directions the Digital Crown can face with respect to the wearer.
- [var onWrist: Bool](srwristdetection/onwrist.md)
  A value that indicates whether the watch is on the user’s wrist.
- [var onWristDate: Date?](srwristdetection/onwristdate.md)
  The date and time that the user puts their Apple Watch on their wrist.
- [var offWristDate: Date?](srwristdetection/offwristdate.md)
  The date and time that the user takes their Apple Watch off their wrist.
- [var wristLocation: SRWristDetection.WristLocation](srwristdetection/wristlocation-swift.property.md)
  A value that indicates the wrist where the user wears the watch.
- [SRWristDetection.WristLocation](srwristdetection/wristlocation-swift.enum.md)
  Preferences for where a user wears a watch.

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

## See Also

- [class SRAmbientLightSample](srambientlightsample.md)
  The amount of ambient light in the user’s environment.
- [class SRDeviceUsageReport](srdeviceusagereport.md)
  The frequency and relative duration that the user uses their device, particular Apple apps, or websites.
- [class SRKeyboardMetrics](srkeyboardmetrics.md)
  The configuration of a device’s keyboard and its usage patterns.
- [class SRMediaEvent](srmediaevent.md)
  A user interaction with a media object, such as an image or a video.
- [class SRMessagesUsageReport](srmessagesusagereport.md)
  An object that describes the user’s Messages app activity over a period of time.
- [class SRPhoneUsageReport](srphoneusagereport.md)
  An object that describes the user’s phone activity over a period of time.
- [class SRVisit](srvisit.md)
  The user’s progress in their daily travel routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristdetection)*