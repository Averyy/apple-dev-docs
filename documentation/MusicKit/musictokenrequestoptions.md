# MusicTokenRequestOptions

**Framework**: MusicKit  
**Kind**: struct

Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.

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
struct MusicTokenRequestOptions
```

## Topics

### Type Properties
- [static let ignoreCache: MusicTokenRequestOptions](musictokenrequestoptions/ignorecache.md)
  An option that indicates the token provider needs to discard any cached token and generate a new token.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [typealias MusicTokenProvider](musictokenprovider.md)
  An object that music requests use to access Apple Music API.
- [protocol MusicDeveloperTokenProvider](musicdevelopertokenprovider.md)
  A set of methods that music requests use to access Apple Music API.
- [class MusicUserTokenProvider](musicusertokenprovider.md)
  A class that music requests use to fetch user tokens your app requires to access Apple Music API.
- [enum MusicTokenRequestError](musictokenrequesterror.md)
  An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.
- [class DefaultMusicTokenProvider](defaultmusictokenprovider.md)
  The default token provider that music requests use to access Apple Music API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musictokenrequestoptions)*