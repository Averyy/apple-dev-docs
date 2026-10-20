# departureDateInterval

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

A range of time within which the user departs from a location of interest.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var departureDateInterval: DateInterval { get }
```

```objc
@property (strong, readonly) NSDateInterval * departureDateInterval;
```

## See Also

### Accessing Visit Information
- [var arrivalDateInterval: DateInterval](./arrivaldateinterval.md)
  A range of time within which the user arrives at a location of interest.
- [var distanceFromHome: CLLocationDistance](./distancefromhome.md)
  The location’s distance from the home-category location.
- [var locationCategory: SRVisit.LocationCategory](./locationcategory-swift.property.md)
  The location’s type.
- [SRVisit.LocationCategory](./locationcategory-swift.enum.md)
  Types of locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srvisit/departuredateinterval)*