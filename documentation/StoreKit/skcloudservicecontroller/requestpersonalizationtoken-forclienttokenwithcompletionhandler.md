# requestPersonalizationToken(forClientToken:withCompletionHandler:)

**Framework**: StoreKit  
**Kind**: method

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- tvOS 10.3+

## Declaration

```swift
func requestPersonalizationToken(forClientToken clientToken: String, withCompletionHandler completionHandler: @escaping (String?, (any Error)?) -> Void)
```

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
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requeststorefrontidentifier(completionhandler:).md)
  Gets the device’s storefront identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestpersonalizationtoken(forclienttoken:withcompletionhandler:))*