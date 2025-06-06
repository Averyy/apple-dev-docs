# requestStorefrontCountryCode(completionHandler:)

**Framework**: StoreKit  
**Kind**: method

Gets the country code for the storefront associated with a customer’s iTunes account.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- watchOS 7.0+

## Declaration

```swift
func requestStorefrontCountryCode() async throws -> String
```

#### Discussion

You need to get the appropriate storefront country code before you specify a product as each country or region contains different products.

## Parameters

- `completionHandler`: A block that is called when the storefront country code is returned. The block takes the following parameters:

## See Also

- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestUserToken(forDeveloperToken: String, completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requestusertoken(fordevelopertoken:completionhandler:).md)
  Returns a user token that you use to access personalized Apple Music content.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](skcloudservicecontroller/requestcapabilities(completionhandler:).md)
  Gets the current capabilities associated with the Music library on the device.
- [struct SKCloudServiceCapability](skcloudservicecapability.md)
  Constants that specify the current capabilities of the customer’s Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requeststorefrontidentifier(completionhandler:).md)
  Gets the device’s storefront identifier.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requestpersonalizationtoken(forclienttoken:withcompletionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requeststorefrontcountrycode(completionhandler:))*