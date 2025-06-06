# SKError.Code

**Framework**: StoreKit  
**Kind**: enum

Error codes for StoreKit errors.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
enum Code
```

## Mentions

- [Handling errors](handling-errors.md)

## Topics

### Enumeration Cases
- [SKError.Code.unknown](skerror/code/unknown.md)
  Error code indicating that an unknown or unexpected error occurred.
- [SKError.Code.clientInvalid](skerror/code/clientinvalid.md)
  Error code indicating that the client is not allowed to perform the attempted action.
- [SKError.Code.paymentCancelled](skerror/code/paymentcancelled.md)
  Error code indicating that the user canceled a payment request.
- [SKError.Code.paymentInvalid](skerror/code/paymentinvalid.md)
  Error code indicating that one of the payment parameters wasn’t recognized by the App Store.
- [SKError.Code.paymentNotAllowed](skerror/code/paymentnotallowed.md)
  Error code indicating that the user is not allowed to authorize payments.
- [SKError.Code.storeProductNotAvailable](skerror/code/storeproductnotavailable.md)
  Error code indicating that the requested product is not available in the store.
- [SKError.Code.cloudServicePermissionDenied](skerror/code/cloudservicepermissiondenied.md)
  Error code indicating that the user has not allowed access to Cloud service information.
- [SKError.Code.cloudServiceNetworkConnectionFailed](skerror/code/cloudservicenetworkconnectionfailed.md)
  Error code indicating that the device could not connect to the network.
- [SKError.Code.cloudServiceRevoked](skerror/code/cloudservicerevoked.md)
  Error code indicating that the user has revoked permission to use this cloud service.
- [SKError.Code.privacyAcknowledgementRequired](skerror/code/privacyacknowledgementrequired.md)
  Error code indicating that the user has not yet acknowledged Apple’s privacy policy for Apple Music.
- [SKError.Code.unauthorizedRequestData](skerror/code/unauthorizedrequestdata.md)
  Error code indicating that the app is attempting to use a property for which it does not have the required entitlement.
- [SKError.Code.invalidOfferIdentifier](skerror/code/invalidofferidentifier.md)
  Error code indicating that the offer identifier is invalid.
- [SKError.Code.invalidOfferPrice](skerror/code/invalidofferprice.md)
  Error code indicating that the price you specified in App Store Connect is no longer valid.
- [SKError.Code.invalidSignature](skerror/code/invalidsignature.md)
  Error code indicating that the signature in a payment discount isn’t valid.
- [SKError.Code.missingOfferParams](skerror/code/missingofferparams.md)
  Error code indicating that parameters are missing in a payment discount.
- [SKError.Code.ineligibleForOffer](skerror/code/ineligibleforoffer.md)
  An error code that indicates the user is ineligible for the subscription offer.
- [SKError.Code.overlayCancelled](skerror/code/overlaycancelled.md)
  An error code that indicates the cancellation of an overlay.
- [SKError.Code.overlayInvalidConfiguration](skerror/code/overlayinvalidconfiguration.md)
  An error code that indicates the overlay’s configuration is invalid.
- [SKError.Code.overlayPresentedInBackgroundScene](skerror/code/overlaypresentedinbackgroundscene.md)
- [SKError.Code.overlayTimeout](skerror/code/overlaytimeout.md)
- [SKError.Code.unsupportedPlatform](skerror/code/unsupportedplatform.md)
  An error code that indicates the current platform doesn’t support overlays.
### Initializers
- [init?(rawValue: Int)](skerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Handling errors](handling-errors.md)
  Determine the underlying cause of errors that result from StoreKit requests.
- [struct SKError](skerror.md)
  StoreKit error descriptions, codes, and domains.
- [let SKErrorDomain: String](skerrordomain.md)
  The error domain name for StoreKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skerror/code)*