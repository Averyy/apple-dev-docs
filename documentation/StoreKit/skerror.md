# SKError

**Framework**: StoreKit  
**Kind**: struct

StoreKit error descriptions, codes, and domains.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
struct SKError
```

## Topics

### Error codes
- [SKError.Code](skerror/code.md)
  Error codes for StoreKit errors.
- [static var unknown: SKError.Code](skerror/unknown.md)
  Error code indicating that an unknown or unexpected error occurred.
- [static var clientInvalid: SKError.Code](skerror/clientinvalid.md)
  Error code indicating that the client is not allowed to perform the attempted action.
- [static var paymentCancelled: SKError.Code](skerror/paymentcancelled.md)
  Error code indicating that the user canceled a payment request.
- [static var paymentInvalid: SKError.Code](skerror/paymentinvalid.md)
  Error code indicating that one of the payment parameters was not recognized by the App Store.
- [static var paymentNotAllowed: SKError.Code](skerror/paymentnotallowed.md)
  Error code indicating that the user is not allowed to authorize payments.
- [static var storeProductNotAvailable: SKError.Code](skerror/storeproductnotavailable.md)
  Error code indicating that the requested product is not available in the store.
- [static var cloudServicePermissionDenied: SKError.Code](skerror/cloudservicepermissiondenied.md)
  Error code indicating that the user has not allowed access to Cloud service information.
- [static var cloudServiceNetworkConnectionFailed: SKError.Code](skerror/cloudservicenetworkconnectionfailed.md)
  Error code indicating that the device could not connect to the network.
- [static var cloudServiceRevoked: SKError.Code](skerror/cloudservicerevoked.md)
  Error code indicating that the user has revoked permission to use this cloud service.
- [static var privacyAcknowledgementRequired: SKError.Code](skerror/privacyacknowledgementrequired.md)
  Error code indicating that the user has not yet acknowledged Apple’s privacy policy for Apple Music.
- [static var unauthorizedRequestData: SKError.Code](skerror/unauthorizedrequestdata.md)
  Error code indicating that the app is attempting to use a property for which it does not have the required entitlement.
- [static var invalidOfferIdentifier: SKError.Code](skerror/invalidofferidentifier.md)
  Error code indicating that the offer identifier cannot be found or is not active.
- [static var invalidOfferPrice: SKError.Code](skerror/invalidofferprice.md)
  Error code indicating that the price you specified in App Store Connect is no longer valid.
- [static var invalidSignature: SKError.Code](skerror/invalidsignature.md)
  Error code indicating that the signature in a payment discount is not valid.
- [static var missingOfferParams: SKError.Code](skerror/missingofferparams.md)
  Error code indicating that parameters are missing in a payment discount.
- [static var ineligibleForOffer: SKError.Code](skerror/ineligibleforoffer.md)
  An error code that indicates the user is ineligible for the subscription offer.
- [static var overlayCancelled: SKError.Code](skerror/overlaycancelled.md)
  An error code that indicates the cancellation of an overlay.
- [static var overlayInvalidConfiguration: SKError.Code](skerror/overlayinvalidconfiguration.md)
  An error code that indicates the overlay’s configuration is invalid.
- [static var overlayPresentedInBackgroundScene: SKError.Code](skerror/overlaypresentedinbackgroundscene.md)
- [static var overlayTimeout: SKError.Code](skerror/overlaytimeout.md)
  An error code that indicates the timing out of an overlay.
- [static var unsupportedPlatform: SKError.Code](skerror/unsupportedplatform.md)
  An error code that indicates the current platform doesn’t support overlays.
### Error domain
- [let SKErrorDomain: String](skerrordomain.md)
  The error domain name for StoreKit errors.
### Type Properties
- [static var errorDomain: String](skerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Handling errors](handling-errors.md)
  Determine the underlying cause of errors that result from StoreKit requests.
- [SKError.Code](skerror/code.md)
  Error codes for StoreKit errors.
- [let SKErrorDomain: String](skerrordomain.md)
  The error domain name for StoreKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skerror)*