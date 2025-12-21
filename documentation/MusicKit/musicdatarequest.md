# MusicDataRequest

**Framework**: MusicKit  
**Kind**: struct

A request for loading data from an arbitrary Apple Music API endpoint.

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
struct MusicDataRequest
```

## Topics

### Structures
- [MusicDataRequest.Error](musicdatarequest/error.md)
  An error that the Apple Music API returns.
### Initializers
- [init(urlRequest: URLRequest)](musicdatarequest/init(urlrequest:).md)
  Creates a data request with a URL request.
### Instance Properties
- [let urlRequest: URLRequest](musicdatarequest/urlrequest.md)
  The URL request for the data request.
### Instance Methods
- [func response() async throws -> MusicDataResponse](musicdatarequest/response.md)
  Fetches data from the Apple Music API endpoint that the URL request defines.
### Type Properties
- [static var currentCountryCode: String](musicdatarequest/currentcountrycode.md)
  Fetches the current country code for the user’s Apple Music account.
- [static var tokenProvider: any MusicUserTokenProvider & MusicDeveloperTokenProvider](musicdatarequest/tokenprovider.md)
  The shared token provider for fetching tokens that Apple Music API requires.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MusicDataResponse](musicdataresponse.md)
  An object containing results for a data request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicdatarequest)*