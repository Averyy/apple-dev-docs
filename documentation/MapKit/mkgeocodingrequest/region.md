# region

**Framework**: MapKit  
**Kind**: property

The geographic region for the framework to use as the bounds for the request; defaults to a region that covers the whole world.

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
var region: MKCoordinateRegion { get set }
```

## See Also

- [var addressString: String](mkgeocodingrequest/addressstring.md)
  The string used to initialize the geocoder.
- [func getMapItems(completionHandler: ([MKMapItem]?, (any Error)?) -> Void)](mkgeocodingrequest/getmapitems(completionhandler:).md)
  Returns the map items relevant to the geocoded location.
- [var preferredLocale: Locale?](mkgeocodingrequest/preferredlocale.md)
  A value that indicates the default locale the geocoder should use when processing requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeocodingrequest/region)*