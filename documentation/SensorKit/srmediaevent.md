# SRMediaEvent

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

A user interaction with a media object, such as an image or a video.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
class SRMediaEvent
```

```objc
@interface SRMediaEvent : NSObject
```

## Topics

### Identifying Media Objects
- [var mediaIdentifier: String](./srmediaevent/mediaidentifier.md)
  A unique identifier for the media object.
### Tracking Media Events
- [var eventType: SRMediaEventType](./srmediaevent/eventtype.md)
  The type of user interaction with the media.
- [enum SRMediaEventType](./srmediaeventtype.md)
  The types of user interaction with media that the sensor tracks.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interpreting data
- [class SRAmbientLightSample](./srambientlightsample.md)
  The amount of ambient light in the user’s environment.
- [class SRDeviceUsageReport](./srdeviceusagereport.md)
  The frequency and relative duration that the user uses their device, particular Apple apps, or websites.
- [class SRKeyboardMetrics](./srkeyboardmetrics.md)
  The configuration of a device’s keyboard and its usage patterns.
- [class SRMessagesUsageReport](./srmessagesusagereport.md)
  An object that describes the user’s Messages app activity over a period of time.
- [class SRPhoneUsageReport](./srphoneusagereport.md)
  An object that describes the user’s phone activity over a period of time.
- [class SRVisit](./srvisit.md)
  The user’s progress in their daily travel routine.
- [class SRWristDetection](./srwristdetection.md)
  The configuration of a watch on the wearer’s wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srmediaevent)*