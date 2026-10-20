# unsupportedPlatform

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

An error code that indicates the current platform doesn’t support overlays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var unsupportedPlatform: SKError.Code { get }
```

## See Also

### Error codes
- [SKError.Code](./code.md)
  Error codes for StoreKit errors.
- [static var unknown: SKError.Code](./unknown.md)
  Error code indicating that an unknown or unexpected error occurred.
- [static var clientInvalid: SKError.Code](./clientinvalid.md)
  Error code indicating that the client is not allowed to perform the attempted action.
- [static var paymentCancelled: SKError.Code](./paymentcancelled.md)
  Error code indicating that the user canceled a payment request.
- [static var paymentInvalid: SKError.Code](./paymentinvalid.md)
  Error code indicating that one of the payment parameters was not recognized by the App Store.
- [static var paymentNotAllowed: SKError.Code](./paymentnotallowed.md)
  Error code indicating that the user is not allowed to authorize payments.
- [static var storeProductNotAvailable: SKError.Code](./storeproductnotavailable.md)
  Error code indicating that the requested product is not available in the store.
- [static var cloudServicePermissionDenied: SKError.Code](./cloudservicepermissiondenied.md)
  Error code indicating that the user has not allowed access to Cloud service information.
- [static var cloudServiceNetworkConnectionFailed: SKError.Code](./cloudservicenetworkconnectionfailed.md)
  Error code indicating that the device could not connect to the network.
- [static var cloudServiceRevoked: SKError.Code](./cloudservicerevoked.md)
  Error code indicating that the user has revoked permission to use this cloud service.
- [static var privacyAcknowledgementRequired: SKError.Code](./privacyacknowledgementrequired.md)
  Error code indicating that the user has not yet acknowledged Apple’s privacy policy for Apple Music.
- [static var unauthorizedRequestData: SKError.Code](./unauthorizedrequestdata.md)
  Error code indicating that the app is attempting to use a property for which it does not have the required entitlement.
- [static var invalidOfferIdentifier: SKError.Code](./invalidofferidentifier.md)
  Error code indicating that the offer identifier cannot be found or is not active.
- [static var invalidOfferPrice: SKError.Code](./invalidofferprice.md)
  Error code indicating that the price you specified in App Store Connect is no longer valid.
- [static var invalidSignature: SKError.Code](./invalidsignature.md)
  Error code indicating that the signature in a payment discount is not valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skerror/unsupportedplatform)*