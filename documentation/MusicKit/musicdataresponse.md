# MusicDataResponse

**Framework**: MusicKit  
**Kind**: struct

An object containing results for a data request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct MusicDataResponse
```

## Topics

### Instance Properties
- [let data: Data](musicdataresponse/data.md)
  The raw data returned by the Apple Music API endpoint for the originating data request.
- [let urlResponse: HTTPURLResponse](musicdataresponse/urlresponse.md)
  The URL response returned by the Apple Music API endpoint for the originating data request.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MusicDataRequest](musicdatarequest.md)
  A request for loading data from an arbitrary Apple Music API endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicdataresponse)*