# preferredLocale

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, nullable) NSLocale * preferredLocale;
```

## See Also

### Getting information about the geocoder
- [var addressString: String](./addressstring.md)
  The string used to initialize the geocoder.
- [func getMapItems(completionHandler: ([MKMapItem]?, (any Error)?) -> Void)](./getmapitems%28completionhandler%29.md)
  Returns the map items relevant to the geocoded location.
- [var region: MKCoordinateRegion](./region.md)
  The geographic region for the framework to use as the bounds for the request; defaults to a region that covers the whole world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkgeocodingrequest/preferredlocale)*