# requestStorefrontIdentifier(completionHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Gets the device’s storefront identifier.

**Availability**:
- iOS 9.3+ - Deprecated in 18.0
- iPadOS 9.3+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 9.3+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use Storefront.current.id.

## Declaration

```swift
func requestStorefrontIdentifier(completionHandler: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
func requestStorefrontIdentifier() async throws -> String
```

```objc
- (void) requestStorefrontIdentifierWithCompletionHandler:(void (^)(NSString *storefrontIdentifier, NSError *error)) completionHandler;
```

## Discussion

You need to get the appropriate storefront before you specify a product, because product identifiers are meaningful within the context of a store.

## Parameters

- `completionHandler`: A block that is called when the storefront ID is returned. The block takes the following parameters:

  - **storefrontIdentifier**: The identifier of a specific storefront.
  - **error**: An error value that indicates the reason for failure. Possible values are [`SKError.Code.unknown`](../skerror/code/unknown.md), [`SKError.Code.cloudServicePermissionDenied`](../skerror/code/cloudservicepermissiondenied.md), and [`SKError.Code.cloudServiceNetworkConnectionFailed`](../skerror/code/cloudservicenetworkconnectionfailed.md).

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
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](./requestpersonalizationtoken%28forclienttoken,withcompletionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requeststorefrontidentifier(completionhandler:))*