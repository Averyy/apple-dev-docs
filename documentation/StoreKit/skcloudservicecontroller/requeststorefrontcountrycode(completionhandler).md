# requestStorefrontCountryCode(completionHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Gets the country code for the storefront associated with a customer’s iTunes account.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 11.0+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use MusicDataRequest.currentCountryCode from MusicKit.

## Declaration

```swift
func requestStorefrontCountryCode(completionHandler: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
func requestStorefrontCountryCode() async throws -> String
```

```objc
- (void) requestStorefrontCountryCodeWithCompletionHandler:(void (^)(NSString *storefrontCountryCode, NSError *error)) completionHandler;
```

## Discussion

You need to get the appropriate storefront country code before you specify a product as each country or region contains different products.

## Parameters

- `completionHandler`: A block that is called when the storefront country code is returned. The block takes the following parameters:

  - **storefrontCountryCode**: The country code of a specific storefront.
  - **error**: An error value that indicates the reason for failure. See [`SKError.Code`](../skerror/code.md) for possible error values.

## See Also

### Determining capabilities
- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestUserToken(forDeveloperToken: String, completionHandler: (String?, (any Error)?) -> Void)](./requestusertoken%28fordevelopertoken,completionhandler%29.md)
  Returns a user token that you use to access personalized Apple Music content.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](./requestcapabilities%28completionhandler%29.md)
  Gets the current capabilities associated with the Music library on the device.
- [struct SKCloudServiceCapability](../skcloudservicecapability.md)
  Constants that specify the current capabilities of the customer’s Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](./requeststorefrontidentifier%28completionhandler%29.md)
  Gets the device’s storefront identifier.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](./requestpersonalizationtoken%28forclienttoken,withcompletionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requeststorefrontcountrycode(completionhandler:))*