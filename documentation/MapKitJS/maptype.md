# MapType

**Framework**: MapKit JS  
**Kind**: enum

Constants representing the type of map to display.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const MapType: Readonly<{
    readonly Satellite: "satellite";
    readonly Hybrid: "hybrid";
    readonly MutedStandard: "mutedStandard";
    readonly Standard: "standard";
}>
type MapType = (typeof MapType)[keyof typeof MapType];
```

## Mentions

- [MapKit JS 6](mapkit-js-6.md)

## Topics

### Map type values
- [Hybrid](maptype/hybrid.md)
  A satellite image of the area with road and road name layers on top.
- [MutedStandard](maptype/mutedstandard.md)
  A street map that emphasizes your data over the underlying map details.
- [Satellite](maptype/satellite.md)
  A satellite image of the area.
- [Standard](maptype/standard.md)
  A street map that shows the position of all roads and some road names.

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
- [const PointOfInterestCategory](pointofinterestcategory.md)
  Point-of-interest categories.
- [const RegionPriority](regionpriority.md)
  A value that indicates the importance of the configured region.
- [const TransportType](transporttype.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/maptype)*