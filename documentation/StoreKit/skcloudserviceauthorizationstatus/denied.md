# SKCloudServiceAuthorizationStatus.denied

**Framework**: StoreKit  
**Kind**: case

The user does not authorize any access to their music library.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 9.3+
- watchOS 7.0+

## Declaration

```swift
case denied
```

## See Also

- [SKCloudServiceAuthorizationStatus.notDetermined](skcloudserviceauthorizationstatus/notdetermined.md)
  The authorization type cannot be determined.
- [SKCloudServiceAuthorizationStatus.restricted](skcloudserviceauthorizationstatus/restricted.md)
  Access to the music library is restricted in a way that the user cannot change, so your app should not prompt for authorization. An example of this situation is if the device is in an education mode.
- [SKCloudServiceAuthorizationStatus.authorized](skcloudserviceauthorizationstatus/authorized.md)
  The user authorizes playback of Apple Music tracks and the addition of tracks to their music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/denied)*