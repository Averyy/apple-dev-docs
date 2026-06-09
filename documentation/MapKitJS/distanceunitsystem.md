# DistanceUnitSystem

**Framework**: MapKit JS  
**Kind**: enum

Constants that indicate the system of measurement that displays on the map.

**Availability**:
- MapKit JS 5.13+

## Declaration

```swift
const DistanceUnitSystem: Readonly<{
    readonly Adaptive: "adaptive";
    readonly Metric: "metric";
    readonly Imperial: "imperial";
}>
type DistanceUnitSystem =
    (typeof DistanceUnitSystem)[keyof typeof DistanceUnitSystem];
```

#### Overview

Use these constants with the map’s [`distances`](map/distances-data.property.md) property.

## Topics

### Distance values
- [Adaptive](distanceunitsystem/adaptive.md)
  A measurement system that adapts to the map’s language.
- [Metric](distanceunitsystem/metric.md)
  The metric measurement system.
- [Imperial](distanceunitsystem/imperial.md)
  The imperial measurement system.

## See Also

- [const AddressCategory](addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [const AnnotationCollisionMode](annotationcollisionmode.md)
  Constants that indicate the collision mode for an annotation.
- [const AnnotationDisplayPriority](annotationdisplaypriority.md)
  Constants that indicate the priority for displaying annotations on the map.
- [const ColorScheme](colorscheme.md)
  Constants that indicate the color scheme of the map or a place detail.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/distanceunitsystem)*