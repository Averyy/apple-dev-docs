# AnnotationDisplayPriority

**Framework**: MapKit JS  
**Kind**: enum

Constants that indicate the priority for displaying annotations on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const AnnotationDisplayPriority: Readonly<{
    readonly Low: 250;
    readonly High: 750;
    readonly Required: 1000;
}>
type AnnotationDisplayPriority =
    (typeof AnnotationDisplayPriority)[keyof typeof AnnotationDisplayPriority];
```

## Topics

### Display priority values
- [High](annotationdisplaypriority/high.md)
  A high display priority, with a preset value of 750 out of 1000.
- [Low](annotationdisplaypriority/low.md)
  A low display priority, with a preset value of 250 out of 1000.
- [Required](annotationdisplaypriority/required.md)
  The highest display priority, with a preset value of 1000 out of 1000.

## See Also

- [const AddressCategory](addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [const AnnotationCollisionMode](annotationcollisionmode.md)
  Constants that indicate the collision mode for an annotation.
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
- [const RegionPriority](regionpriority.md)
  A value that indicates the importance of the configured region.
- [const TransportType](transporttype.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationdisplaypriority)*