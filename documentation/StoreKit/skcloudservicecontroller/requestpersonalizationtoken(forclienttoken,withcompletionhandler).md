# requestPersonalizationToken(forClientToken:withCompletionHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 10.3+ - Deprecated in 11.0
- iPadOS 10.3+ - Deprecated in 11.0
- Mac Catalyst 10.3+ - Deprecated in 11.0
- tvOS 10.3+ - Deprecated in 11.0

## Declaration

```swift
func requestPersonalizationToken(forClientToken clientToken: String, withCompletionHandler completionHandler: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```objc
- (void) requestPersonalizationTokenForClientToken:(NSString *) clientToken withCompletionHandler:(void (^)(NSString *personalizationToken, NSError *error)) completionHandler;
```

## See Also

### Determining capabilities
- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestUserToken(forDeveloperToken: String, completionHandler: (String?, (any Error)?) -> Void)](./requestusertoken%28fordevelopertoken,completionhandler%29.md)
  Returns a user token that you use to access personalized Apple Music content.
- [func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?) -> Void)](./requeststorefrontcountrycode%28completionhandler%29.md)
  Gets the country code for the storefront associated with a customer’s iTunes account.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](./requestcapabilities%28completionhandler%29.md)
  Gets the current capabilities associated with the Music library on the device.
- [struct SKCloudServiceCapability](../skcloudservicecapability.md)
  Constants that specify the current capabilities of the customer’s Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](./requeststorefrontidentifier%28completionhandler%29.md)
  Gets the device’s storefront identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestpersonalizationtoken(forclienttoken:withcompletionhandler:))*