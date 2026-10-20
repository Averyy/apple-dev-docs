# SKCloudServiceAuthorizationStatus

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the type of authorization the customer has for accessing the Music library.

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
enum SKCloudServiceAuthorizationStatus
```

```c
enum SKCloudServiceAuthorizationStatus : NSInteger;
```

## Topics

### Constants
- [SKCloudServiceAuthorizationStatus.notDetermined](./skcloudserviceauthorizationstatus/notdetermined.md)
  The authorization type cannot be determined.
- [SKCloudServiceAuthorizationStatus.denied](./skcloudserviceauthorizationstatus/denied.md)
  The user does not authorize any access to their music library.
- [SKCloudServiceAuthorizationStatus.restricted](./skcloudserviceauthorizationstatus/restricted.md)
  Access to the music library is restricted in a way that the user cannot change, so your app should not prompt for authorization. An example of this situation is if the device is in an education mode.
- [SKCloudServiceAuthorizationStatus.authorized](./skcloudserviceauthorizationstatus/authorized.md)
  The user authorizes playback of Apple Music tracks and the addition of tracks to their music library.
### Initializers
- [init?(rawValue: Int)](./skcloudserviceauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting authorization to access the Music library
- [Requesting Access to Apple Music Library](./requesting-access-to-apple-music-library.md)
  Prompt the customer to authorize access to Apple Music library.
- [class func authorizationStatus() -> SKCloudServiceAuthorizationStatus](./skcloudservicecontroller/authorizationstatus%28%29.md)
  Returns the type of authorization the customer has for accessing the Music library on the device.
- [class func requestAuthorization((SKCloudServiceAuthorizationStatus) -> Void)](./skcloudservicecontroller/requestauthorization%28_%29.md)
  Asks the customer for permission to access the Music library on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus)*