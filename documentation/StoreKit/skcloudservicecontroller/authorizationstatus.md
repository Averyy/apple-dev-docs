# authorizationStatus()

**Framework**: StoreKit  
**Kind**: method

Returns the type of authorization the customer has for accessing the Music library on the device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 9.3+
- watchOS 7.0+

## Declaration

```swift
class func authorizationStatus() -> SKCloudServiceAuthorizationStatus
```

## Mentions

- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md)
- [Offering Apple Music Subscription in Your App](offering-apple-music-subscription-in-your-app.md)
- [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md)

#### Return Value

The type of authorization for music library access. See [`SKCloudServiceAuthorizationStatus`](skcloudserviceauthorizationstatus.md) for a list of possible values.

#### Discussion

Use the authorization status to determine in what ways you can access the user’s music library.

## See Also

- [In-App Purchase Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
- [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md)
  Prompt the customer to authorize access to Apple Music library.
- [class func requestAuthorization((SKCloudServiceAuthorizationStatus) -> Void)](skcloudservicecontroller/requestauthorization(_:).md)
  Asks the customer for permission to access the Music library on the device.
- [enum SKCloudServiceAuthorizationStatus](skcloudserviceauthorizationstatus.md)
  Constants that indicate the type of authorization the customer has for accessing the Music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/authorizationstatus())*