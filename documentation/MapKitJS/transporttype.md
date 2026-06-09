# TransportType

**Framework**: MapKit JS  
**Kind**: enum

The modes of transportation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const TransportType: Readonly<{
    readonly Automobile: "AUTOMOBILE";
    readonly Walking: "WALKING";
    readonly Cycling: "CYCLING";
}>
type TransportType = (typeof TransportType)[keyof typeof TransportType];
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

Constants that describe the mode of transportation in [`DirectionsRequest`](directionsrequest.md) and [`DirectionsResponse`](directionsresponse.md).

## Topics

### Transport types
- [Walking](transporttype/walking.md)
  A constant identifying the mode of transportation as walking.
- [Automobile](transporttype/automobile.md)
  A constant identifying the mode of transportation as driving.
- [Cycling](transporttype/cycling.md)
  A constant identifying the mode of transportation as cycling.

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
- [const RegionPriority](regionpriority.md)
  A value that indicates the importance of the configured region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/transporttype)*