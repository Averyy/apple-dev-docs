# language

**Framework**: MapKit JS  
**Kind**: property

A language ID that determines the language to use for displaying addresses.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string language;
```

#### Discussion

When you set the [`language`](mapkit.geocoder/language.md) attribute to a language ID (such as `fr-CA` or `en-GB`), the geocoder returns addresses in this language, if available. If [`language`](mapkit.geocoder/language.md) isn’t set when initializing a [`mapkit.Geocoder`](mapkit.geocoder/mapkit.geocoder.md) object, then the geocoder uses the language provided when you initialized mapkit.

The default value is `null`. The language can be unset by setting [`language`](mapkit.geocoder/language.md) to `null` or `undefined`.

## See Also

- [mapkit.Geocoder](mapkit.geocoder/mapkit.geocoder.md)
  Creates a geocoder object and sets optional language and user location properties.
- [GeocoderConstructorOptions](geocoderconstructoroptions.md)
  Initialization options for geocoder objects.
- [getsUserLocation](mapkit.geocoder/getsuserlocation.md)
  A Boolean value that indicates whether the geocoder returns results near the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.geocoder/language)*