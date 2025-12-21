# getsUserLocation

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that indicates whether the request returns results near a person’s location.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get getsUserLocation(): boolean;
set getsUserLocation(value: boolean);
```

#### Discussion

When set to `true`, the request returns results that are near the user’s current location. The default value is `false`.

## See Also

- [new Geocoder(options)](geocoder/geocoderconstructor.md)
  Creates a geocoder object and sets optional language and user location properties.
- [interface ServiceConstructorOptions](serviceconstructoroptions.md)
  Common options you provide when you create a service object.
- [language](service/language.md)
  A language ID that determines the language to use for displaying addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/service/getsuserlocation)*