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

### Operators
- [static func == (MusicDataResponse, MusicDataResponse) -> Bool](musicdataresponse/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let data: Data](musicdataresponse/data.md)
  The raw data returned by the Apple Music API endpoint for the originating data request.
- [var hashValue: Int](musicdataresponse/hashvalue.md)
  The hash value.
- [let urlResponse: HTTPURLResponse](musicdataresponse/urlresponse.md)
  The URL response returned by the Apple Music API endpoint for the originating data request.
### Instance Methods
- [func hash(into: inout Hasher)](musicdataresponse/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musicdataresponse/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musicdataresponse/customstringconvertible-implementations.md)
- [Equatable Implementations](musicdataresponse/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MusicDataRequest](musicdatarequest.md)
  A request for loading data from an arbitrary Apple Music API endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicdataresponse)*