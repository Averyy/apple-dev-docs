# getMapItems(completionHandler:)

**Framework**: MapKit  
**Kind**: method

Returns the map items relevant to the geocoded location.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var mapItems: [MKMapItem] { get async throws }
```

## See Also

- [var addressString: String](mkgeocodingrequest/addressstring.md)
  The string used to initialize the geocoder.
- [var preferredLocale: Locale?](mkgeocodingrequest/preferredlocale.md)
  A value that indicates the default locale the geocoder should use when processing requests.
- [var region: MKCoordinateRegion](mkgeocodingrequest/region.md)
  The geographic region for the framework to use as the bounds for the request; defaults to a region that covers the whole world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeocodingrequest/getmapitems(completionhandler:))*