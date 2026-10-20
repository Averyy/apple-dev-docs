# SKCloudServiceAuthorizationStatus.notDetermined

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The authorization type cannot be determined.

**Availability**:
- iOS 9.3+ - Deprecated in 18.0
- iPadOS 9.3+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 9.3+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use MusicAuthorization.Status from MusicKit.

## Declaration

```swift
case notDetermined
```

```c
SKCloudServiceAuthorizationStatusNotDetermined
```

## Mentions

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
- [Requesting Access to Apple Music Library](../requesting-access-to-apple-music-library.md)

## See Also

### Constants
- [SKCloudServiceAuthorizationStatus.denied](./denied.md)
  The user does not authorize any access to their music library.
- [SKCloudServiceAuthorizationStatus.restricted](./restricted.md)
  Access to the music library is restricted in a way that the user cannot change, so your app should not prompt for authorization. An example of this situation is if the device is in an education mode.
- [SKCloudServiceAuthorizationStatus.authorized](./authorized.md)
  The user authorizes playback of Apple Music tracks and the addition of tracks to their music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/notdetermined)*