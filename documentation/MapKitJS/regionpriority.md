# RegionPriority

**Framework**: MapKit JS  
**Kind**: enum

A value that indicates the importance of the configured region.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
const RegionPriority: Readonly<{
    readonly Default: "default";
    readonly Required: "required";
}>
type RegionPriority = (typeof RegionPriority)[keyof typeof RegionPriority];
```

## Topics

### Setting the region priority
- [Default](regionpriority/default.md)
  A value indicating that the results can originate from outside the specified region.
- [Required](regionpriority/required.md)
  A value indicating that no results can originate from outside the specified region.

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
- [const MapLoadPriority](maploadpriority.md)
  Constants that prioritize the visibility of specific map features during map loading.
- [const MapType](maptype.md)
  Constants representing the type of map to display.
- [const PointOfInterestCategory](pointofinterestcategory.md)
  Point-of-interest categories.
- [const TransportType](transporttype.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/regionpriority)*