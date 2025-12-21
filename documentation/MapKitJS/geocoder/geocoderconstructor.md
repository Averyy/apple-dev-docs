# new Geocoder(options)

**Framework**: MapKit JS  
**Kind**: init

Creates a geocoder object and sets optional language and user location properties.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(options?: ServiceConstructorOptions);
```

#### Discussion

To use geocoding, create an instance of [`Geocoder`](geocoder.md). Optionally, you can set the [`language`](serviceconstructoroptions/language.md) and [`getsUserLocation`](serviceconstructoroptions/getsuserlocation.md) properties of a [`Geocoder`](geocoder.md) object on initialization, as the following examples shows:

```javascript
const geocoder = new mapkit.Geocoder({
    language: "en-GB",
    getsUserLocation: true
});
```

## See Also

- [interface ServiceConstructorOptions](serviceconstructoroptions.md)
  Common options you provide when you create a service object.
- [getsUserLocation](service/getsuserlocation.md)
  A Boolean value that indicates whether the request returns results near a person’s location.
- [language](service/language.md)
  A language ID that determines the language to use for displaying addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoder/geocoderconstructor)*