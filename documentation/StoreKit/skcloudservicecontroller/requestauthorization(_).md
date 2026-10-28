# requestAuthorization(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Asks the customer for permission to access the Music library on the device.

**Availability**:
- iOS 9.3+ - Deprecated in 18.0
- iPadOS 9.3+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 9.3+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use MusicAuthorization.request() from MusicKit.

## Declaration

```swift
class func requestAuthorization(_ completionHandler: @escaping @Sendable (SKCloudServiceAuthorizationStatus) -> Void)
```

```swift
class func requestAuthorization() async -> SKCloudServiceAuthorizationStatus
```

```objc
+ (void) requestAuthorization:(void (^)(SKCloudServiceAuthorizationStatus authorizationStatus)) completionHandler;
```

## Mentions

- [Requesting Access to Apple Music Library](../requesting-access-to-apple-music-library.md)
- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)

## Discussion

You can use this method to ask the user for permission to play Apple Music tracks or to add tracks to the music library.

## Parameters

- `completionHandler`: A block that is called when authorization is granted or denied by the user.

## See Also

### Getting authorization to access the Music library
- [Requesting Access to Apple Music Library](../requesting-access-to-apple-music-library.md)
  Prompt the customer to authorize access to Apple Music library.
- [class func authorizationStatus() -> SKCloudServiceAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns the type of authorization the customer has for accessing the Music library on the device.
- [enum SKCloudServiceAuthorizationStatus](../skcloudserviceauthorizationstatus.md)
  Constants that indicate the type of authorization the customer has for accessing the Music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestauthorization(_:))*