# SRVisit.LocationCategory

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

Types of locations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum LocationCategory
```

```c
enum SRLocationCategory : NSInteger;
```

## Topics

### Categories
- [SRVisit.LocationCategory.gym](./locationcategory-swift.enum/gym.md)
  The user’s gym.
- [SRVisit.LocationCategory.home](./locationcategory-swift.enum/home.md)
  The user’s home.
- [SRVisit.LocationCategory.school](./locationcategory-swift.enum/school.md)
  The user’s school.
- [SRVisit.LocationCategory.unknown](./locationcategory-swift.enum/unknown.md)
  A location the user frequents that’s an unknown type.
- [SRVisit.LocationCategory.work](./locationcategory-swift.enum/work.md)
  The user’s workplace.
### Initializers
- [init?(rawValue: Int)](./locationcategory-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Visit Information
- [var arrivalDateInterval: DateInterval](./arrivaldateinterval.md)
  A range of time within which the user arrives at a location of interest.
- [var departureDateInterval: DateInterval](./departuredateinterval.md)
  A range of time within which the user departs from a location of interest.
- [var distanceFromHome: CLLocationDistance](./distancefromhome.md)
  The location’s distance from the home-category location.
- [var locationCategory: SRVisit.LocationCategory](./locationcategory-swift.property.md)
  The location’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srvisit/locationcategory-swift.enum)*