# MKError

**Framework**: MapKit  
**Kind**: struct

Error constants for the MapKit framework.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
struct MKError
```

## Topics

### Error codes
- [static var decodingFailed: MKError.Code](mkerror/decodingfailed.md)
  GeoJSON decoding failed.
- [static var directionsNotFound: MKError.Code](mkerror/directionsnotfound.md)
  Directions to the specified location aren’t available.
- [static var loadingThrottled: MKError.Code](mkerror/loadingthrottled.md)
  The data didn’t load because data throttling is in effect.
- [static var placemarkNotFound: MKError.Code](mkerror/placemarknotfound.md)
  The framework couldn’t find the specified placemark.
- [static var serverFailure: MKError.Code](mkerror/serverfailure.md)
  The map server was unable to return the desired information.
- [static var unknown: MKError.Code](mkerror/unknown.md)
  An unknown error occurred.
- [MKError.Code](mkerror/code.md)
  Error constants for the MapKit framework.
### Type Properties
- [static var errorDomain: String](mkerror/errordomain.md)
  The error domain.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let MKErrorDomain: String](mkerrordomain.md)
  The error domain for MapKit.
- [MKError.Code](mkerror/code.md)
  Error constants for the MapKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkerror)*