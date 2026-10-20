# PaymentCardReaderError.unsupported

**Framework**: ProximityReader  
**Kind**: case  
**Role**: Case

An error that indicates unsupported hardware or a problem with the device.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
case unsupported
```

## See Also

### Getting the error code
- [PaymentCardReaderError.accountAlreadyLinked](./accountalreadylinked.md)
  An error that indicates the merchant already accepted the Terms and Conditions.
- [PaymentCardReaderError.accountDeactivated](./accountdeactivated.md)
  An error that indicates the linked Apple Account account has been deactivated by the merchant.
- [PaymentCardReaderError.accountLinkingCancelled](./accountlinkingcancelled.md)
  An error that indicates the user cancelled the linking or relinking operation.
- [PaymentCardReaderError.accountLinkingCheckFailed](./accountlinkingcheckfailed.md)
  An error that indicates the system couldn’t check the account status of the merchant.
- [PaymentCardReaderError.accountLinkingFailed](./accountlinkingfailed.md)
  An error that indicates the system couldn’t link or relink the merchant using the provided Apple Account.
- [PaymentCardReaderError.accountLinkingRequiresiCloudSignIn](./accountlinkingrequiresicloudsignin.md)
  An error that indicates the merchant must be signed into an Apple Account on the device to accept the Terms and Conditions.
- [PaymentCardReaderError.accountNotLinked](./accountnotlinked.md)
  An error that indicates the merchant must accept the Terms and Conditions with a valid Apple Account.
- [PaymentCardReaderError.backgroundRequestNotAllowed](./backgroundrequestnotallowed.md)
  An error that results from requests to the reader while the host app is in the background state.
- [PaymentCardReaderError.deviceBanned(_:)](./devicebanned%28_%29.md)
  An error that indicates the device is banned until the specified date.
- [PaymentCardReaderError.emptyReaderToken](./emptyreadertoken.md)
  An error that indicates the reader token is empty, which is invalid.
- [PaymentCardReaderError.invalidMerchant](./invalidmerchant.md)
  An error that indicates the merchant is invalid or unknown.
- [PaymentCardReaderError.invalidReaderToken(_:)](./invalidreadertoken%28_%29.md)
  An error that indicates an invalid, non-empty reader token.
- [PaymentCardReaderError.merchantBlocked](./merchantblocked.md)
  An error that indicates the merchant is blocked.
- [PaymentCardReaderError.modelNotSupported](./modelnotsupported.md)
  An error that indicates the current device isn’t supported.
- [PaymentCardReaderError.networkAuthenticationError](./networkauthenticationerror.md)
  An authentication error that occurred during connection to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadererror/unsupported)*