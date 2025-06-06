# MusicUserTokenProvider

**Framework**: MusicKit  
**Kind**: class

A class that music requests use to fetch user tokens your app requires to access Apple Music API.

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
class MusicUserTokenProvider
```

## Topics

### Initializers
- [init()](musicusertokenprovider/init.md)
  Creates a user token provider.
### Instance Methods
- [func userToken(for: String, options: MusicTokenRequestOptions) async throws -> String](musicusertokenprovider/usertoken(for:options:).md)
  Fetches and returns a user token for Apple Music API.

## Relationships

### Inherited By
- [DefaultMusicTokenProvider](defaultmusictokenprovider.md)

## See Also

- [typealias MusicTokenProvider](musictokenprovider.md)
  An object that music requests use to access Apple Music API.
- [protocol MusicDeveloperTokenProvider](musicdevelopertokenprovider.md)
  A set of methods that music requests use to access Apple Music API.
- [struct MusicTokenRequestOptions](musictokenrequestoptions.md)
  Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.
- [enum MusicTokenRequestError](musictokenrequesterror.md)
  An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.
- [class DefaultMusicTokenProvider](defaultmusictokenprovider.md)
  The default token provider that music requests use to access Apple Music API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicusertokenprovider)*