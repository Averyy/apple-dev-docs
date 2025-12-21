# Service

**Framework**: MapKit JS  
**Kind**: class

An abstract class that provides common interfaces for service objects.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
abstract class Service
```

#### Discussion

You can’t initialize an abstract class. Use specific service classes to create service objects.

## Topics

### Instance Properties
- [getsUserLocation](service/getsuserlocation.md)
  A Boolean value that indicates whether the request returns results near a person’s location.
- [language](service/language.md)
  A language ID that determines the language to use for displaying addresses.
### Instance Methods
- [cancel(id)](service/cancel.md)
  Cancels a request using the provided request ID.

## Relationships

### Inherited By
- [Directions](directions.md)
- [Geocoder](geocoder.md)
- [PlaceLookup](placelookup.md)
- [PointsOfInterestSearch](pointsofinterestsearch.md)
- [Search](search.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/service)*