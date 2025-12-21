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
### Type Aliases
- [type AddressCategory](addresscategory/addresscategory.md)
  A type alias that represents address category values.

## See Also

- [class AddressFilter](addressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [class Search](search.md)
  An object that retrieves map-based search results for a user-entered query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/addresscategory)*