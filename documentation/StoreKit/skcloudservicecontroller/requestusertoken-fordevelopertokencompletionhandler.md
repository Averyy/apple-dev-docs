# requestUserToken(forDeveloperToken:completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Returns a user token that you use to access personalized Apple Music content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 11.0+
- watchOS 7.0+

## Declaration

```swift
func requestUserToken(forDeveloperToken developerToken: String) async throws -> String
```

#### Discussion

Use this method with your developer token to get a token that authenticates the user in personalized Apple Music API requests. Note that personalized requests return user-specific data. Errors 401 and 403 only occur when requesting a music user token. They do not occur for any of the other Apple Music API requests.

## Parameters

- `developerToken`: A signed and encrypted JWT token used to authenticate the developer in Apple Music API requests.
- `completionHandler`: A completion block that includes the following parameters:

## See Also

- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requeststorefrontcountrycode(completionhandler:).md)
  Gets the country code for the storefront associated with a customer’s iTunes account.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](skcloudservicecontroller/requestcapabilities(completionhandler:).md)
  Gets the current capabilities associated with the Music library on the device.
- [struct SKCloudServiceCapability](skcloudservicecapability.md)
  Constants that specify the current capabilities of the customer’s Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requeststorefrontidentifier(completionhandler:).md)
  Gets the device’s storefront identifier.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requestpersonalizationtoken(forclienttoken:withcompletionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestusertoken(fordevelopertoken:completionhandler:))*