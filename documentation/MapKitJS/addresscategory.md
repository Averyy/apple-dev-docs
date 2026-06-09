# AddressCategory

**Framework**: MapKit JS  
**Kind**: enum

The categories of address components that users can search for with an address filter.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
const AddressCategory: Readonly<{
    readonly Country: "Country";
    readonly AdministrativeArea: "AdministrativeArea";
    readonly SubAdministrativeArea: "SubAdministrativeArea";
    readonly Locality: "Locality";
    readonly SubLocality: "SubLocality";
    readonly PostalCode: "PostalCode";
}>
type AddressCategory =
    (typeof AddressCategory)[keyof typeof AddressCategory];
```

## Topics

### Category values
- [AdministrativeArea](addresscategory/administrativearea.md)
  The primary administrative divisions of countries or regions.
- [Country](addresscategory/country.md)
  Countries and regions.
- [Locality](addresscategory/locality.md)
  Local administrative divisions, postal cities, and populated places.
- [PostalCode](addresscategory/postalcode.md)
  An address code for mail sorting and delivery.
- [SubAdministrativeArea](addresscategory/subadministrativearea.md)
  The secondary administrative divisions of countries or regions.
- [SubLocality](addresscategory/sublocality.md)
  Local administrative subdivisions, postal city subdistricts, and neighborhoods.

## See Also

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
- [const TransportType](transporttype.md)
  The modes of transportation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/addresscategory)*