# SRMessagesUsageReport

**Framework**: SensorKit  
**Kind**: class

An object that describes the user’s Messages app activity over a period of time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRMessagesUsageReport
```

#### Overview

This object describes the frequency that the user sends or receives messages, and the relative amount of time the user uses the Messages app.

The [`messagesUsageReport`](srsensor/messagesusagereport.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Analyzing Message Use
- [var duration: TimeInterval](srmessagesusagereport/duration.md)
  The duration that the report spans.
- [var totalIncomingMessages: Int](srmessagesusagereport/totalincomingmessages.md)
  The number of messages the user receives.
- [var totalOutgoingMessages: Int](srmessagesusagereport/totaloutgoingmessages.md)
  The number of messages the user sends.
- [var totalUniqueContacts: Int](srmessagesusagereport/totaluniquecontacts.md)
  The user’s number of contacts.

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
- [class SRPhoneUsageReport](srphoneusagereport.md)
  An object that describes the user’s phone activity over a period of time.
- [class SRVisit](srvisit.md)
  The user’s progress in their daily travel routine.
- [class SRWristDetection](srwristdetection.md)
  The configuration of a watch on the wearer’s wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport)*