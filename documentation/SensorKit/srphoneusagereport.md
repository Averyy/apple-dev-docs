# SRPhoneUsageReport

**Framework**: SensorKit  
**Kind**: class

An object that describes the user’s phone activity over a period of time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRPhoneUsageReport
```

#### Overview

This object describes the frequency that a device makes or receives phone calls, and the relative amount of time the user is on a call.

The [`phoneUsageReport`](srsensor/phoneusagereport.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Analyzing Phone Use
- [var duration: TimeInterval](srphoneusagereport/duration.md)
  The duration that the report spans.
- [var totalIncomingCalls: Int](srphoneusagereport/totalincomingcalls.md)
  The number of calls the user receives.
- [var totalOutgoingCalls: Int](srphoneusagereport/totaloutgoingcalls.md)
  The number of calls the user makes.
- [var totalPhoneCallDuration: TimeInterval](srphoneusagereport/totalphonecallduration.md)
  The total duration of all calls.
- [var totalUniqueContacts: Int](srphoneusagereport/totaluniquecontacts.md)
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
- [class SRMessagesUsageReport](srmessagesusagereport.md)
  An object that describes the user’s Messages app activity over a period of time.
- [class SRVisit](srvisit.md)
  The user’s progress in their daily travel routine.
- [class SRWristDetection](srwristdetection.md)
  The configuration of a watch on the wearer’s wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphoneusagereport)*