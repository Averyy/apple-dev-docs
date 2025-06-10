# SKError.Code.unknown

**Framework**: StoreKit  
**Kind**: case

Error code indicating that an unknown or unexpected error occurred.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
case unknown
```

#### Discussion

For more information about the underlying cause of the error, see the [`localizedDescription`](https://developer.apple.com/documentation/Foundation/NSError/localizedDescription) property of the error object.

Retrying may resolve this error in some instances.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skerror/code/unknown)*