# PKPaymentAuthorizationStatus.failure

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

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

```c
PKPaymentAuthorizationStatusFailure
```

## Discussion

Use this value for all failures other than PIN-related failures (which have their own status constants), such as for an invalid address, contact, or unknown error.

List the specific errors in the [`errors`](../pkpaymentrequestshippingcontactupdate/errors.md) array.

## See Also

### Payment authorization status constants
- [PKPaymentAuthorizationStatus.success](./success.md)
  Merchant successfully authorized the transaction, or the transaction is expected to succeed.
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
- [PKPaymentAuthorizationStatus.pinLockout](./pinlockout.md)
  PIN retry limit exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationstatus/failure)*