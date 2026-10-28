# shippingMethod

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The user-selected shipping method for this transaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var shippingMethod: PKShippingMethod? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) PKShippingMethod * shippingMethod;
```

## Discussion

A value is set for this property only if the corresponding payment request specified available shipping methods in the [`shippingMethods`](../pkpaymentrequest/shippingmethods.md) property of the [`PKPaymentRequest`](../pkpaymentrequest.md) object. Otherwise, the value is `nil.`

## See Also

### Working with billing and shipping information
- [var billingContact: PKContact?](./billingcontact.md)
  The user-selected billing address for this transaction.
- [var shippingContact: PKContact?](./shippingcontact.md)
  The user-selected shipping address for this transaction.
- [class PKContact](../pkcontact.md)
  An object that encapsulates contact information needed for billing and shipping.
- [class PKShippingMethod](../pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpayment/shippingmethod)*