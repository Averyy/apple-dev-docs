# mapkit.AddressCategory

**Framework**: MapKit JS  
**Kind**: enum

The categories of address components that users can search for with an address filter.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
interface mapkit.AddressCategory {
	const string Country;
	const string AdministrativeArea;
	const string SubAdministrativeArea;
	const string Locality;
	const string SubLocality;
	const string PostalCode;
};
```

## Topics

### Category values
- [AdministrativeArea](mapkit.addresscategory/administrativearea.md)
  The primary administrative divisions of countries or regions.
- [Country](mapkit.addresscategory/country.md)
  Countries and regions.
- [Locality](mapkit.addresscategory/locality.md)
  Local administrative divisions, postal cities, and populated places.
- [PostalCode](mapkit.addresscategory/postalcode.md)
  An address code for mail sorting and delivery.
- [SubAdministrativeArea](mapkit.addresscategory/subadministrativearea.md)
  The secondary administrative divisions of countries or regions.
- [SubLocality](mapkit.addresscategory/sublocality.md)
  Local administrative subdivisions, postal city subdistricts, and neighborhoods.

## See Also

- [mapkit.AddressFilter](mapkit.addressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [mapkit.Search](mapkit.search.md)
  An object that retrieves map-based search results for a user-entered query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.addresscategory)*