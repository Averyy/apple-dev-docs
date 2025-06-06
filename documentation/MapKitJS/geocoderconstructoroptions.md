# GeocoderConstructorOptions

**Framework**: MapKit JS  
**Kind**: struct

Initialization options for geocoder objects.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary GeocoderConstructorOptions {
	string language;
	boolean getsUserLocation;
};
```

#### Overview

You can optionally set the [`language`](mapkit.geocoder/language.md) and [`getsUserLocation`](mapkit.geocoder/getsuserlocation.md) properties of a [`mapkit.Geocoder`](mapkit.geocoder/mapkit.geocoder.md) object on initialization. Provide a dictionary of [`GeocoderConstructorOptions`](geocoderconstructoroptions.md), as shown in the following code listing.

```javascript
var geocoder = new mapkit.Geocoder({
    language: "en-GB",
    getsUserLocation: true
});
```

## Topics

### Initializing options
- [getsUserLocation](geocoderconstructoroptions/getsuserlocation.md)
  An initial Boolean value that indicates whether the geocoder returns results near the user’s location.
- [language](geocoderconstructoroptions/language.md)
  An initial value for the language ID, which determines the language to use for displaying addresses.

## See Also

- [mapkit.Geocoder](mapkit.geocoder/mapkit.geocoder.md)
  Creates a geocoder object and sets optional language and user location properties.
- [getsUserLocation](mapkit.geocoder/getsuserlocation.md)
  A Boolean value that indicates whether the geocoder returns results near the user’s location.
- [language](mapkit.geocoder/language.md)
  A language ID that determines the language to use for displaying addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderconstructoroptions)*