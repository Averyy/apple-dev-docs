# PKPaymentAuthorizationStatus.failure

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

Merchant failed to authorize the transaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case failure
```

#### Discussion

Use this value for all failures other than PIN-related failures (which have their own status constants), such as for an invalid address, contact, or unknown error.

List the specific errors in the [`errors`](pkpaymentrequestshippingcontactupdate/errors.md) array.

## See Also

- [PKPaymentAuthorizationStatus.success](pkpaymentauthorizationstatus/success.md)
  Merchant successfully authorized the transaction, or the transaction is expected to succeed.
- [PKPaymentAuthorizationStatus.invalidBillingPostalAddress](pkpaymentauthorizationstatus/invalidbillingpostaladdress.md)
  Invalid or unusable billing address.
- [PKPaymentAuthorizationStatus.invalidShippingPostalAddress](pkpaymentauthorizationstatus/invalidshippingpostaladdress.md)
  Invalid or unusable shipping address.
- [PKPaymentAuthorizationStatus.invalidShippingContact](pkpaymentauthorizationstatus/invalidshippingcontact.md)
  Invalid or incomplete shipping contact.
- [PKPaymentAuthorizationStatus.pinRequired](pkpaymentauthorizationstatus/pinrequired.md)
  Transaction requires PIN entry.
- [PKPaymentAuthorizationStatus.pinIncorrect](pkpaymentauthorizationstatus/pinincorrect.md)
  Incorrect PIN entered.
- [PKPaymentAuthorizationStatus.pinLockout](pkpaymentauthorizationstatus/pinlockout.md)
  PIN retry limit exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/failure)*