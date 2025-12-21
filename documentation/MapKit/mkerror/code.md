# MKError.Code

**Framework**: MapKit  
**Kind**: enum

Error constants for the MapKit framework.

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
enum Code
```

## Topics

### Constants
- [MKError.Code.decodingFailed](mkerror/code/decodingfailed.md)
  GeoJSON decoding failed.
- [MKError.Code.directionsNotFound](mkerror/code/directionsnotfound.md)
  The framework couldn’t find the specified directions.
- [MKError.Code.loadingThrottled](mkerror/code/loadingthrottled.md)
  The data didn’t load because data throttling is in effect.
- [MKError.Code.placemarkNotFound](mkerror/code/placemarknotfound.md)
  The specified placemark could not be found.
- [MKError.Code.serverFailure](mkerror/code/serverfailure.md)
  The map server was unable to return the desired information.
- [MKError.Code.unknown](mkerror/code/unknown.md)
  An unknown error occurred.
### Initializers
- [init?(rawValue: UInt)](mkerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let MKErrorDomain: String](mkerrordomain.md)
  The error domain for MapKit.
- [struct MKError](mkerror.md)
  Error constants for the MapKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkerror/code)*