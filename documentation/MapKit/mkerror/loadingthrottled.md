# loadingThrottled

**Framework**: MapKit  
**Kind**: property  
**Role**: Type Property

The data didn’t load because data throttling is in effect.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
static var loadingThrottled: MKError.Code { get }
```

#### Discussion

This error can occur if an app makes frequent requests for data over a short period of time.

## See Also

### Error codes
- [static var decodingFailed: MKError.Code](./decodingfailed.md)
  GeoJSON decoding failed.
- [static var directionsNotFound: MKError.Code](./directionsnotfound.md)
  Directions to the specified location aren’t available.
- [static var placemarkNotFound: MKError.Code](./placemarknotfound.md)
  The framework couldn’t find the specified placemark.
- [static var serverFailure: MKError.Code](./serverfailure.md)
  The map server was unable to return the desired information.
- [static var unknown: MKError.Code](./unknown.md)
  An unknown error occurred.
- [MKError.Code](./code.md)
  Error constants for the MapKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkerror/loadingthrottled)*