# requestCapabilities(completionHandler:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Gets the current capabilities associated with the Music library on the device.

**Availability**:
- iOS 9.3+ - Deprecated in 18.0
- iPadOS 9.3+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 9.3+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use MusicSubscription.current from MusicKit.

## Declaration

```swift
func requestCapabilities(completionHandler: @escaping @Sendable (SKCloudServiceCapability, (any Error)?) -> Void)
```

```swift
func requestCapabilities() async throws -> SKCloudServiceCapability
```

```objc
- (void) requestCapabilitiesWithCompletionHandler:(void (^)(SKCloudServiceCapability capabilities, NSError *error)) completionHandler;
```

## Mentions

- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
- [Offering Apple Music Subscription in Your App](../offering-apple-music-subscription-in-your-app.md)

## Discussion

## Parameters

- `completionHandler`: A block that is called when the device’s current capabilities are determined. The block takes the following parameters:

  - **capabilities**: Flags that indicate the device’s capabilities. For possible values, see [`SKCloudServiceCapability`](../skcloudservicecapability.md).
  - **error**: An error value that indicates the reason for failure. Possible values are [`SKError.Code.unknown`](../skerror/code/unknown.md), [`SKError.Code.cloudServicePermissionDenied`](../skerror/code/cloudservicepermissiondenied.md), and [`SKError.Code.cloudServiceNetworkConnectionFailed`](../skerror/code/cloudservicenetworkconnectionfailed.md).

## See Also

### Determining capabilities
- [Determining a person’s Apple Music capabilities](../determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestUserToken(forDeveloperToken: String, completionHandler: (String?, (any Error)?) -> Void)](./requestusertoken%28fordevelopertoken,completionhandler%29.md)
  Returns a user token that you use to access personalized Apple Music content.
- [func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?) -> Void)](./requeststorefrontcountrycode%28completionhandler%29.md)
  Gets the country code for the storefront associated with a customer’s iTunes account.
- [struct SKCloudServiceCapability](../skcloudservicecapability.md)
  Constants that specify the current capabilities of the customer’s Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](./requeststorefrontidentifier%28completionhandler%29.md)
  Gets the device’s storefront identifier.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](./requestpersonalizationtoken%28forclienttoken,withcompletionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/requestcapabilities(completionhandler:))*