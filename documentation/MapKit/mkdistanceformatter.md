# MKDistanceFormatter

**Framework**: MapKit  
**Kind**: class

A utility object that converts between a geographic distance and a string-based expression of that distance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class MKDistanceFormatter
```

#### Overview

Use a distance formatter to display distances to the user or to parse user-specified text to obtain a numerical value for a distance. When formatting strings containing distances, a distance formatter object takes into account the user’s locale and language settings. You can also specify a custom locale or custom units for any distances that you format.

## Topics

### Converting distances
- [func string(fromDistance: CLLocationDistance) -> String](mkdistanceformatter/string(fromdistance:).md)
  Creates a string representation of the specified distance.
- [func distance(from: String) -> CLLocationDistance](mkdistanceformatter/distance(from:).md)
  Returns the distance value parsed from the specified string.
### Specifying the format
- [var locale: Locale!](mkdistanceformatter/locale.md)
  The locale to use when formatting strings.
- [var units: MKDistanceFormatter.Units](mkdistanceformatter/units-swift.property.md)
  The measuring system — imperial or metric — to use for units.
- [MKDistanceFormatter.Units](mkdistanceformatter/units-swift.enum.md)
  Constants that reflect the type of units to use in the string.
- [var unitStyle: MKDistanceFormatter.DistanceUnitStyle](mkdistanceformatter/unitstyle.md)
  The preferred style for units.
- [MKDistanceFormatter.DistanceUnitStyle](mkdistanceformatter/distanceunitstyle.md)
  Constants that indicate the format style to use for strings.

## Relationships

### Inherits From
- [Formatter](../Foundation/Formatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct MKCoordinateRegion](mkcoordinateregion.md)
  A rectangular geographic region that centers around a specific latitude and longitude.
- [struct MKCoordinateSpan](mkcoordinatespan.md)
  The width and height of a map region.
- [struct MKMapRect](mkmaprect.md)
  A rectangular area on a two-dimensional map projection.
- [struct MKMapPoint](mkmappoint.md)
  A point on a two-dimensional map projection.
- [struct MKMapSize](mkmapsize.md)
  Width and height information on a two-dimensional map projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdistanceformatter)*