# requestAuthorization(_:)

**Framework**: StoreKit  
**Kind**: method

Asks the customer for permission to access the Music library on the device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 9.3+
- watchOS 7.0+

## Declaration

```swift
class func requestAuthorization() async -> SKCloudServiceAuthorizationStatus
```

## Mentions

- [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md)
- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md)

#### Discussion

You can use this method to ask the user for permission to play Apple Music tracks or to add tracks to the music library.

## Parameters

- `completionHandler`: A block that is called when authorization is granted or denied by the user.

## See Also

- [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md)
  Prompt the customer to authorize access to Apple Music library.
- [class func authorizationStatus() -> SKCloudServiceAuthorizationStatus](skcloudservicecontroller/authorizationstatus.md)
  Returns the type of authorization the customer has for accessing the Music library on the device.
- [enum SKCloudServiceAuthorizationStatus](skcloudserviceauthorizationstatus.md)
  Constants that indicate the type of authorization the customer has for accessing the Music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestauthorization(_:))*