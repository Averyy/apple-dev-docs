# SRMediaEvent

**Framework**: SensorKit  
**Kind**: class

A user interaction with a media object, such as an image or a video.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
class SRMediaEvent
```

## Topics

### Identifying Media Objects
- [var mediaIdentifier: String](srmediaevent/mediaidentifier.md)
  A unique identifier for the media object.
### Tracking Media Events
- [var eventType: SRMediaEventType](srmediaevent/eventtype.md)
  The type of user interaction with the media.
- [enum SRMediaEventType](srmediaeventtype.md)
  The types of user interaction with media that the sensor tracks.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SRAmbientLightSample](srambientlightsample.md)
  The amount of ambient light in the user’s environment.
- [class SRDeviceUsageReport](srdeviceusagereport.md)
  The frequency and relative duration that the user uses their device, particular Apple apps, or websites.
- [class SRKeyboardMetrics](srkeyboardmetrics.md)
  The configuration of a device’s keyboard and its usage patterns.
- [class SRMessagesUsageReport](srmessagesusagereport.md)
  An object that describes the user’s Messages app activity over a period of time.
- [class SRPhoneUsageReport](srphoneusagereport.md)
  An object that describes the user’s phone activity over a period of time.
- [class SRVisit](srvisit.md)
  The user’s progress in their daily travel routine.
- [class SRWristDetection](srwristdetection.md)
  The configuration of a watch on the wearer’s wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srmediaevent)*