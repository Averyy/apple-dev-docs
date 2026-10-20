# PKPaymentAuthorizationStatus.invalidShippingPostalAddress

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Invalid or unusable shipping address.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`PKPaymentAuthorizationResult`](../pkpaymentauthorizationresult.md) with the [`PKPaymentAuthorizationStatus.failure`](./failure.md) status instead.  Include the result of [`paymentShippingAddressInvalidError(withKey:localizedDescription:)`](../pkpaymentrequest/paymentshippingaddressinvaliderror%28withkey,localizeddescription%29.md) in the errors array.

## Declaration

```swift
case invalidShippingPostalAddress
```

```c
PKPaymentAuthorizationStatusInvalidShippingPostalAddress
```

## See Also

### Payment authorization status constants
- [PKPaymentAuthorizationStatus.success](./success.md)
  Merchant successfully authorized the transaction, or the transaction is expected to succeed.
- [PKPaymentAuthorizationStatus.failure](./failure.md)
  Merchant failed to authorize the transaction.
- [PKPaymentAuthorizationStatus.invalidBillingPostalAddress](./invalidbillingpostaladdress.md)
  Invalid or unusable billing address.
- [PKPaymentAuthorizationStatus.invalidShippingContact](./invalidshippingcontact.md)
  Invalid or incomplete shipping contact.
- [PKPaymentAuthorizationStatus.pinRequired](./pinrequired.md)
  Transaction requires PIN entry.
- [PKPaymentAuthorizationStatus.pinIncorrect](./pinincorrect.md)
  Incorrect PIN entered.
- [PKPaymentAuthorizationStatus.pinLockout](./pinlockout.md)
  PIN retry limit exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/invalidshippingpostaladdress)*