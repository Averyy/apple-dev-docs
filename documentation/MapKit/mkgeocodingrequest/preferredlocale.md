# preferredLocale

**Framework**: MapKit  
**Kind**: property

A value that indicates the default locale the geocoder should use when processing requests.

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
var preferredLocale: Locale? { get set }
```

## See Also

- [var addressString: String](mkgeocodingrequest/addressstring.md)
  The string used to initialize the geocoder.
- [func getMapItems(completionHandler: ([MKMapItem]?, (any Error)?) -> Void)](mkgeocodingrequest/getmapitems(completionhandler:).md)
  Returns the map items relevant to the geocoded location.
- [var region: MKCoordinateRegion](mkgeocodingrequest/region.md)
  The geographic region for the framework to use as the bounds for the request; defaults to a region that covers the whole world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeocodingrequest/preferredlocale)*