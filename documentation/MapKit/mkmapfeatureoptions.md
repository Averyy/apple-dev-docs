# MKMapFeatureOptions

**Framework**: MapKit  
**Kind**: struct

A structure you use to tell the map which kinds of features users can interact with.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MKMapFeatureOptions
```

## Topics

### Initializers
- [init(rawValue: Int)](mkmapfeatureoptions/init(rawvalue:).md)
  Creates a new feature option structure with the specified value.
### Selecting interactive map features
- [static var physicalFeatures: MKMapFeatureOptions](mkmapfeatureoptions/physicalfeatures.md)
  The option that represents physical map features such as mountain ranges, rivers, and ocean basins.
- [static var pointsOfInterest: MKMapFeatureOptions](mkmapfeatureoptions/pointsofinterest.md)
  The option that represents points of interest such as museums, cafes, parks, or schools.
- [static var territories: MKMapFeatureOptions](mkmapfeatureoptions/territories.md)
  The option that represents territorial boundaries such as a national border, a state boundary, or a neighborhood.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [class MKMapFeatureAnnotation](mkmapfeatureannotation.md)
  A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.
- [class MKMapItemRequest](mkmapitemrequest.md)
  A utility class you use to request additional information about a map feature.
- [class MKIconStyle](mkiconstyle.md)
  A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [class MKPointOfInterestFilter](mkpointofinterestfilter.md)
  A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.
- [struct MKPointOfInterestCategory](mkpointofinterestcategory.md)
  A point of interest category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapfeatureoptions)*