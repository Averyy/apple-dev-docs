# PaymentCardReaderError.invalidReaderToken(_:)

**Framework**: ProximityReader  
**Kind**: case

An error that indicates an invalid, non-empty reader token.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
case invalidReaderToken(String?)
```

#### Discussion

There is an issue with the token provided by your payment service provider, check the description string for more details.

## See Also

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
- [PaymentCardReaderError.merchantBlocked](paymentcardreadererror/merchantblocked.md)
  An error that indicates the merchant is blocked.
- [PaymentCardReaderError.modelNotSupported](paymentcardreadererror/modelnotsupported.md)
  An error that indicates the current device isn’t supported.
- [PaymentCardReaderError.networkAuthenticationError](paymentcardreadererror/networkauthenticationerror.md)
  An authentication error that occurred during connection to the server.
- [PaymentCardReaderError.networkError](paymentcardreadererror/networkerror.md)
  A network error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadererror/invalidreadertoken(_:))*