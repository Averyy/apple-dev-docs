# SRVisit

**Framework**: SensorKit  
**Kind**: class

The user’s progress in their daily travel routine.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRVisit
```

#### Overview

The [`visits`](srsensor/visits.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Identifying a Visit
- [var identifier: UUID](srvisit/identifier.md)
  A value that maps to a unique geographic location.
### Accessing Visit Information
- [var arrivalDateInterval: DateInterval](srvisit/arrivaldateinterval.md)
  A range of time within which the user arrives at a location of interest.
- [var departureDateInterval: DateInterval](srvisit/departuredateinterval.md)
  A range of time within which the user departs from a location of interest.
- [var distanceFromHome: CLLocationDistance](srvisit/distancefromhome.md)
  The location’s distance from the home-category location.
- [var locationCategory: SRVisit.LocationCategory](srvisit/locationcategory-swift.property.md)
  The location’s type.
- [SRVisit.LocationCategory](srvisit/locationcategory-swift.enum.md)
  Types of locations.

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
- [class SRWristDetection](srwristdetection.md)
  The configuration of a watch on the wearer’s wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srvisit)*