# PKPaymentAuthorizationStatus.pinRequired

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Transaction requires PIN entry.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case pinRequired
```

```c
PKPaymentAuthorizationStatusPINRequired
```

## Discussion

Pass this constant to the completion block when the payment requires a PIN but the token did not include one—for example, when the bank’s and app’s PIN limits are out of sync. Apple Pay automatically prompts the user to enter their PIN.

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
- [PKPaymentAuthorizationStatus.pinIncorrect](./pinincorrect.md)
  Incorrect PIN entered.
- [PKPaymentAuthorizationStatus.pinLockout](./pinlockout.md)
  PIN retry limit exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/pinrequired)*