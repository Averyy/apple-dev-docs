# getMapItems(completionHandler:)

**Framework**: MapKit  
**Kind**: method

Returns the map items relevant to the geocoded location.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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