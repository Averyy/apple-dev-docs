# SKCloudServiceAuthorizationStatus.authorized

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The user authorizes playback of Apple Music tracks and the addition of tracks to their music library.

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
case authorized
```

```c
SKCloudServiceAuthorizationStatusAuthorized
```

## Mentions

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
- [Offering Apple Music Subscription in Your App](../offering-apple-music-subscription-in-your-app.md)

## See Also

### Constants
- [SKCloudServiceAuthorizationStatus.notDetermined](./notdetermined.md)
  The authorization type cannot be determined.
- [SKCloudServiceAuthorizationStatus.denied](./denied.md)
  The user does not authorize any access to their music library.
- [SKCloudServiceAuthorizationStatus.restricted](./restricted.md)
  Access to the music library is restricted in a way that the user cannot change, so your app should not prompt for authorization. An example of this situation is if the device is in an education mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/authorized)*