# SRDeviceUsageReport.ApplicationUsage

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

An object that describes the user’s app activity over a period of time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class ApplicationUsage
```

```objc
@interface SRApplicationUsage : NSObject
```

#### Overview

Each instance of this class represents an app in a particular app category. For more information, see [`applicationUsageByCategory`](./applicationusagebycategory.md).

## Topics

### Identifying the App
- [var bundleIdentifier: String?](./applicationusage/bundleidentifier.md)
  The bundle identifier of the app in use.
- [var reportApplicationIdentifier: String](./applicationusage/reportapplicationidentifier.md)
  A pseudonymn for a real application identifier.
- [var supplementalCategories: [SRSupplementalCategory]](./applicationusage/supplementalcategories.md)
  Categories that provide more information about an app.
- [class SRSupplementalCategory](../srsupplementalcategory.md)
  A more detailed category that provides additional context to the app category.
### Timing App Use
- [var usageTime: TimeInterval](./applicationusage/usagetime.md)
  The amount of time the user uses the app.
- [var relativeStartTime: TimeInterval](./applicationusage/relativestarttime.md)
  The time the user starts the app relative to the start time of the first app in a report interval.
### Inspecting Text Input
- [var textInputSessions: [SRTextInputSession]](./applicationusage/textinputsessions.md)
  The text input session types that occur during application usage.
- [class SRTextInputSession](../srtextinputsession.md)
  The characters a user types for a particular keyboard.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Analyzing App Use
- [var applicationUsageByCategory: [SRDeviceUsageReport.CategoryKey : [SRDeviceUsageReport.ApplicationUsage]]](./applicationusagebycategory.md)
  The usage time of apps per category.
- [SRDeviceUsageReport.CategoryKey](./categorykey.md)
  Categories of apps or websites that the user uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage)*