# MusicTokenProvider

**Framework**: MusicKit  
**Kind**: typealias

An object that music requests use to access Apple Music API.

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
typealias MusicTokenProvider = MusicUserTokenProvider & MusicDeveloperTokenProvider
```

#### Discussion

A token provider for MusicKit needs to be a subclass of [`MusicUserTokenProvider`](musicusertokenprovider.md) which conforms to the [`MusicDeveloperTokenProvider`](musicdevelopertokenprovider.md) protocol.

## See Also

- [protocol MusicDeveloperTokenProvider](musicdevelopertokenprovider.md)
  A set of methods that music requests use to access Apple Music API.
- [class MusicUserTokenProvider](musicusertokenprovider.md)
  A class that music requests use to fetch user tokens your app requires to access Apple Music API.
- [struct MusicTokenRequestOptions](musictokenrequestoptions.md)
  Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.
- [enum MusicTokenRequestError](musictokenrequesterror.md)
  An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.
- [class DefaultMusicTokenProvider](defaultmusictokenprovider.md)
  The default token provider that music requests use to access Apple Music API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musictokenprovider)*