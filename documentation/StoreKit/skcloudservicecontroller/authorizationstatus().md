# authorizationStatus()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Returns the type of authorization the customer has for accessing the Music library on the device.

**Availability**:
- iOS 9.3+ - Deprecated in 18.0
- iPadOS 9.3+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 9.3+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use MusicAuthorization.currentStatus from MusicKit.

## Declaration

```swift
class func authorizationStatus() -> SKCloudServiceAuthorizationStatus
```

```objc
+ (SKCloudServiceAuthorizationStatus) authorizationStatus;
```

## Mentions

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
- [Offering Apple Music Subscription in Your App](../offering-apple-music-subscription-in-your-app.md)
- [Requesting Access to Apple Music Library](../requesting-access-to-apple-music-library.md)

## Return Value

The type of authorization for music library access. See [`SKCloudServiceAuthorizationStatus`](../skcloudserviceauthorizationstatus.md) for a list of possible values.

## Discussion

Use the authorization status to determine in what ways you can access the user’s music library.

## See Also

### Related Documentation
- [Apple In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
### Getting authorization to access the Music library
- [Requesting Access to Apple Music Library](../requesting-access-to-apple-music-library.md)
  Prompt the customer to authorize access to Apple Music library.
- [class func requestAuthorization((SKCloudServiceAuthorizationStatus) -> Void)](./requestauthorization%28_%29.md)
  Asks the customer for permission to access the Music library on the device.
- [enum SKCloudServiceAuthorizationStatus](../skcloudserviceauthorizationstatus.md)
  Constants that indicate the type of authorization the customer has for accessing the Music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/authorizationstatus())*