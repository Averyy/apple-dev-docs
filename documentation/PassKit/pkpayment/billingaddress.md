# billingAddress

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The user-selected billing address for this transaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

## Declaration

```swift
unowned(unsafe) var billingAddress: ABRecord? { get }
```

#### Discussion

Only the fields specified in the the [`requiredBillingAddressFields`](pkpaymentrequest/requiredbillingaddressfields.md) property of the [`PKPaymentRequest`](pkpaymentrequest.md) object are populated. If no required billing fields were specified, the value of this property is `nil`.

## See Also

- [var shippingAddress: ABRecord?](pkpayment/shippingaddress.md)
  The user-selected shipping address for this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpayment/billingaddress)*