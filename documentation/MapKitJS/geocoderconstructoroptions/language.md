# language

**Framework**: MapKit JS  
**Kind**: property

An initial value for the language ID, which determines the language to use for displaying addresses.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string language;
```

#### Discussion

If you don’t set [`language`](geocoderconstructoroptions/language.md) during initialization, the geocoder uses the value you provide during MapKit initialization ([`language`](mapkitinitoptions/language.md)).

Use standard two-letter ISO language IDs and two-letter region designators.

## See Also

- [getsUserLocation](geocoderconstructoroptions/getsuserlocation.md)
  An initial Boolean value that indicates whether the geocoder returns results near the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderconstructoroptions/language)*