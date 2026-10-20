# billingContact

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The user-selected billing address for this transaction.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var billingContact: PKContact? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) PKContact * billingContact;
```

#### Discussion

Only the fields specified in the [`requiredBillingAddressFields`](../pkpaymentrequest/requiredbillingaddressfields.md) property of the [`PKPaymentRequest`](../pkpaymentrequest.md) object are populated. If no required billing fields were specified, the value of this property is `nil`.

## See Also

### Working with billing and shipping information
- [var shippingContact: PKContact?](./shippingcontact.md)
  The user-selected shipping address for this transaction.
- [var shippingMethod: PKShippingMethod?](./shippingmethod.md)
  The user-selected shipping method for this transaction.
- [class PKContact](../pkcontact.md)
  An object that encapsulates contact information needed for billing and shipping.
- [class PKShippingMethod](../pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpayment/billingcontact)*