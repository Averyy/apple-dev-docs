# serverFailure

**Framework**: MapKit  
**Kind**: property

The map server was unable to return the desired information.

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
static var serverFailure: MKError.Code { get }
```

## See Also

- [static var decodingFailed: MKError.Code](mkerror/decodingfailed.md)
  GeoJSON decoding failed.
- [static var directionsNotFound: MKError.Code](mkerror/directionsnotfound.md)
  Directions to the specified location aren’t available.
- [static var loadingThrottled: MKError.Code](mkerror/loadingthrottled.md)
  The data didn’t load because data throttling is in effect.
- [static var placemarkNotFound: MKError.Code](mkerror/placemarknotfound.md)
  The framework couldn’t find the specified placemark.
- [static var unknown: MKError.Code](mkerror/unknown.md)
  An unknown error occurred.
- [MKError.Code](mkerror/code.md)
  Error constants for the MapKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkerror/serverfailure)*