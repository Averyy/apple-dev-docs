# SKError.Code.storeProductNotAvailable

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

Error code indicating that the requested product is not available in the store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
case storeProductNotAvailable
```

```c
SKErrorStoreProductNotAvailable
```

## Discussion

See [`SKStorefront`](../../skstorefront.md) for more information.

## See Also

### Enumeration Cases
- [SKError.Code.unknown](./unknown.md)
  Error code indicating that an unknown or unexpected error occurred.
- [SKError.Code.clientInvalid](./clientinvalid.md)
  Error code indicating that the client is not allowed to perform the attempted action.
- [SKError.Code.paymentCancelled](./paymentcancelled.md)
  Error code indicating that the user canceled a payment request.
- [SKError.Code.paymentInvalid](./paymentinvalid.md)
  Error code indicating that one of the payment parameters wasn’t recognized by the App Store.
- [SKError.Code.paymentNotAllowed](./paymentnotallowed.md)
  Error code indicating that the user is not allowed to authorize payments.
- [SKError.Code.cloudServicePermissionDenied](./cloudservicepermissiondenied.md)
  Error code indicating that the user has not allowed access to Cloud service information.
- [SKError.Code.cloudServiceNetworkConnectionFailed](./cloudservicenetworkconnectionfailed.md)
  Error code indicating that the device could not connect to the network.
- [SKError.Code.cloudServiceRevoked](./cloudservicerevoked.md)
  Error code indicating that the user has revoked permission to use this cloud service.
- [SKError.Code.privacyAcknowledgementRequired](./privacyacknowledgementrequired.md)
  Error code indicating that the user has not yet acknowledged Apple’s privacy policy for Apple Music.
- [SKError.Code.unauthorizedRequestData](./unauthorizedrequestdata.md)
  Error code indicating that the app is attempting to use a property for which it does not have the required entitlement.
- [SKError.Code.invalidOfferIdentifier](./invalidofferidentifier.md)
  Error code indicating that the offer identifier is invalid.
- [SKError.Code.invalidOfferPrice](./invalidofferprice.md)
  Error code indicating that the price you specified in App Store Connect is no longer valid.
- [SKError.Code.invalidSignature](./invalidsignature.md)
  Error code indicating that the signature in a payment discount isn’t valid.
- [SKError.Code.missingOfferParams](./missingofferparams.md)
  Error code indicating that parameters are missing in a payment discount.
- [SKError.Code.ineligibleForOffer](./ineligibleforoffer.md)
  An error code that indicates the user is ineligible for the subscription offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skerror/code/storeproductnotavailable)*