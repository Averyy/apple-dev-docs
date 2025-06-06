# PKPaymentAuthorizationStatus.success

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

Merchant successfully authorized the transaction, or the transaction is expected to succeed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case success
```

#### Discussion

Use this value when the transaction is successful and no errors exist on the payment sheet.

## See Also

- [PKPaymentAuthorizationStatus.failure](pkpaymentauthorizationstatus/failure.md)
  Merchant failed to authorize the transaction.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/success)*