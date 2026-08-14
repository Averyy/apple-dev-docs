# MusicTokenRequestError

**Framework**: MusicKit  
**Kind**: enum

An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.

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
enum MusicTokenRequestError
```

## Topics

### Enumeration Cases
- [MusicTokenRequestError.developerTokenRequestFailed](musictokenrequesterror/developertokenrequestfailed.md)
  An error that indicates a failure in the process of fetching a developer token for the current app.
- [MusicTokenRequestError.permissionDenied](musictokenrequesterror/permissiondenied.md)
  An error that occurs when the user doesn’t consent for the current app to access their Apple Music data.
- [MusicTokenRequestError.privacyAcknowledgementRequired](musictokenrequesterror/privacyacknowledgementrequired.md)
  An error that occurs when the user needs to acknowledge the most recent privacy policy.
- [MusicTokenRequestError.unknown](musictokenrequesterror/unknown.md)
  An error indicating the ocurrence of an unknown or unexpected error.
- [MusicTokenRequestError.userNotSignedIn](musictokenrequesterror/usernotsignedin.md)
  An error that occurs when the user isn’t signed in with an Apple Music account.
- [MusicTokenRequestError.userTokenRequestFailed](musictokenrequesterror/usertokenrequestfailed.md)
  An error that indicates a failure in the process of fetching a user token.
- [MusicTokenRequestError.userTokenRevoked](musictokenrequesterror/usertokenrevoked.md)
  An error that occurs when the user revokes permission for the current app to access their Apple Music data.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [LocalizedError](../foundation/localizederror.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [typealias MusicTokenProvider](musictokenprovider.md)
  An object that music requests use to access Apple Music API.
- [protocol MusicDeveloperTokenProvider](musicdevelopertokenprovider.md)
  A set of methods that music requests use to access Apple Music API.
- [class MusicUserTokenProvider](musicusertokenprovider.md)
  A class that music requests use to fetch user tokens your app requires to access Apple Music API.
- [struct MusicTokenRequestOptions](musictokenrequestoptions.md)
  Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.
- [class DefaultMusicTokenProvider](defaultmusictokenprovider.md)
  The default token provider that music requests use to access Apple Music API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musictokenrequesterror)*