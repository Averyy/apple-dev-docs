# Place

**Framework**: MapKit JS  
**Kind**: struct

A place object that returns from a geocoder lookup, a reverse lookup, or a fetch request for points of interest.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary Place {
	string name;
	string? id;
	string[]? alternateIds;
	mapkit.Coordinate coordinate;
	string formattedAddress;
	mapkit.CoordinateRegion region;
	string countryCode;
	mapkit.PointOfInterestCategory pointOfInterestCategory;
	string? country;
	string? administrativeArea;
	string? administrativeAreaCode;
	string? locality;
	string? postCode;
	string? subLocality;
	string? thoroughfare;
	string? subThoroughfare;
	string? fullThoroughfare;
	string[]? areasOfInterest;
	string[]? dependentLocalities;
};
```

#### Overview

[`GeocoderResponse`](geocoderresponse.md), [`SearchResponse`](searchresponse.md), and [`PointsOfInterestSearchResponse`](pointsofinterestsearchresponse.md) return places.

## Topics

### Place name and category
- [name](place/name.md)
  The name of the place.
- [formattedAddress](place/formattedaddress.md)
  The address of the place, formatted using its conventions of its country or region.
- [areasOfInterest](place/areasofinterest.md)
  Common names of the area in which the place resides.
- [pointOfInterestCategory](place/pointofinterestcategory.md)
  The category of the place.
### Street address
- [thoroughfare](place/thoroughfare.md)
  The street name at the place.
- [subThoroughfare](place/subthoroughfare.md)
  The number on the street at the place.
- [fullThoroughfare](place/fullthoroughfare.md)
  A combination of thoroughfare and subthoroughfare.
- [postCode](place/postcode.md)
  The postal code of the place.
### City and district address
- [locality](place/locality.md)
  The city of the place.
- [subLocality](place/sublocality.md)
  The name of the area within the locality.
- [dependentLocalities](place/dependentlocalities.md)
  Common names for the local area or neighborhood of the place.
- [administrativeArea](place/administrativearea.md)
  The state or province of the place.
- [administrativeAreaCode](place/administrativeareacode.md)
  The short code for the state or area.
### Country address
- [country](place/country.md)
  The country or region of the place.
- [countryCode](place/countrycode.md)
  The country or region associated with the place.
### Location
- [coordinate](place/coordinate.md)
  The latitude and longitude for the place.
- [region](place/region.md)
  The geographic region associated with the place.
### Place IDs
- [id](place/id.md)
  The Place ID referencing a feature.
- [alternateIds](place/alternateids.md)
  A list of alternate Place IDs referencing a feature.

## See Also

- [PlaceDetailOptions](placedetailoptions.md)
- [mapkit.PlaceLookup](mapkit.placelookup.md)
  An object that provides the ability to look up place information for a specified Place ID.
- [placeDetails](mapkit/placedetails.md)
  A list of all user-created place detail objects that are currently active on a page.
- [PlaceLookupOptions](placelookupoptions.md)
  The options for creating a place lookup.
- [PlaceSelectionAccessoryOptions](placeselectionaccessoryoptions.md)
  The options for selection accessories.
- [mapkit.PlaceAnnotation](mapkit.placeannotation.md)
  An annotation for a place.
- [mapkit.PlaceDetail](mapkit.placedetail.md)
  An interactive view that displays information about a place.
- [mapkit.PlaceSelectionAccessory](mapkit.placeselectionaccessory.md)
  The accessory that conveys information about a place associated with an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/place)*