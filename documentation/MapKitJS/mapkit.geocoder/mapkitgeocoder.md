# mapkit.Geocoder

**Framework**: MapKit JS  
**Kind**: init

Creates a geocoder object and sets optional language and user location properties.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.Geocoder(
	optional GeocoderConstructorOptions options
);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

To use geocoding, create an instance of [`mapkit.Geocoder`](mapkit.geocoder/mapkit.geocoder.md). Optionally, you can set the [`language`](mapkit.geocoder/language.md) and [`getsUserLocation`](mapkit.geocoder/getsuserlocation.md) properties of a [`mapkit.Geocoder`](mapkit.geocoder/mapkit.geocoder.md) object on initialization, as the following examples shows:

```javascript
const geocoder = new mapkit.Geocoder({
    language: "en-GB",
    getsUserLocation: true
});
```

## See Also

- [GeocoderConstructorOptions](geocoderconstructoroptions.md)
  Initialization options for geocoder objects.
- [getsUserLocation](mapkit.geocoder/getsuserlocation.md)
  A Boolean value that indicates whether the geocoder returns results near the user’s location.
- [language](mapkit.geocoder/language.md)
  A language ID that determines the language to use for displaying addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.geocoder/mapkit.geocoder)*