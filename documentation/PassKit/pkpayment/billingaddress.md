# billingAddress

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The user-selected billing address for this transaction.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0

> **Deprecated**: This property is deprecated. Use [`billingContact`](./billingcontact.md) instead.

## Declaration

```swift
unowned(unsafe) var billingAddress: ABRecord? { get }
```

```objc
@property (nonatomic, assign, readonly, nullable) ABRecordRef billingAddress;
```

#### Discussion

Only the fields specified in the the [`requiredBillingAddressFields`](../pkpaymentrequest/requiredbillingaddressfields.md) property of the [`PKPaymentRequest`](../pkpaymentrequest.md) object are populated. If no required billing fields were specified, the value of this property is `nil`.

## See Also

### Deprecated
- [var shippingAddress: ABRecord?](./shippingaddress.md)
  The user-selected shipping address for this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpayment/billingaddress)*