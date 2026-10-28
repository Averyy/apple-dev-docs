# PKPaymentAuthorizationStatus.pinLockout

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

PIN retry limit exceeded.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case pinLockout
```

```c
PKPaymentAuthorizationStatusPINLockout
```

## Discussion

Pass this constant to the completion block when the bank informs you that the user has exceeded the allowed number of attempts to enter their PIN.

## See Also

### Payment authorization status constants
- [PKPaymentAuthorizationStatus.success](./success.md)
  Merchant successfully authorized the transaction, or the transaction is expected to succeed.
- [PKPaymentAuthorizationStatus.failure](./failure.md)
  Merchant failed to authorize the transaction.
- [PKPaymentAuthorizationStatus.invalidBillingPostalAddress](./invalidbillingpostaladdress.md)
  Invalid or unusable billing address.
- [PKPaymentAuthorizationStatus.invalidShippingPostalAddress](./invalidshippingpostaladdress.md)
  Invalid or unusable shipping address.
- [PKPaymentAuthorizationStatus.invalidShippingContact](./invalidshippingcontact.md)
  Invalid or incomplete shipping contact.
- [PKPaymentAuthorizationStatus.pinRequired](./pinrequired.md)
  Transaction requires PIN entry.
- [PKPaymentAuthorizationStatus.pinIncorrect](./pinincorrect.md)
  Incorrect PIN entered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pinlockout)*