# MKError.Code

**Framework**: MapKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MKErrorCode : NSUInteger;
```

## Topics

### Constants
- [MKError.Code.decodingFailed](./code/decodingfailed.md)
  GeoJSON decoding failed.
- [MKError.Code.directionsNotFound](./code/directionsnotfound.md)
  The framework couldn’t find the specified directions.
- [MKError.Code.loadingThrottled](./code/loadingthrottled.md)
  The data didn’t load because data throttling is in effect.
- [MKError.Code.placemarkNotFound](./code/placemarknotfound.md)
  The specified placemark could not be found.
- [MKError.Code.serverFailure](./code/serverfailure.md)
  The map server was unable to return the desired information.
- [MKError.Code.unknown](./code/unknown.md)
  An unknown error occurred.
### Initializers
- [init?(rawValue: UInt)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [let MKErrorDomain: String](../mkerrordomain.md)
  The error domain for MapKit.
- [struct MKError](../mkerror.md)
  Error constants for the MapKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkerror/code)*