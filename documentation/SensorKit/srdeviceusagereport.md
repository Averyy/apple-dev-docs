# SRDeviceUsageReport

**Framework**: SensorKit  
**Kind**: class

The frequency and relative duration that the user uses their device, particular Apple apps, or websites.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRDeviceUsageReport
```

#### Overview

The [`deviceUsageReport`](srsensor/deviceusagereport.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Summarizing Device Use
- [var duration: TimeInterval](srdeviceusagereport/duration.md)
  The duration that the report spans.
- [var totalScreenWakes: Int](srdeviceusagereport/totalscreenwakes.md)
  The total number of screen wakes for the device.
- [var totalUnlocks: Int](srdeviceusagereport/totalunlocks.md)
  The total number of unlocks for the device.
- [var totalUnlockDuration: TimeInterval](srdeviceusagereport/totalunlockduration.md)
  The duration of time the device is in an unlocked state.
### Analyzing App Use
- [var applicationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.ApplicationUsage]]](srdeviceusagereport/applicationusagebycategory.md)
  The usage time of apps per category.
- [SRDeviceUsageReport.ApplicationUsage](srdeviceusagereport/applicationusage.md)
  An object that describes the user’s app activity over a period of time.
- [SRDeviceUsageReport.CategoryKey](srdeviceusagereport/categorykey.md)
  Categories of apps or websites that the user uses.
### Analyzing Notification Use
- [var notificationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.NotificationUsage]]](srdeviceusagereport/notificationusagebycategory.md)
  The frequency of notifications per category.
- [SRDeviceUsageReport.NotificationUsage](srdeviceusagereport/notificationusage.md)
  An object that describes notification frequency and the manner in which the user interacts with notifications.
### Analyzing Web Use
- [var webUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.WebUsage]]](srdeviceusagereport/webusagebycategory.md)
  The amount of time the user accesses domains per category.
- [SRDeviceUsageReport.WebUsage](srdeviceusagereport/webusage.md)
  An object that describes a user’s website usage.
### Getting algorithm information
- [var version: String](srdeviceusagereport/version.md)
  The version of the algorithm that the system uses to generate the report.

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
- [class SRWristDetection](srwristdetection.md)
  The configuration of a watch on the wearer’s wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport)*