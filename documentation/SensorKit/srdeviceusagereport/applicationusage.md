# SRDeviceUsageReport.ApplicationUsage

**Framework**: SensorKit  
**Kind**: class

An object that describes the user’s app activity over a period of time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class ApplicationUsage
```

#### Overview

Each instance of this class represents an app in a particular app category. For more information, see [`applicationUsageByCategory`](srdeviceusagereport/applicationusagebycategory.md).

## Topics

### Identifying the App
- [var bundleIdentifier: String?](srdeviceusagereport/applicationusage/bundleidentifier.md)
  The bundle identifier of the app in use.
- [var reportApplicationIdentifier: String](srdeviceusagereport/applicationusage/reportapplicationidentifier.md)
  A pseudonymn for a real application identifier.
- [var supplementalCategories: [SRSupplementalCategory]](srdeviceusagereport/applicationusage/supplementalcategories.md)
  Categories that provide more information about an app.
- [class SRSupplementalCategory](srsupplementalcategory.md)
  A more detailed category that provides additional context to the app category.
### Timing App Use
- [var usageTime: TimeInterval](srdeviceusagereport/applicationusage/usagetime.md)
  The amount of time the user uses the app.
- [var relativeStartTime: TimeInterval](srdeviceusagereport/applicationusage/relativestarttime.md)
  The time the user starts the app relative to the start time of the first app in a report interval.
### Inspecting Text Input
- [var textInputSessions: [SRTextInputSession]](srdeviceusagereport/applicationusage/textinputsessions.md)
  The text input session types that occur during application usage.
- [class SRTextInputSession](srtextinputsession.md)
  The characters a user types for a particular keyboard.

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

- [var applicationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.ApplicationUsage]]](srdeviceusagereport/applicationusagebycategory.md)
  The usage time of apps per category.
- [SRDeviceUsageReport.CategoryKey](srdeviceusagereport/categorykey.md)
  Categories of apps or websites that the user uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage)*