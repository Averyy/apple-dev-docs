# SKError.Code

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum SKErrorCode : NSInteger;
```

## Mentions

- [Handling errors](../handling-errors.md)

## Topics

### Enumeration Cases
- [SKError.Code.unknown](./code/unknown.md)
  Error code indicating that an unknown or unexpected error occurred.
- [SKError.Code.clientInvalid](./code/clientinvalid.md)
  Error code indicating that the client is not allowed to perform the attempted action.
- [SKError.Code.paymentCancelled](./code/paymentcancelled.md)
  Error code indicating that the user canceled a payment request.
- [SKError.Code.paymentInvalid](./code/paymentinvalid.md)
  Error code indicating that one of the payment parameters wasn’t recognized by the App Store.
- [SKError.Code.paymentNotAllowed](./code/paymentnotallowed.md)
  Error code indicating that the user is not allowed to authorize payments.
- [SKError.Code.storeProductNotAvailable](./code/storeproductnotavailable.md)
  Error code indicating that the requested product is not available in the store.
- [SKError.Code.cloudServicePermissionDenied](./code/cloudservicepermissiondenied.md)
  Error code indicating that the user has not allowed access to Cloud service information.
- [SKError.Code.cloudServiceNetworkConnectionFailed](./code/cloudservicenetworkconnectionfailed.md)
  Error code indicating that the device could not connect to the network.
- [SKError.Code.cloudServiceRevoked](./code/cloudservicerevoked.md)
  Error code indicating that the user has revoked permission to use this cloud service.
- [SKError.Code.privacyAcknowledgementRequired](./code/privacyacknowledgementrequired.md)
  Error code indicating that the user has not yet acknowledged Apple’s privacy policy for Apple Music.
- [SKError.Code.unauthorizedRequestData](./code/unauthorizedrequestdata.md)
  Error code indicating that the app is attempting to use a property for which it does not have the required entitlement.
- [SKError.Code.invalidOfferIdentifier](./code/invalidofferidentifier.md)
  Error code indicating that the offer identifier is invalid.
- [SKError.Code.invalidOfferPrice](./code/invalidofferprice.md)
  Error code indicating that the price you specified in App Store Connect is no longer valid.
- [SKError.Code.invalidSignature](./code/invalidsignature.md)
  Error code indicating that the signature in a payment discount isn’t valid.
- [SKError.Code.missingOfferParams](./code/missingofferparams.md)
  Error code indicating that parameters are missing in a payment discount.
- [SKError.Code.ineligibleForOffer](./code/ineligibleforoffer.md)
  An error code that indicates the user is ineligible for the subscription offer.
- [SKError.Code.overlayCancelled](./code/overlaycancelled.md)
  An error code that indicates the cancellation of an overlay.
- [SKError.Code.overlayInvalidConfiguration](./code/overlayinvalidconfiguration.md)
  An error code that indicates the overlay’s configuration is invalid.
- [SKError.Code.overlayPresentedInBackgroundScene](./code/overlaypresentedinbackgroundscene.md)
- [SKError.Code.overlayTimeout](./code/overlaytimeout.md)
- [SKError.Code.unsupportedPlatform](./code/unsupportedplatform.md)
  An error code that indicates the current platform doesn’t support overlays.
- [SKError.Code.paymentMethodBindingConfigurationRequired](./code/paymentmethodbindingconfigurationrequired.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [Handling errors](../handling-errors.md)
  Determine the underlying cause of errors that result from StoreKit requests.
- [struct SKError](../skerror.md)
  StoreKit error descriptions, codes, and domains.
- [let SKErrorDomain: String](../skerrordomain.md)
  The error domain name for StoreKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skerror/code)*