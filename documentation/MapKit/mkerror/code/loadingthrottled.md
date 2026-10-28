# MKError.Code.loadingThrottled

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

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
case loadingThrottled
```

```c
MKErrorLoadingThrottled
```

## Discussion

This error can occur if an app makes frequent requests for data over a short period of time.

## See Also

### Constants
- [MKError.Code.decodingFailed](./decodingfailed.md)
  GeoJSON decoding failed.
- [MKError.Code.directionsNotFound](./directionsnotfound.md)
  The framework couldn’t find the specified directions.
- [MKError.Code.placemarkNotFound](./placemarknotfound.md)
  The specified placemark could not be found.
- [MKError.Code.serverFailure](./serverfailure.md)
  The map server was unable to return the desired information.
- [MKError.Code.unknown](./unknown.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkerror/code/loadingthrottled)*