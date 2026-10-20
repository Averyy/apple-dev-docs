# requestUserToken(forDeveloperToken:completionHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Returns a user token that you use to access personalized Apple Music content.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 11.0+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use MusicKit.

## Declaration

```swift
func requestUserToken(forDeveloperToken developerToken: String, completionHandler: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
func requestUserToken(forDeveloperToken developerToken: String) async throws -> String
```

```objc
- (void) requestUserTokenForDeveloperToken:(NSString *) developerToken completionHandler:(void (^)(NSString *userToken, NSError *error)) completionHandler;
```

#### Discussion

Use this method with your developer token to get a token that authenticates the user in personalized Apple Music API requests. Note that personalized requests return user-specific data. Errors 401 and 403 only occur when requesting a music user token. They do not occur for any of the other Apple Music API requests.

## Parameters

- `developerToken`: A signed and encrypted JWT token used to authenticate the developer in Apple Music API requests.
- `completionHandler`: A completion block that includes the following parameters:

  - **userToken**: A token that identifies the user.
  - **error**: The error that occurred, if any.

## See Also

### Determining capabilities
- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?) -> Void)](./requeststorefrontcountrycode%28completionhandler%29.md)
  Gets the country code for the storefront associated with a customer’s iTunes account.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](./requestcapabilities%28completionhandler%29.md)
  Gets the current capabilities associated with the Music library on the device.
- [struct SKCloudServiceCapability](../skcloudservicecapability.md)
  Constants that specify the current capabilities of the customer’s Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](./requeststorefrontidentifier%28completionhandler%29.md)
  Gets the device’s storefront identifier.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](./requestpersonalizationtoken%28forclienttoken,withcompletionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestusertoken(fordevelopertoken:completionhandler:))*