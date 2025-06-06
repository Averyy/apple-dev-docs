# SKCloudServiceAuthorizationStatus

**Framework**: StoreKit  
**Kind**: enum

Constants that indicate the type of authorization the customer has for accessing the Music library.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 9.3+
- watchOS 7.0+

## Declaration

```swift
enum SKCloudServiceAuthorizationStatus
```

## Topics

### Constants
- [SKCloudServiceAuthorizationStatus.notDetermined](skcloudserviceauthorizationstatus/notdetermined.md)
  The authorization type cannot be determined.
- [SKCloudServiceAuthorizationStatus.denied](skcloudserviceauthorizationstatus/denied.md)
  The user does not authorize any access to their music library.
- [SKCloudServiceAuthorizationStatus.restricted](skcloudserviceauthorizationstatus/restricted.md)
  Access to the music library is restricted in a way that the user cannot change, so your app should not prompt for authorization. An example of this situation is if the device is in an education mode.
- [SKCloudServiceAuthorizationStatus.authorized](skcloudserviceauthorizationstatus/authorized.md)
  The user authorizes playback of Apple Music tracks and the addition of tracks to their music library.
### Initializers
- [init?(rawValue: Int)](skcloudserviceauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md)
  Prompt the customer to authorize access to Apple Music library.
- [class func authorizationStatus() -> SKCloudServiceAuthorizationStatus](skcloudservicecontroller/authorizationstatus.md)
  Returns the type of authorization the customer has for accessing the Music library on the device.
- [class func requestAuthorization((SKCloudServiceAuthorizationStatus) -> Void)](skcloudservicecontroller/requestauthorization(_:).md)
  Asks the customer for permission to access the Music library on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus)*