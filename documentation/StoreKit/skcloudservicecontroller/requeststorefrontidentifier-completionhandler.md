# requestStorefrontIdentifier(completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Gets the device’s storefront identifier.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 9.3+
- watchOS 7.0+

## Declaration

```swift
func requestStorefrontIdentifier() async throws -> String
```

#### Discussion

You need to get the appropriate storefront before you specify a product, because product identifiers are meaningful within the context of a store.

## Parameters

- `completionHandler`: A block that is called when the storefront ID is returned. The block takes the following parameters:

## See Also

- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestUserToken(forDeveloperToken: String, completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requestusertoken(fordevelopertoken:completionhandler:).md)
  Returns a user token that you use to access personalized Apple Music content.
- [func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requeststorefrontcountrycode(completionhandler:).md)
  Gets the country code for the storefront associated with a customer’s iTunes account.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](skcloudservicecontroller/requestcapabilities(completionhandler:).md)
  Gets the current capabilities associated with the Music library on the device.
- [struct SKCloudServiceCapability](skcloudservicecapability.md)
  Constants that specify the current capabilities of the customer’s Music library on the device.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requestpersonalizationtoken(forclienttoken:withcompletionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requeststorefrontidentifier(completionhandler:))*