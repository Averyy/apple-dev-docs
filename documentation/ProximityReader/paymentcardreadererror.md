# PaymentCardReaderError

**Framework**: ProximityReader  
**Kind**: enum

An error type that indicates problems with the configuration of the reader.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
enum PaymentCardReaderError
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

## Topics

### Getting the error code
- [PaymentCardReaderError.accountAlreadyLinked](paymentcardreadererror/accountalreadylinked.md)
  An error that indicates the merchant already accepted the Terms and Conditions.
- [PaymentCardReaderError.accountDeactivated](paymentcardreadererror/accountdeactivated.md)
  An error that indicates the linked Apple Account account has been deactivated by the merchant.
- [PaymentCardReaderError.accountLinkingCancelled](paymentcardreadererror/accountlinkingcancelled.md)
  An error that indicates the user cancelled the linking or relinking operation.
- [PaymentCardReaderError.accountLinkingCheckFailed](paymentcardreadererror/accountlinkingcheckfailed.md)
  An error that indicates the system couldn’t check the account status of the merchant.
- [PaymentCardReaderError.accountLinkingFailed](paymentcardreadererror/accountlinkingfailed.md)
  An error that indicates the system couldn’t link or relink the merchant using the provided Apple Account.
- [PaymentCardReaderError.accountLinkingRequiresiCloudSignIn](paymentcardreadererror/accountlinkingrequiresicloudsignin.md)
  An error that indicates the merchant must be signed into iCloud to accept the Terms and Conditions.
- [PaymentCardReaderError.accountNotLinked](paymentcardreadererror/accountnotlinked.md)
  An error that indicates the merchant must accept the Terms and Conditions with a valid Apple Account.
- [PaymentCardReaderError.backgroundRequestNotAllowed](paymentcardreadererror/backgroundrequestnotallowed.md)
  An error that results from requests to the reader while the host app is in the background state.
- [PaymentCardReaderError.deviceBanned(_:)](paymentcardreadererror/devicebanned(_:).md)
  An error that indicates the device is banned until the specified date.
- [PaymentCardReaderError.emptyReaderToken](paymentcardreadererror/emptyreadertoken.md)
  An error that indicates the reader token is empty, which is invalid.
- [PaymentCardReaderError.invalidMerchant](paymentcardreadererror/invalidmerchant.md)
  An error that indicates the merchant is invalid or unknown.
- [PaymentCardReaderError.invalidReaderToken(_:)](paymentcardreadererror/invalidreadertoken(_:).md)
  An error that indicates an invalid, non-empty reader token.
- [PaymentCardReaderError.merchantBlocked](paymentcardreadererror/merchantblocked.md)
  An error that indicates the merchant is blocked.
- [PaymentCardReaderError.modelNotSupported](paymentcardreadererror/modelnotsupported.md)
  An error that indicates the current device isn’t supported.
- [PaymentCardReaderError.networkAuthenticationError](paymentcardreadererror/networkauthenticationerror.md)
  An authentication error that occurred during connection to the server.
- [PaymentCardReaderError.networkError](paymentcardreadererror/networkerror.md)
  A network error.
- [PaymentCardReaderError.notAllowed](paymentcardreadererror/notallowed.md)
  An error usually caused by an entitlement issue, an invalid application bundle, a configuration issue, or a token issue.
- [PaymentCardReaderError.notReady](paymentcardreadererror/notready.md)
  An error that indicates the reader session isn’t ready.
- [PaymentCardReaderError.osVersionNotSupported](paymentcardreadererror/osversionnotsupported.md)
  An error that indicates the current OS version isn’t supported.
- [PaymentCardReaderError.passcodeDisabled](paymentcardreadererror/passcodedisabled.md)
  An error that indicates the device doesn’t have an active passcode.
- [PaymentCardReaderError.prepareExpired](paymentcardreadererror/prepareexpired.md)
  An error that indicates the reader’s session expired.
- [PaymentCardReaderError.prepareFailed(_:)](paymentcardreadererror/preparefailed(_:).md)
  An error that indicates preparation failed.
- [PaymentCardReaderError.readerBusy](paymentcardreadererror/readerbusy.md)
  An error that indicates the card reader is busy.
- [PaymentCardReaderError.readerMemoryFull](paymentcardreadererror/readermemoryfull.md)
  An error that indicates the reader’s internal memory is full.
- [PaymentCardReaderError.serviceConnectionError](paymentcardreadererror/serviceconnectionerror.md)
  An error that indicates an internal service is unavailable.
- [PaymentCardReaderError.tokenExpired](paymentcardreadererror/tokenexpired.md)
  An error that indicates the reader’s token expired.
- [PaymentCardReaderError.unsupported](paymentcardreadererror/unsupported.md)
  An error that indicates unsupported hardware or a problem with the device.
- [PaymentCardReaderError.unknown(code:)](paymentcardreadererror/unknown(code:).md)
  An unexpected error happened, try again.
### Getting the error details
- [var errorDescription: String](paymentcardreadererror/errordescription.md)
  A plain-text description of the error.
- [var errorName: String](paymentcardreadererror/errorname.md)
  The name of the error.
### Enumeration Cases
- [PaymentCardReaderError.requestInterrupted](paymentcardreadererror/requestinterrupted.md)
  An error that indicates the application went to background before a reader request completed.
- [PaymentCardReaderError.storeAndForwardNotAllowed](paymentcardreadererror/storeandforwardnotallowed.md)
  An error that indicates the framework can’t create a Store and Forward session because:
- [PaymentCardReaderError.storeAndForwardSessionExpired](paymentcardreadererror/storeandforwardsessionexpired.md)
  An error that indicates the framework can’t execute more reads using the current Store and Forward session, because it’s expired.
- [PaymentCardReaderError.storeAndForwardSessionInvalidated](paymentcardreadererror/storeandforwardsessioninvalidated.md)
  An error that indicates the framework invalidated the current Store and Forward session, and it can’t execute additional reads.
- [PaymentCardReaderError.storeAndForwardTokenIssuerChanged](paymentcardreadererror/storeandforwardtokenissuerchanged.md)
  An error that indicates the current Store and Forward mode has payments from a different token issuer.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MobileDocumentReaderError](mobiledocumentreadererror.md)
  An error type that indicates problems when preparing a mobile document reader session and performing document requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadererror)*