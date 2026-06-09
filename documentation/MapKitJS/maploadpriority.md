# MapLoadPriority

**Framework**: MapKit JS  
**Kind**: enum

Constants that prioritize the visibility of specific map features during map loading.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const MapLoadPriority: Readonly<{
    readonly LandCover: "LandCover";
    readonly PointsOfInterest: "PointsOfInterest";
    readonly None: null;
}>
type MapLoadPriority = (typeof MapLoadPriority)[keyof typeof MapLoadPriority];
```

## Topics

### Prioritizations
- [LandCover](maploadpriority/landcover.md)
  Prioritizes loading of the map land cover and borders, without POIs or labels.
- [PointsOfInterest](maploadpriority/pointsofinterest.md)
  Prioritizes loading of the full standard map, with rendered POIs.
- [None](maploadpriority/none.md)
  Signifies no preference for what to prioritize when loading the map.

## See Also

- [const AddressCategory](addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [const AnnotationCollisionMode](annotationcollisionmode.md)
  Constants that indicate the collision mode for an annotation.
- [const AnnotationDisplayPriority](annotationdisplaypriority.md)
  Constants that indicate the priority for displaying annotations on the map.
- [const ColorScheme](colorscheme.md)
  Constants that indicate the color scheme of the map or a place detail.
- [const DistanceUnitSystem](distanceunitsystem.md)
  Constants that indicate the system of measurement that displays on the map.
- [const FeatureVisibility](featurevisibility.md)
  Constants indicating the visibility of different adaptive map features.
- [const MapFeatureType](mapfeaturetype.md)
  Values that describe the feature type of a point of interest.
- [const MapType](maptype.md)
  Constants representing the type of map to display.
- [const PointOfInterestCategory](pointofinterestcategory.md)
  Point-of-interest categories.
- [const RegionPriority](regionpriority.md)
  A value that indicates the importance of the configured region.
- [const TransportType](transporttype.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/maploadpriority)*